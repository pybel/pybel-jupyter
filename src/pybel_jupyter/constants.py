# -*- coding: utf-8 -*-

"""Constants for PyBEL-Jupyter."""

from pybel.constants import ABUNDANCE, BIOPROCESS, COMPLEX, COMPOSITE, GENE, MIRNA, PATHOLOGY, PROTEIN, REACTION, RNA

VERSION = '0.1.0'

#: The color map defining the node colors in visualization
DEFAULT_COLOR_MAP = {
    PROTEIN: "#1F77B4",
    PATHOLOGY: "#FF7F0E",
    BIOPROCESS: "#2CA02C",
    MIRNA: "#D62728",
    COMPLEX: "#9467bd",
    COMPOSITE: "#9467bd",
    REACTION: "#8c564b",
    GENE: "#e377c2",
    ABUNDANCE: "#bcbd22",
    RNA: "#17becf"
}
