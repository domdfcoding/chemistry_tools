#  This file is managed by 'repo_helper'. Don't edit it directly.

__all__ = ["extras_require"]

extras_require = {
		"pubchem": [
				"cawdrey>=0.5.0",
				"mathematical>=0.5.1",
				"pillow>=9.0.0",
				'pillow<=10.2.0; platform_python_implementation == "PyPy" and python_version < "3.9" and platform_system == "Windows"',
				"pyparsing>=2.4.6",
				"tabulate>=0.8.9"
				],
		"formulae": ["cawdrey>=0.5.0", "mathematical>=0.5.1", "pyparsing>=2.4.6", "tabulate>=0.8.9"],
		"plotting": ["matplotlib>=3.6.0"],
		"toxnet": ["beautifulsoup4>=4.7.0"],
		"all": [
				"beautifulsoup4>=4.7.0",
				"cawdrey>=0.5.0",
				"mathematical>=0.5.1",
				"matplotlib>=3.6.0",
				"pillow>=9.0.0",
				'pillow<=10.2.0; platform_python_implementation == "PyPy" and python_version < "3.9" and platform_system == "Windows"',
				"pyparsing>=2.4.6",
				"tabulate>=0.8.9"
				]
		}
