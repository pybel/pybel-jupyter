# -*- coding: utf-8 -*-

"""A PyBEL extension for Jupyter notebooks.

Installation
------------
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
"""

import warnings

from pybel.io.jupyter import to_html, to_html_file, to_jupyter, to_jupyter_str

__all__ = [
    'to_html',
    'to_html_file',
    'to_jupyter',
    'to_jupyter_str',
]

warnings.warn(
    'pybel_jupyter has been incorporated directly in pybel.'
    ' Please make imports directly from pybel.io.jupyter',
    DeprecationWarning
)
