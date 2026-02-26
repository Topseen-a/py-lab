class Dog:
    def __init__(self, name, height = 5):
        self.name = name
        self.height = height

    def __eq__(self, dog):
        return self.name == dog.name

    def __ge__(self, dog):
        return self.height >= dog.height

    def __iter__(self):
        return iter([self.name])

my_dog = Dog("Nelson", 2)
street_dog = Dog("Jack")

print(my_dog == street_dog)
print(my_dog >= street_dog)
print("Jack" == "Nelson")
print(type(my_dog) == type(street_dog))

print("musa".__add__("3"))
print(dir(int))
