import pytest

from app import calculer_total


def test_un_cafe():
    assert calculer_total(1) == 12


def test_deux_cafes():
    assert calculer_total(2) == 24


def test_dix_cafes():
    assert calculer_total(10) == 120


def test_zero_refuse():
    with pytest.raises(ValueError):
        calculer_total(0)


def test_onze_refuse():
    with pytest.raises(ValueError):
        calculer_total(11)
