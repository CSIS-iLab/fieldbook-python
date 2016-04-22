from fieldbook import Fieldbook
import os
import json
import time
import configparser

import argparse


def download(args):
    friendly = getattr(args, 'friendly', False)
    verbose = getattr(args, 'verbose', 0)
    config = configparser.ConfigParser()
    config.read_file(args.configfile)

    for section_name, section_conf in config.items():
        if section_name != 'DEFAULT':
            if verbose > 2:
                print("Reading config for '{}'".format(section_name))
            book_id = section_conf.get('id')
            book_key = section_conf.get('key')
            book_secret = section_conf.get('secret')
            outdir = section_conf.get('outdir')
            if not os.path.exists(outdir):
                raise FileNotFoundError(outdir)
            outpath = os.path.abspath(os.path.join(outdir, section_name))
            if not os.path.exists(outpath):
                if verbose > 0:
                    print("Creating '{}'".format(outpath))
                os.mkdir(outpath)
            if book_id and book_key and book_secret:
                book = Fieldbook(book_id, key=book_key, secret=book_secret)
                sheet_names = book.sheets()
                if verbose > 2:
                    print("Processing fieldbook '{}'".format(book_id))

                for sheet in sheet_names:
                    if verbose > 1:
                        print("Downloading '{}'".format(sheet))
                    data = book.list(sheet)
                    outtfile = os.path.join(outpath, "{}.json".format(sheet))
                    if verbose > 2:
                        print("Saving data to '{}'".format(outtfile))
                    json.dump(data, open(outtfile, 'w'), indent=4)
                    if friendly:
                        time.sleep(0.05)
            else:
                print("'{}' section must include `id`, `key`, and `secret`.".format(section_name))


def main():
    parser = argparse.ArgumentParser(description='Download Fieldbok data')
    parser.add_argument('--verbose', '-v', action='count')
    subparsers = parser.add_subparsers(title='subcommands', dest='subcommand')
    dl_parser = subparsers.add_parser('download', help='Download fieldbooks using ini-style config')
    dl_parser.add_argument(
        '--friendly',
        action='store_true',
        help='Throttle the number of API calls to Fieldbook'
    )
    dl_parser.add_argument(
        'configfile',
        help='INI-style config file that defined fieldbooks to download. `id`, `key`, and `secret` are required arguments. `outdir` is optional.',
        type=argparse.FileType('r')
    )
    dl_parser.set_defaults(func=download)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.exit(message=parser.format_help())


if __name__ == '__main__':
    main()
