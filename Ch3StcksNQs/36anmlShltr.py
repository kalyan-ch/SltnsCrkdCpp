#animal shelter system that helps choose oldest animal enrolled

from Queue import Queue

class Animal(object):
	def __init__(self, name, order):
		self.name = name
		self.order = order


class Dog(Animal):	
	def __init__(self, name, order):
		Animal.__init__(self,name,order)		


class Cat(Animal):	
	def __init__(self, name, order):
		Animal.__init__(self,name,order)
		


class AnimalQueue(object):
		
	def __init__(self):
		self.dogs = Queue()
		self.cats = Queue()


	def adoptDog(self):
		return self.dogs.pop()

	def adoptCat(self):
		return self.cats.pop()

	def adoptAny(self):

		if self.dogs.peek().order < self.cats.peek().order:
			return self.dogs.pop()
		else:
			return self.cats.pop()

	def enQueAnimals(self, a):
		if (type(a) == Dog):
			self.dogs.push(a)
		if (type(a) == Cat):
			self.cats.push(a)


		
if __name__ == '__main__':
	
	an = AnimalQueue()

	an.enQueAnimals(Dog("Scooby",1))
	an.enQueAnimals(Cat("Thomas",2))
	an.enQueAnimals(Cat("Marge",3))
	an.enQueAnimals(Dog("Kakarot",4))
	an.enQueAnimals(Cat("Clark",5))
	an.enQueAnimals(Cat("Jeremy",6))

	print an.adoptAny().name
	print an.adoptAny().name
