"""
test_download
~~~~~~~~~~~~~

Test downloading.

"""

# stdlib
import csv

# 3rd party
import pytest
from domdf_python_tools.paths import PathPlus

# this package
from chemistry_tools.pubchem.images import get_structure_image
from chemistry_tools.pubchem.properties import rest_get_properties


def test_image_download(tmp_pathplus: PathPlus):
	img = get_structure_image("Asprin")
	img.save(tmp_pathplus / "aspirin.png")


@pytest.mark.usefixtures("pubchem_cassette")
def test_csv_download(tmp_pathplus: PathPlus):
	csv_content = rest_get_properties(
			[1, 2, 3],
			namespace="cid",
			properties="CanonicalSMILES,IsomericSMILES",
			format_="csv",
			)
	(tmp_pathplus / "s.csv").write_text(csv_content)

	with (tmp_pathplus / "s.csv").open() as f:
		rows = list(csv.reader(f))
		assert rows[0] == ["CID", "CanonicalSMILES", "IsomericSMILES"]
		assert rows[1][0] == '1'
		assert rows[2][0] == '2'
		assert rows[3][0] == '3'
