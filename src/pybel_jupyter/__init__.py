# -*- coding: utf-8 -*-

"""A PyBEL extension for Jupyter notebooks."""

from .inline import to_jupyter, to_jupyter_str  # noqa: F401
from .utils import get_version  # noqa: F401
from .visualization import to_html, to_html_file, to_html_path  # noqa: F401

__all__ = [
    'to_html',
    'to_html_file',
    'to_html_path',
    'to_jupyter',
    'to_jupyter_str',
]

__version__ = '0.1.0'

__title__ = 'pybel_jupyter'
__description__ = 'A PyBEL extension for Jupyter notebooks'
__url__ = 'https://github.com/pybel/pybel-jupyter'

__author__ = 'Charles Tapley Hoyt'
__email__ = 'charles.hoyt@scai.fraunhofer.de'

__license__ = 'MIT License'
__copyright__ = 'Copyright (c) 2018 Charles Tapley Hoyt'
