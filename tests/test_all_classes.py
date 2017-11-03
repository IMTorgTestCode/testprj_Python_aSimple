import pytest


def test_Dog(capfd):
	from aSimple import aSimple

	tmpDog = aSimple.Dog('name')
	tmpDog.getSound()
	out, err = capfd.readouterr()
	assert out == "name says: bark\n"

def test_Cat(capfd):
	from aSimple import aSimple

	tmpCat = aSimple.Cat('name')
	tmpCat.getSound()
	out, err = capfd.readouterr()
	assert out == "name says: meeow\n"



