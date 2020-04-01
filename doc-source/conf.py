#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  !/usr/bin/env python
#   -*- coding: utf-8 -*-
#
#  filename.py
#
#  Copyright (c) 2019 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as
#  published by the Free Software Foundation; either version 3 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

#### No need to change anything in this file ####

import os
import re
import sys

sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('..'))

from sphinx.locale import _

from chemistry_tools import __author__, __version__, __copyright__
from __pkginfo__ import github_username, modname

github_url = f"https://github.com/{github_username}/{modname}"

rst_prolog = f""".. |pkgname| replace:: {modname}
.. |pkgname2| replace:: ``{modname}``
.. |browse_github| replace:: `Browse the GitHub Repository <{github_url}>`__
.. |ghurl| replace:: {github_url}
"""

project = modname
slug = re.sub(r'\W+', '-', modname.lower())
version = __version__
release = __version__
author = __author__
copyright = __copyright__
language = 'en'

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinxcontrib.httpdomain',
]

templates_path = ['_templates']
source_suffix = '.rst'
exclude_patterns = []

master_doc = 'index'
suppress_warnings = ['image.nonlocal_uri']
pygments_style = 'default'

intersphinx_mapping = { # Is this where those mystery links are specified?
    'rtd': ('https://docs.readthedocs.io/en/latest/', None),
    'sphinx': ('http://www.sphinx-doc.org/en/stable/', None),
}

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': False,  # True will show just the logo
}
html_theme_path = ["../.."]
#html_logo = "logo/pyms.png"
html_show_sourcelink = False    # True will show link to source

html_context = {
    # Github Settings
    "display_github": True, # Integrate GitHub
    "github_user": github_username, # Username
    "github_repo": modname, # Repo name
    "github_version": "master", # Version
    "conf_py_path": "/", # Path in the checkout to the docs root
}

htmlhelp_basename = slug

latex_documents = [
  ('index', '{0}.tex'.format(slug), modname, author, 'manual'),
]

man_pages = [
    ('index', slug, modname, [author], 1)
]

texinfo_documents = [
  ('index', slug, modname, author, slug, modname, 'Miscellaneous'),
]


# Extensions to theme docs
def setup(app):
    from sphinx.domains.python import PyField
    from sphinx.util.docfields import Field

    app.add_object_type(
        'confval',
        'confval',
        objname='configuration value',
        indextemplate='pair: %s; configuration value',
        doc_field_types=[
            PyField(
                'type',
                label=_('Type'),
                has_arg=False,
                names=('type',),
                bodyrolename='class'
            ),
            Field(
                'default',
                label=_('Default'),
                has_arg=False,
                names=('default',),
            ),
        ]
    )