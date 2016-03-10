



import Animal, Dog, Cat		






if __name__ == '__main__':
	print "Hello World!" 
	dogName = raw_input("\nWhat is your dog's name?" ) 
	

	if dogName:
		Fido = Dog.Dog(dogName)
		Fido.getSound()
	
	Fluffy = Cat.Cat("Fluffy")
	Fluffy.getSound()




