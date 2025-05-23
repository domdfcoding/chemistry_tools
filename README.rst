=====================
Chemistry Tools
=====================

.. start short_desc

**Python tools for analysis of chemical compounds.**

.. end short_desc

.. start shields

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Docs
	  - |docs| |docs_check|
	* - Tests
	  - |actions_linux| |actions_windows| |actions_macos| |coveralls|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Anaconda
	  - |conda-version| |conda-platform|
	* - Activity
	  - |commits-latest| |commits-since| |maintained| |pypi-downloads|
	* - QA
	  - |codefactor| |actions_flake8| |actions_mypy|
	* - Other
	  - |license| |language| |requires|

.. |docs| image:: https://img.shields.io/readthedocs/chemistry-tools/latest?logo=read-the-docs
	:target: https://chemistry-tools.readthedocs.io/en/latest
	:alt: Documentation Build Status

.. |docs_check| image:: https://github.com/domdfcoding/chemistry_tools/workflows/Docs%20Check/badge.svg
	:target: https://github.com/domdfcoding/chemistry_tools/actions?query=workflow%3A%22Docs+Check%22
	:alt: Docs Check Status

.. |actions_linux| image:: https://github.com/domdfcoding/chemistry_tools/workflows/Linux/badge.svg
	:target: https://github.com/domdfcoding/chemistry_tools/actions?query=workflow%3A%22Linux%22
	:alt: Linux Test Status

.. |actions_windows| image:: https://github.com/domdfcoding/chemistry_tools/workflows/Windows/badge.svg
	:target: https://github.com/domdfcoding/chemistry_tools/actions?query=workflow%3A%22Windows%22
	:alt: Windows Test Status

.. |actions_macos| image:: https://github.com/domdfcoding/chemistry_tools/workflows/macOS/badge.svg
	:target: https://github.com/domdfcoding/chemistry_tools/actions?query=workflow%3A%22macOS%22
	:alt: macOS Test Status

.. |actions_flake8| image:: https://github.com/domdfcoding/chemistry_tools/workflows/Flake8/badge.svg
	:target: https://github.com/domdfcoding/chemistry_tools/actions?query=workflow%3A%22Flake8%22
	:alt: Flake8 Status

.. |actions_mypy| image:: https://github.com/domdfcoding/chemistry_tools/workflows/mypy/badge.svg
	:target: https://github.com/domdfcoding/chemistry_tools/actions?query=workflow%3A%22mypy%22
	:alt: mypy status

.. |requires| image:: https://dependency-dash.repo-helper.uk/github/domdfcoding/chemistry_tools/badge.svg
	:target: https://dependency-dash.repo-helper.uk/github/domdfcoding/chemistry_tools/
	:alt: Requirements Status

.. |coveralls| image:: https://img.shields.io/coveralls/github/domdfcoding/chemistry_tools/master?logo=coveralls
	:target: https://coveralls.io/github/domdfcoding/chemistry_tools?branch=master
	:alt: Coverage

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/chemistry_tools?logo=codefactor
	:target: https://www.codefactor.io/repository/github/domdfcoding/chemistry_tools
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/chemistry_tools
	:target: https://pypi.org/project/chemistry_tools/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/chemistry_tools?logo=python&logoColor=white
	:target: https://pypi.org/project/chemistry_tools/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/chemistry_tools
	:target: https://pypi.org/project/chemistry_tools/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/chemistry_tools
	:target: https://pypi.org/project/chemistry_tools/
	:alt: PyPI - Wheel

.. |conda-version| image:: https://img.shields.io/conda/v/domdfcoding/chemistry_tools?logo=anaconda
	:target: https://anaconda.org/domdfcoding/chemistry_tools
	:alt: Conda - Package Version

.. |conda-platform| image:: https://img.shields.io/conda/pn/domdfcoding/chemistry_tools?label=conda%7Cplatform
	:target: https://anaconda.org/domdfcoding/chemistry_tools
	:alt: Conda - Platform

.. |license| image:: https://img.shields.io/github/license/domdfcoding/chemistry_tools
	:target: https://github.com/domdfcoding/chemistry_tools/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/chemistry_tools
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/chemistry_tools/v1.1.1
	:target: https://github.com/domdfcoding/chemistry_tools/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/chemistry_tools
	:target: https://github.com/domdfcoding/chemistry_tools/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2025
	:alt: Maintenance

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/chemistry_tools
	:target: https://pypi.org/project/chemistry_tools/
	:alt: PyPI - Downloads

.. end shields


Installation
================

.. start installation

``chemistry_tools`` can be installed from PyPI or Anaconda.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install chemistry_tools

To install with ``conda``:

	* First add the required channels

	.. code-block:: bash

		$ conda config --add channels https://conda.anaconda.org/conda-forge
		$ conda config --add channels https://conda.anaconda.org/domdfcoding

	* Then install

	.. code-block:: bash

		$ conda install chemistry_tools

.. end installation


lookup and pubchem adapted from PubChemPy
=========================================
Python interface to the PubChem REST API

|

Copyright 2017 Matt Swain <m.swain@me.com>

https://github.com/mcs07/PubChemPy

Available under the MIT License


SpectrumSimilarity
======================================
Perform mass spectrum similarity calculations

|

Adapted from SpectrumSimilarity.R

Part of OrgMassSpecR

Copyright 2011-2017 Nathan Dodder <nathand@sccwrp.org>

https://cran.r-project.org/web/packages/OrgMassSpecR/index.html

Available under the BSD 2-Clause License


elements and formulae
=========================

Provides properties for the elements in the periodic table, and functions
for parsing formulae and calculating isotope distributions.

Calculations are based on the isotopic composition of the elements. Mass
deficiency due to chemical bonding is not taken into account.

Examples of valid formulae are ``H2O``, ``[2H]2O``, ``CH3COOH``, ``EtOH``,
``CuSO4.5H2O``, and ``(COOH)2``. Formulae are case sensitive.

|

Based on ChemPy (https://github.com/bjodah/chempy)

Copyright (c) 2015-2018, Björn Dahlgren

All rights reserved.

|

Also based on molmass (https://github.com/cgohlke/molmass)

Copyright (c) 1990-2020, Christoph Gohlke

All rights reserved.

Licensed under the BSD 3-Clause License

|

Also based on Pyteomics (https://github.com/levitsky/pyteomics)

Copyright (c) 2011-2015, Anton Goloborodko & Lev Levitsky

Licensed under the Apache License
