class Person:
    """
    Class representing a person.
    """
    def __init__(self, name, living_years, sex, children=None, mother=None, father=None, partner=None):
        """
        Initialization of person.
        :param name: string
        :param living_years: tuple wih 2 integers
        :param sex: "f" or "m"
        :param children: list of Persons
        :param mother: Persons with "f" sex
        :param father: Persons with "m" sex
        :param partner: Person with opposite sex
        """
        self.name = name
        self.birth_year = living_years[0]
        self.death_year = living_years[1]
        self.sex = sex
        self.mother = mother
        self.father = father
        self.partner = partner
        self.children = children

    def __str__(self):
        """
        Returns string representation of Person.
        :return: str
        """
        pass

    def get_name(self):
        """
        Returns name of Person.
        :return: str
        """
        pass

    def get_sex(self):
        """
        Returns sex of Person.
        :return: str
        """
        pass

    def get_birth_year(self):
        """
        Returns Person's birth year.
        :return: int
        """
        pass

    def get_death_year(self):
        """
        Returns Person's death year.
        :return: int
        """
        pass

    def get_mother(self):
        """
        Returns Person's mother.
        :return: Person or None
        """
        pass

    def get_father(self):
        """
        Returns Person's father.
        :return: Person or None
        """
        pass

    def get_partner(self):
        """
        Returns Person's partner.
        :return: Person or None
        """
        pass

    def get_children(self):
        """
        Returns list of Person's children.
        :return: list of Persons or None
        """
        pass
