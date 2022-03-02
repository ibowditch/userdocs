# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'RFS Tag'
# rst_epilog = '.. |project| replace:: %s' % project

# logo = "assets/images/nfc-logo-red-sm.png"

copyright = '2022, Ian Bowditch'
author = 'Ian Bowditch'
# hostsite = "eb.fred"

# The full version, including alpha/beta/rc tags
release = '1.0'
homepage = "http://kuringai.rfstag.org/bfb/"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
import os
import sys
sys.path.insert(0, os.path.abspath("."))

# "sphinx_autodoc_typehints",

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    'sphinx_panels',
]

intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
    # "bushfire": ("http://kuringai.rfstag.org/bfb/indexawsmt", None),
}
myst_url_schemes = ["http", "https", ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'       # 'sphinxdoc'        # 'alabaster'

html_theme_options = {
    "home_page_in_toc": True,
    "show_navbar_depth": 3,
}


html_title = "RFS Tag"      #  - Electronic Sign-in"

html_logo = "assets/images/nfc-logo-red-sm.png"      # "_static/python-logo-generic.svg"

html_css_files = [#"https://cdn.jsdelivr.net/npm/bulma@0.9.2/css/bulma.min.css",     # "alabaster.css",
                  #"https://code.iconify.design/2/2.1.2/iconify.min.js",
                    "custom.css", "css/hacks.css",
                    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"]

# "custom2.css",

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

myst_enable_extensions = [
    "colon_fence",
    "substitution",
    "deflist",
]

myst_substitutions = {
    "snippet": "I'm a **substitution**",
    # "bushfire2": "http://kuringai.rfstag.org/bfb/kiosk/ib2",
}

rst_prolog = """
.. include:: s5defs.txt

"""

rst_epilog = "\n.. include:: .special.rst\n"


# html_sidebars = {
#   '**': [
#     "about.html",
#     "navigation.html",
#     "relations.html",
#     "searchbox.html",
#     "donate.html",
#   ]
# }


# html_theme = "sphinx_book_theme"
# html_sidebars = {
#     "**": ["sbt-sidebar-nav.html", "sbt-sidebar-footer.html"]
# }

# templates_path = ["_templates"]
# html_sidebars = {
#   '**': [
#  #   "about.html",
#  #    "navigation.html",
#  #    "relations.html",
#     # "luv_sphinx.html",
#     "searchbox.html",
#     # "donate.html",
#   ]
# }

# html_sidebars = {
#     "**": ["sbt-sidebar-nav.html", "sbt-sidebar-footer.html"]
# }
#
# html_sidebars = {
#     "reference/blog/*": [
#         "sidebar-logo.html",
#         "search-field.html",
#         "postcard.html",
#         "recentposts.html",
#         "tagcloud.html",
#         "categories.html",
#         "archives.html",
#         "sbt-sidebar-nav.html",
#         "sbt-sidebar-footer.html",
#     ]
# }






# extlinks = {'issue': ('https://github.com/sphinx-doc/sphinx/issues/%s','issue %s'),
#             'bushfire': ('http://kuringai.rfstag.org/bfb/%s','bushpage %s'),
#             }

numfig = True