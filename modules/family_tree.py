class FamilyTree:
    """
    Class representing family tree.
    """
    def __init__(self, root):
        """
        Initialization of tree based on main person.
        :param root: Person
        """
        pass

    def draw(self):
        """
        Drawing a tree.
        :return: None
        """
        pass

    def add_child(self, person, child):
        """
        Add a child to given person.
        :param person: Person
        :param child: Person
        :return: None
        """
        pass

    def add_mother(self, person, mother):
        """
        Add a mother to given person.
        :param person: Person
        :param mother: Person
        :return: None
        """
        pass

    def add_father(self, person, father):
        """
        Add a father to given person.
        :param person: Person
        :param father: Person
        :return: None
        """
        pass

    def add_partner(self, person):
        """
        Add a child to given person.
        :param person: Person
        :return: None
        """
        pass

    def check_marriage(self, man, woman):
        """
        Checks if marriage between man and woman is possible.
        :param man: Person
        :param woman: Person
        :return: bool
        """
        pass

    def root(self, person):
        """
        Checks if given person is a root.
        :param person: Person
        :return: bool
        """
        pass

    def num_children(self, person):
        """
        Returns number of person's children.
        :param person: Person
        :return: int
        """
        pass

    def children(self, person):
        """
        Returns person's children.
        :param person: Person
        :return: list of Persons
        """
        pass

    def mother(self, person):
        """
        Returns person's mother.
        :param person: Person
        :return: Person
        """
        pass

    def father(self, person):
        """
        Returns person's father.
        :param person: Person
        :return: Person
        """
        pass

    def partner(self, person):
        """
        Returns person's partner.
        :param person: Person
        :return: Person
        """
        pass
