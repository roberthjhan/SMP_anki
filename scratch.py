

class Zoo:
    def __init__(self):
        self.animals = []


    def __add__(self, other):
        self.animals.append(other)

    def __repr__(self):
        ret = ""
        for animal in self.animals:
            ret += animal
            ret += "\n"

        return ret
class Animal:
    def __init__(self, type):
        self.type = type

    def __repr__(self):
        return str(self.type)

zoooo = Zoo()
animals = ["dog","zebra", "elephant"]
for animal in animals:
    print(animal)
    zoooo.animals += animal
print(zoooo)




