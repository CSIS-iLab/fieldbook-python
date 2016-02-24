===============================
Fieldbook API Client
===============================

A Fieldbook python3.x client. Currently a read-only client.

* Free software: ISC license

Installation
--------

`pip install git+https://github.com/CSIS-iLab/fieldbook-python.git`

Usage
-------

A basic example:

::

    from fieldbook import Fieldbook

    client = Fieldbook(key='yourkey', secret='yoursecret', book_id='fieldbook_id')

    # list sheets in book
    print(client.sheets())

    # Request data from a sheet, with filters
    data = client.get('people', params={'first_name': 'John', 'include': 'first_name,last_name,alias'})


See the Fieldbook_ API docs for more information.

.. _Fieldbook: https://github.com/fieldbook/api-docs

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
