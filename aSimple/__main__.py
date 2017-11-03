from aSimple import *
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('name')


def main():
	user = parser.parse_args()

	print "Hello, {0.name}!".format(user) 
	dogName = raw_input("\nWhat is your dog's name?" ) 
	

	if dogName:
		Fido = Dog(dogName)
		Fido.getSound()
	
	Fluffy = Cat("Fluffy")
	Fluffy.getSound()


if __name__ == '__main__':
	main()
