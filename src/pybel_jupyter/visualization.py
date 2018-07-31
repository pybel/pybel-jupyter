# -*- coding: utf-8 -*-

"""Convert BEL graphs to HTML.

This module provides functions for making HTML visualizations of BEL Graphs. Because the :class:`pybel.BELGraph`
inherits from :class:`networkx.MultiDiGraph`, it can also be visualized using :mod:`networkx`
`library <https://networkx.github.io/documentation/latest/reference/drawing.html>`_.

"""

from __future__ import print_function

import json
import os

from pybel import to_jsons

from .constants import DEFAULT_COLOR_MAP
from .utils import add_canonical_names, render_template

__all__ = [
    'to_html',
    'to_html_file',
    'to_html_path',
]


def build_graph_context(graph, color_map=None):
    """Build the data dictionary to be used by the Jinja templating engine in :py:func:`to_html`.

    :param pybel.BELGraph graph: A BEL graph
    :param color_map: A dictionary from PyBEL internal node functions to CSS color strings like #FFEE00.
                    Defaults to :data:`default_color_map`
    :type color_map: Optional[dict[str,str]]
    :return: JSON context for rendering
    :rtype: dict
    """
    add_canonical_names(graph)

    color_map = DEFAULT_COLOR_MAP if color_map is None else color_map

    return {
        'json': to_jsons(graph),
        'cmap': json.dumps(color_map),
        'number_nodes': graph.number_of_nodes(),
        'number_edges': graph.number_of_edges()
    }


def to_html(graph, color_map=None):
    """Create an HTML visualization for the given JSON representation of a BEL graph.

    :param pybel.BELGraph graph: A BEL graph
    :param color_map: A dictionary from PyBEL internal node functions to CSS color strings like #FFEE00.
                    Defaults to :data:`default_color_map`
    :type color_map: Optional[dict[str,str]]
    :return: HTML string representing the graph
    :rtype: str
    """
    context = build_graph_context(graph, color_map=color_map)
    return render_template('graph_template.html', context=context)


def to_html_file(graph, file, color_map=None):
    """Write the HTML visualization to a file or file-like.

    :param pybel.BELGraph graph: A BEL graph
    :param color_map: A dictionary from PyBEL internal node functions to CSS color strings like #FFEE00.
                    Defaults to :data:`default_color_map`
    :type color_map: Optional[dict[str,str]]
    :param file file: A writable file or file-like
    """
    print(to_html(graph, color_map=color_map), file=file)


def to_html_path(graph, path, color_map=None):
    """Write the HTML visualization to a file specified by the file path.

    :param pybel.BELGraph graph: A BEL graph
    :param dict[str,str] color_map: A dictionary from PyBEL internal node functions to CSS color strings like #FFEE00.
                    Defaults to :data:`default_color_map`
    :param str path: The file path
    """
    with open(os.path.expanduser(path), 'w') as file:
        to_html_file(graph, file, color_map=color_map)
