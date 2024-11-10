class parrot:
    species = 'bird'
    def __init__(self, name, age):
        self.name = name
        self.age = age

ob = parrot('alexa', 3)
ob1 = parrot('bob', 5)
print('the species of the parrot is', ob.species)
print('the name of the parrot is', ob.name)
print('the age of the parrot is', ob.age)

print('the name of the other parrot is', ob1.name)
print('the age of the other parrot is', ob1.age)