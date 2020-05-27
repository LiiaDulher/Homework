import sys
sys.path.insert(1, '../modules')
from person import Person
from family_graph import FamilyGraph

person1 = Person("Maria", (1970, 2014), "f")
person2 = Person("Anna", (2000, 2021), "f")
person3 = Person("Vlad", (1973, 2018), "m")
graph = FamilyGraph()
v_1 = graph.insert_vertex(person1)
v_2 = graph.insert_vertex(person2)
v_3 = graph.insert_vertex(person3)
graph.insert_edge(v_1, v_2, "child")
graph.insert_edge(v_3, v_2, "child")
graph.insert_edge(v_1, v_3, "husband")
print(graph.vertices())
print(graph.edges())
print(graph.adjacent_vertices(v_1))
print(graph.adjacent_vertices(v_1, "child"))
