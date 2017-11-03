




class Animal:
	
	MaxAnimals = 5
	NumOfAnimals = 0				# @userstory1
	
	name = "name"
	type = "NA"
	sound = "rooar"
	weight = 0
	color = "gray"
			
	def __init__(self, name):
		self.name = name
		Animal.NumOfAnimals += 1	# @userstory1
	
	def getName(self):
		print self.name
	
	def setSound(self, s):
		self.sound = s
	
	def getSound(self):
		print self.name + " says: " + self.sound


class Dog(Animal):

	def __init__(self, name):
		self.name = name
		self.setSound("bark")


class Cat(Animal):

	def __init__(self, name):
		self.name = name
		self.setSound("meeow")








if __name__ == '__main__':
	print "Hello World!" 
	dogName = raw_input("\nWhat is your dog's name?" ) 
	

	if dogName:
		Fido = Dog(dogName)
		Fido.getSound()
	
	Fluffy = Cat("Fluffy")
	Fluffy.getSound()



