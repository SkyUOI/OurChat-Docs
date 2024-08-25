# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os

project = "OurChat-Docs"
copyright = "2024, OutChat"
author = "OutChat"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser"]

templates_path = ["_templates"]
exclude_patterns = []

default_lang = "en"
support_languages = ["en", "zh_CN"]
language = os.getenv("READTHEDOCS_LANGUAGE", default_lang)
if language not in support_languages:
    print(f"Unknown Language:{language}")
    language = default_lang

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]

myst_enable_extensions = [
    # "amsmath",
    # "attrs_inline",
    # "colon_fence",
    # "deflist",
    # "dollarmath",
    # "fieldlist",
    # "html_admonition",
    # "html_image",
    # "linkify",
    # "replacements",
    # "smartquotes",
    # "strikethrough",
    # "substitution",
    # "tasklist",
]
myst_heading_anchors = 3

locale_dirs = ["locale/"]
gettext_compact = True
