from person import Person
from family_tree import FamilyTree

person1 = Person("Anna", (2000, 2021), "f", None, None, None, None)
tree = FamilyTree(person1)
person2 = Person("Maria", (1970, 2014), "f", None, None, None, None)
tree.add_mother(person1, person2)
print(tree.mother(person1))  # expected: Anna(2000-2021)
print(tree.num_children(person2))  # expected: 1
print(tree.children(person2))  # expected: [Anna(2000-2021)]
person3 = Person("Vlad", (1973, 2018), "m", None, None, None, None)
tree.add_father(person1, person3)
print(tree.father(person1))  # expected: Anna(2000-2021)
print(tree.num_children(person3))  # expected: 1
print(tree.children(person3))  # expected: [Anna(2000-2021)]
print(tree.partner(person3))  # expected: Maria(1970-2014)
print(tree.partner(person2))  # expected: Vlad(1973-2018)
