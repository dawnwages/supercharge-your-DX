# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Supercharge Python DX with VS Code'
copyright = '2024, Dawn Wages'
author = 'Dawn Wages'
release = '2.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.githubpages",
]

templates_path = ['_templates']
exclude_patterns = []

html_theme_options = {
    #'analytics_anonymize_ip': False,
    #'logo_only': False,
    "display_version": True,
    "prev_next_buttons_location": 'bottom',
    "style_external_links": False,
    "navigation_with_keys": True,
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 3,
    "includehidden": True,
    "titles_only": False,
    "vcs_pageview_mode": '',
}
html_title = "Supercharge 🐍 DX with VS Code"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
