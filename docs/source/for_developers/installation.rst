************
Installation
************

Virtual Environment
===================

* First, you need to create a virtual environment.

.. code-block:: bash

    cd GBOmonitoring
    /users/gbosdd/python/bin/python3.11 -m venv GBOmonitoring-venv-py3.11
    source GBOmonitoring-venv-py3.11/bin/activate
    pip install -r requirements.txt

Sphinx Autobuilds
=================

.. code-block:: bash

    cd docs
    cp .docs-env.template .docs-env

* Add values for `DOCS_ROOT`, `DOCS_HOST`, and `DOCS_PORT` in `.docs-env`
* Start the autobuild

.. code-block:: bash
    
    source .docs-env
    startdocs

* Go to `http://{$DOCS_HOST}:{$DOCS_PORT}` in a web browser. You should now see the documentation with live edits as you save changes. 