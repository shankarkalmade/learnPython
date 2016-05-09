''' sample class and subclass '''
class pet(object):

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)


'''Testing pet class'''

pet = pet("dog", "aaa")
print pet.__str__()



class Dog(pet):

    def __init__(self, name, chases_cats):
        pet.__init__(self, name, "Dog")
        self.chases_cats = chases_cats

    def chasesCats(self):
        return self.chases_cats

    def __str__(self):
        print 'The Dog named %s, chases Cats: %s' % (self.name, self.chases_cats)

"""Testing Pet and Dog

pet = pet("tommy", "Dog")
dog1 = Dog("Sheru", True)

"""

class Cat(pet):

    def __init__(self, name, hates_dogs):
        pet.__init__(self, name, "Cat")
        self.hates_dogs = hates_dogs

    def hatesDogs(self):
        return self.hates_dogs

    def __str__(self):
        print 'The Cat named %s, hates Dog: %s' % (self.name, self.hates_dogs)


mittens = Cat("Mittens", True)
print mittens



