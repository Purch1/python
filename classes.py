# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x}, {self.y})"

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# point = Point(1, 2)
# print(str(point))


# Making Custom Containers
# class TagCloud:
#     def __init__(self):
#         self.tags = {}

#     def add(self, tag):
#         self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1


# cloud = TagCloud()
# cloud.add("Python")
# cloud.add("python")
# cloud.add("python")
# print(cloud.tags)

# Inheritance
class Animal:
    def __init__(self):
        self.age = 1
        
    def eat(self):
        print("eat")

class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")

m = Mammal()
print(isinstance(m, object))
o = object()
o.
