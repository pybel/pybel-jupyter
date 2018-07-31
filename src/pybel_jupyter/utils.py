# -*- coding: utf-8 -*-

"""Utilities for PyBEL-Jupyter."""

import os

import jinja2
from pybel.canonicalize import calculate_canonical_name
from pybel.struct.filters import filter_nodes
from pybel.struct.filters.node_predicate_builders import data_missing_key_builder

from .constants import VERSION

__all__ = [
    'add_canonical_names',
    'render_template',
    'get_version',
]


def get_version():
    """Get the software version of PyBEL-Jupyter.

    :rtype: str
    """
    return VERSION


CNAME = 'cname'
node_missing_cname = data_missing_key_builder(CNAME)


def add_canonical_names(graph, replace=False):
    """Add a canonical name to each node's data dictionary if they are missing, in place.

    :param pybel.BELGraph graph: A BEL graph
    :param bool replace: Should the canonical names be recalculated?
    """
    nodes = graph if replace else filter_nodes(graph, node_missing_cname)

    for node in nodes:
        graph.node[node][CNAME] = calculate_canonical_name(graph, node)


def build_template_environment(here):
    """Build a custom templating environment so Flask apps can get data from lots of different places.

    :param str here: Give this the result of :code:`os.path.dirname(os.path.abspath(__file__))`
    :rtype: jinja2.Environment
    """
    template_environment = jinja2.Environment(
        autoescape=False,
        loader=jinja2.FileSystemLoader(os.path.join(here, 'templates')),
        trim_blocks=False
    )

    template_environment.globals['STATIC_PREFIX'] = here + '/static/'

    return template_environment


def build_template_renderer(file):
    """Build a render template function.

    :param str file: The location of the current file. Pass it :code:`__file__` like in the example below.

    >>> render_template = build_template_renderer(__file__)
    """
    here = os.path.dirname(os.path.abspath(file))
    template_environment = build_template_environment(here)

    def render_template_enclosure(template_filename, **context):
        """Render a template as a unicode string.

        :param str template_filename: The name of the file to render in the template directory
        :param dict context: The variables to template
        :rtype: str
        """
        return template_environment.get_template(template_filename).render(context)

    return render_template_enclosure


#: Renders templates from pybel_tools.visualization.templates folder
render_template = build_template_renderer(__file__)
