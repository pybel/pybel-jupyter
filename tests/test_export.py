# -*- coding: utf-8 -*-

"""Test for export functions in PyBEL-Jupyter."""

import unittest

from pybel.examples import sialic_acid_graph
from pybel_jupyter import to_html


class TestHTML(unittest.TestCase):
    """Text HTML functions."""

    def test_to_html(self):
        """Test export to HTML."""
        html = to_html(sialic_acid_graph)
        self.assertIsNotNone(html)
