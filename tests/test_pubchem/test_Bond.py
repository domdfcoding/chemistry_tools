"""
test_Bond
~~~~~~~~~~~~~

Test Bond class

"""

# 3rd party
import pytest

# this package
from chemistry_tools.pubchem.bond import Bond, BondType


@pytest.fixture(scope="module")
def b1() -> Bond:
	return Bond(1, 2, order=BondType.QUADRUPLE)


def test_bond(b1: Bond):
	assert b1.__repr__() == "Bond(1, 2, <BondType.QUADRUPLE: 4>)"
	assert isinstance(b1.to_dict(), dict)
	assert b1.to_dict()["order"] == BondType.QUADRUPLE
