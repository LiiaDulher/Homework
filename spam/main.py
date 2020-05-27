from get_data import get_information
from family_graph import FamilyGraph
from person import Person
from get_names import read_names
import pprint


class Menu:
    """
    Class to get only certain choices.
    """
    def __init__(self, lst):
        self.options = {str(x): lst[x-1] for x in range(1, len(lst)+1)}

    def get_str_repr(self):
        """
        Creates string with all possible choices.
        :return: str
        """
        result = []
        for key in self.options.keys():
            if self.options[key] is not None:
                result.append('{} : {}'.format(key, self.options[key]))
        return ', '.join(result)

    def __str__(self):
        return self.get_str_repr()

    def get_selection(self):
        """
        Gets user's selection.
        :return: str
        """
        print("Choose:")
        print(self.get_str_repr())
        choice = self.read()
        if choice in self.options.keys() and self.options[choice] is not None:
            return self.options[choice]
        else:
            print("Impossible choice")
            return self.get_selection()

    def read(self):
        """
        Reads user's choice.
        :return: str
        """
        return input('>')


def get_name():
    """
    Get name from user.
    :return: str
    """
    def check_name(name):
        """
        Return True if name is entered correctly.
        """
        name = "_".join(name.split(" "))
        try:
            get_information(name)
        except KeyError:
            return False
        return True
    name = input("Enter name(use space or underscores between words):")
    while not check_name(name):
        print("Wrong name.")
        name = input("Enter name(use space or underscores between words):")
    return name


names = read_names()


def get_sex(name):
    """
    Returns sex of person with given name.
    :param name: str
    :return: str
    """
    first_name = name.split("_")[0].split("-")[0]
    if first_name.lower() in names["male"]:
        sex = "m"
    else:
        sex = "f"
    return sex


def extend_graph(graph, v_name, i, end, reverse=False):
    """
    Extends graph with needed data from given vertex.
    :param graph: FamilyGraph
    :param v_name: Vertex
    :param i: int
    :param end: int
    :param reverse: bool
    :return: None
    """
    if i == end:
        return graph
    name = v_name.element().get_name()
    name = "_".join(name.split(" "))
    data = get_information(name)
    if reverse:
        if data["father"] is None and data["mother"] is None:
            return graph
        if data["mother"] is not None:
            mother_data = get_information(data["mother"])
            mother = Person(data["mother"], (mother_data["born"], mother_data["died"]), "f")
            v_mother = graph.insert_vertex(mother)
            graph.insert_edge(v_mother, v_name, "child")
            extend_graph(graph, v_mother, i + 1, end, reverse=True)
        if data["father"] is not None:
            father_data = get_information(data["father"])
            father = Person(data["father"], (father_data["born"], father_data["died"]), "m")
            v_father = graph.insert_vertex(father)
            graph.insert_edge(v_father, v_name, "child")
            extend_graph(graph, v_father, i + 1, end, reverse=True)
        if data["mother"] is not None and data["father"] is not None:
            graph.insert_edge(v_father, v_mother, "wife")
    else:
        children = []
        for child_name in data["children_names"]:
            name = "_".join(child_name.split(" "))
            child_result = get_information(name)
            sex = get_sex(name)
            child = Person(name, (child_result["born"], child_result["died"]), sex)
            v_child = graph.insert_vertex(child)
            children.append(v_child)
            graph.insert_edge(v_name, v_child, "child")
            if v_name.element().get_sex() == "m":
                mother_data = get_information(child_result["mother"])
                mother = Person(child_result["mother"], (mother_data["born"], mother_data["died"]), "f")
                v_mother = graph.insert_vertex(mother)
                graph.insert_edge(v_mother, v_child, "child")
                try:
                    graph.insert_edge(v_mother, v_name, "husband")
                except ValueError:
                    pass
            else:
                father_data = get_information(child_result["father"])
                father = Person(child_result["father"], (father_data["born"], father_data["died"]), "m")
                v_father = graph.insert_vertex(father)
                graph.insert_edge(v_father, v_child, "child")
                try:
                    graph.insert_edge(v_father, v_name, "wife")
                except ValueError:
                    pass
        if not children:
            return graph
        for v_child in children:
            extend_graph(graph, v_child, i+1, end, reverse=False)


def main():
    """
    Main function.
    :return: None
    """
    menu = Menu(["print family", "check marriage", "exit"])
    while True:
        command = menu.get_selection()
        if command == "exit":
            break
        elif command == "print family":
            name = get_name()
            name = "_".join(name.split(" "))
            data = get_information(name)
            sex = get_sex(name)
            graph = FamilyGraph()
            person = Person(data["name"], (data["born"], data["died"]), sex)
            v_name = graph.insert_vertex(person)
            extend_graph(graph, v_name, 0, 7)  # TODO: draw graph
            pprint.pprint(graph.draw(v_name), indent=4)
        else:
            name1 = get_name()
            name2 = get_name()
            name1 = "_".join(name1.split(" "))
            data1 = get_information(name1)
            name2 = "_".join(name2.split(" "))
            data2 = get_information(name2)
            sex1 = get_sex(name1)
            sex2 = get_sex(name2)
            if sex1 == sex2:
                print("Marriage is impossible. Similar sex.")
            else:
                born1 = data1["born"]
                born2 = data2["born"]
                died1 = data1["died"]
                if died1 == "present":
                    died1 = int(born1) + 150
                died2 = data2["died"]
                if died2 == "present":
                    died2 = int(born2) + 150
                if int(born1) < int(born2) and (int(born2) + 15) < int(died1) and (int(born2) + 15) < int(died1):
                    graph1 = FamilyGraph()
                    graph2 = FamilyGraph()
                    person1 = Person(data1["name"], (born1, died1), sex1)
                    person2 = Person(data2["name"], (born2, died2), sex2)
                    v_name1 = graph1.insert_vertex(person1)
                    v_name2 = graph2.insert_vertex(person2)
                    extend_graph(graph1, v_name1, 0, 5, reverse=True)
                    extend_graph(graph2, v_name2, 0, 5, reverse=True)
                    if graph1.graph_intersection(graph2):
                        print("Marriage is impossible. They are relatives.")
                    else:
                        print("Marriage is possible.")
                elif int(born2) < int(born1) and (int(born1) + 15) < int(died2) and (int(born1) + 15) < int(died2):
                    graph1 = FamilyGraph()
                    graph2 = FamilyGraph()
                    person1 = Person(data1["name"], (born1, died1), sex1)
                    person2 = Person(data2["name"], (born2, died2), sex2)
                    v_name1 = graph1.insert_vertex(person1)
                    v_name2 = graph2.insert_vertex(person2)
                    extend_graph(graph1, v_name1, 0, 5, reverse=True)
                    extend_graph(graph2, v_name2, 0, 5, reverse=True)
                    if graph1.graph_intersection(graph2):
                        print("Marriage is impossible. They are relatives.")
                    else:
                        print("Marriage is possible.")
                else:
                    print("Marriage is impossible. Wrong age.")


if __name__ == "__main__":
    main()
