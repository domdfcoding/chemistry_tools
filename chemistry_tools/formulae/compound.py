#!/usr/bin/env python3
#
#  compound.py
"""
Parse formulae into a Python object
"""
#
#  Copyright (c) 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#  Based on ChemPy (https://github.com/bjodah/chempy)
#  |  Copyright (c) 2015-2018, Björn Dahlgren
#  |  All rights reserved.
#  |
#  |  Redistribution and use in source and binary forms, with or without modification,
#  |  are permitted provided that the following conditions are met:
#  |
#  |    Redistributions of source code must retain the above copyright notice, this
#  |    list of conditions and the following disclaimer.
#  |
#  |    Redistributions in binary form must reproduce the above copyright notice, this
#  |    list of conditions and the following disclaimer in the documentation and/or
#  |    other materials provided with the distribution.
#  |
#  |  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#  |  ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#  |  WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  |  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
#  |  ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#  |  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#  |  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
#  |  ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  |  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  |  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#  Also based on Pyteomics (https://github.com/levitsky/pyteomics)
#  |  Copyright (c) 2011-2015, Anton Goloborodko & Lev Levitsky
#  |  Licensed under the Apache License, Version 2.0 (the "License");
#  |  you may not use this file except in compliance with the License.
#  |  You may obtain a copy of the License at
#  |
#  |    http://www.apache.org/licenses/LICENSE-2.0
#  |
#  |  Unless required by applicable law or agreed to in writing, software
#  |  distributed under the License is distributed on an "AS IS" BASIS,
#  |  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  |  See the License for the specific language governing permissions and
#  |  limitations under the License.
#  |
#  |  See also:
#  |  Goloborodko, A.A.; Levitsky, L.I.; Ivanov, M.V.; and Gorshkov, M.V. (2013)
#  |  "Pyteomics - a Python Framework for Exploratory Data Analysis and Rapid Software
#  |  Prototyping in Proteomics", Journal of The American Society for Mass Spectrometry,
#  |  24(2), 301–304. DOI: `10.1007/s13361-012-0516-6 <http://dx.doi.org/10.1007/s13361-012-0516-6>`_
#  |
#  |  Levitsky, L.I.; Klein, J.; Ivanov, M.V.; and Gorshkov, M.V. (2018)
#  |  "Pyteomics 4.0: five years of development of a Python proteomics framework",
#  |  Journal of Proteome Research.
#  |  DOI: `10.1021/acs.jproteome.8b00717 <http://dx.doi.org/10.1021/acs.jproteome.8b00717>`_
#


# this package
import quantities
from domdf_python_tools.bases import Dictable

from chemistry_tools.formulae.formula import Formula
from chemistry_tools.formulae.html import string_to_html
from chemistry_tools.formulae.latex import string_to_latex
from chemistry_tools.formulae.unicode import string_to_unicode


class Compound(Dictable):
	"""
	Class representing a chemical compound.
	
	Parameters
	----------
	name : str
	latex_name : str
	unicode_name : str
	html_name : str
	formula: Formula
		The chemical formula of the compound. If none this is generated from the name
	data : dict
		Free form dictionary. Could be simple such as ``{'mp': 0, 'bp': 100}``
		or considerably more involved, e.g.: ``{'diffusion_coefficient': {\
		'water': lambda T: 2.1*m**2/s/K*(T - 273.15*K)}}``.

	Attributes
	----------
	mass
		The mass of the compound
	formula:
		The :class:`Formula` object representing the compound
	data
		Free form dictionary of additional properties.
	"""
	
	def __init__(
			self, name, formula=None, data=None,
			latex_name=None, unicode_name=None, html_name=None,
			):
		
		super().__init__()
		
		self.name = name
		
		if formula is None:
			formula = name
			self.formula = Formula.from_string(formula)
		else:
			self.formula = formula
		
		if latex_name:
			self.latex_name = latex_name
		else:
			self.latex_name = string_to_latex(self.formula.hill_formula)
			
		if unicode_name:
			self.unicode_name = unicode_name
		else:
			self.unicode_name = string_to_unicode(self.formula.hill_formula)
			
		if html_name:
			self.html_name = html_name
		else:
			self.html_name = string_to_html(self.formula.hill_formula)
		
		self.data = data or {}
	
	def __dict__(self):
		return dict(
				name=self.name,
				latex_name=self.latex_name,
				unicode_name=self.unicode_name,
				html_name=self.html_name,
				formula=self.formula,
				data=self.data,
				)
	
	def __eq__(self, other):
		if isinstance(other, str):
			return self.name == other
		else:
			super().__eq__(other)
	
	@property
	def charge(self):
		"""
		Convenience property for accessing charge of the formula
		"""
		
		return self.formula.charge
	
	@property
	def mass(self):
		"""
		Convenience property for accessing the mass of the formula
		"""
		
		return self.formula.mass
	
	def molar_mass(self):
		"""
		Returns the molar mass (with units) of the substance

		Examples
		--------
		>>> nh4p = Compound.from_formula('NH4+')
		>>> from chemistry_tools.units import quantities
		>>> nh4p.molar_mass(quantities)
		array(18.0384511...) * g/mol

		"""
		
		return self.mass * quantities.g / quantities.mol
	
	def __repr__(self):
		return f"<{self.__class__.__name__}({self.name}, {self.formula})>"
	
	def __str__(self):
		return str(self.name)
	
	def _repr_html_(self):
		return self.html_name
