# -*- coding: utf-8 -*-

"""Utilities for displaying graphs with inline HTML in Jupyter Notebooks."""

from random import sample

from IPython.display import Javascript
from pybel.io import to_jsons

from .constants import DEFAULT_COLOR_MAP
from .utils import add_canonical_names, render_template

__all__ = [
    'to_jupyter',
    'to_jupyter_str'
]

DEFAULT_WIDTH = 1000
DEFAULT_HEIGHT = 650


def _generate_id():
    """Generate a random string of letters."""
    return "".join(sample('abcdefghjkmopqrstuvqxyz', 16))


def to_jupyter(graph, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, color_map=None, replace_cnames=False):
    """Display a BEL graph inline in a Jupyter notebook.

    To use successfully, make run as the last statement in a cell inside a Jupyter notebook.

    :param pybel.BELGraph graph: A BEL graph
    :param int width: The width of the visualization window to render
    :param int height: The height of the visualization window to render
    :param dict color_map: A dictionary from PyBEL internal node functions to CSS color strings like #FFEE00. Defaults
                    to :data:`default_color_map`
    :return: An IPython notebook Javascript object
    :rtype: :class:`IPython.display.Javascript`
    """
    return Javascript(to_jupyter_str(
        graph,
        width=width,
        height=height,
        color_map=color_map,
        replace_cnames=replace_cnames
    ))


def to_jupyter_str(graph, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, color_map=None, replace_cnames=False):
    """Return the string to be javascript-ified by the Jupyter notebook function :class:`IPython.display.Javascript`.

    :param pybel.BELGraph graph: A BEL graph
    :param int width: The width of the visualization window to render
    :param int height: The height of the visualization window to render
    :param dict color_map: A dictionary from PyBEL internal node functions to CSS color strings like #FFEE00. Defaults
                    to :data:`default_color_map`
    :return: The javascript string to turn into magic
    :rtype: str
    """
    add_canonical_names(graph, replace=replace_cnames)
    gjson = to_jsons(graph, sort_keys=True)
    chart_id = _generate_id()

    if color_map is None:
        color_map = DEFAULT_COLOR_MAP

    return render_template(
        'pybel_jupyter.js',
        graph=gjson,
        chart=chart_id,
        width=width,
        height=height,
        color_map=color_map
    )
