import pytest


def test_Dog(capfd):
	from aSimple import Dog

	tmpDog = Dog('name')
	tmpDog.getSound()
	out, err = capfd.readouterr()
	assert out == "name says: bark"




