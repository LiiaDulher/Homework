class Person:
    """
    Class representing a person.
    """
    def __init__(self, name, living_years, sex):
        """
        Initialization of person.
        :param name: string
        :param living_years: tuple wih 2 strings
        :param sex: "f" or "m"
        """
        self.name = name
        self.birth_year = living_years[0]
        self.death_year = living_years[1]
        self.sex = sex

    def __str__(self):
        """
        Returns string representation of Person.
        :return: str
        """
        return self.name + "(" + str(self.birth_year) + "-" + str(self.death_year) + ")"

    def __repr__(self):
        """
        Returns string representation of Person.
        :return: str
        """
        return self.name + "(" + str(self.birth_year) + "-" + str(self.death_year) + ")"

    def __eq__(self, other):
        """
        Returns True if self equals other.
        :param other: Person
        :return: bool
        """
        return self.name == other.name

    def __ne__(self, other):
        """
        Returns True if self not equals other.
        :param other: Person
        :return: bool
        """
        return not self == other

    def get_name(self):
        """
        Returns name of Person.
        :return: str
        """
        return self.name

    def get_sex(self):
        """
        Returns sex of Person.
        :return: str
        """
        return self.sex

    def get_birth_year(self):
        """
        Returns Person's birth year.
        :return: str
        """
        return self.birth_year

    def get_death_year(self):
        """
        Returns Person's death year.
        :return: str
        """
        return self.death_year

    def convert_to_dict(self):
        """
        Converts Person to dictionary
        :return: dict
        """
        return {"1. name": self.name,
                "2. living_years": (self.birth_year, self.death_year),
                "3. sex": self.sex}

