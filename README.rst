PyBEL-Jupyter |build| |docs|
============================
A PyBEL extension for Jupyter notebooks.

.. warning::

    This module has been included in PyBEL as of v0.14.0, so it has been deprecated. You can keep using it like normal,
    though.

Installation |pypi_version| |python_versions| |pypi_license|
------------------------------------------------------------
``pybel_jupyter`` can be installed easily from `PyPI <https://pypi.python.org/pypi/pybel-jupyter>`_ with the following
code in your favorite terminal:

.. code-block:: sh

    $ pip install pybel-jupyter

or from the latest code on `GitHub <https://github.com/pybel/pybel-jupyter>`_ with:

.. code-block:: sh

    $ pip install git+https://github.com/pybel/pybel-jupyter.git

Getting Started
---------------
Inside a Jupyter notebook, run the following code at the end of the cell to get an interactive visualization:

.. code-block:: python

    >>> from pybel.examples import sialic_acid_graph
    >>> from pybel_jupyter import to_jupyter
    >>> to_jupyter(sialic_acid_graph)

.. |build| image:: https://travis-ci.com/pybel/pybel-jupyter.svg?branch=master
    :target: https://travis-ci.com/pybel/pybel-jupyter

.. |docs| image:: https://readthedocs.org/projects/pybel-jupyter/badge/?version=latest
    :target: https://pybel.readthedocs.io/projects/jupyter/en/latest/?badge=latest
    :alt: Documentation Status

.. |python_versions| image:: https://img.shields.io/pypi/pyversions/pybel-jupyter.svg
    :alt: Stable Supported Python Versions

.. |pypi_version| image:: https://img.shields.io/pypi/v/pybel-jupyter.svg
    :alt: Current version on PyPI

.. |pypi_license| image:: https://img.shields.io/pypi/l/pybel-jupyter.svg
    :alt: MIT License
