class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return self.sound


class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "Moo")

    def produce_milk(self):
        return f"{self.name} produces milk."


class Chicken(Animal):
    def __init__(self, name):
        super().__init__(name, "Cluck")

    def lay_eggs(self):
        return f"{self.name} laid an egg."


class Horse(Animal):
    def __init__(self, name):
        super().__init__(name, "Neigh")

    def gallop(self):
        return f"{self.name} is galloping."


class Field:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)


class Barn:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)


if __name__ == "__main__":

    cow = Cow("Bessie")
    chicken = Chicken("Chicken")
    horse = Horse("Horsie")

    field = Field()
    barn = Barn()

    field.add_animal(cow)
    field.add_animal(chicken)
    barn.add_animal(horse)

    field.remove_animal(cow)
    barn.add_animal(cow)

    print("Animals in the field:")
    for animal in field.animals:
        print(f"{animal.name} says {animal.make_sound()}")

    print("\nAnimals in the barn:")
    for animal in barn.animals:
        print(f"{animal.name} says {animal.make_sound()}")


input('Press ENTER to exit')