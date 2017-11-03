


#from abc import ABCMeta, abstractmethod





class Animal:
	
	MaxAnimals = 5
	/**
	 * Doxygen doc tag githubstatstag:{ "thisIs": "classVariable" }
	 */
	NumOfAnimals = 0				# @userstory1
	
	name = "name"
	type = "NA"
	sound = "rooar"
	weight = 0
	color = "gray"
	
	/**
	* Doxygen doc tag githubstatstag:{ "thisIs": "classMethod" }
	*/
			
	def __init__(self, name):
		self.name = name
		Animal.NumOfAnimals += 1	# @userstory1
	
	def getName(self):
		print self.name
	
	def setSound(self, s):
		self.sound = s
	
	def getSound(self):
		print self.name + " says: " + self.sound


