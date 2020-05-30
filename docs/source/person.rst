person module
=============

.. automodule:: person
   :members:
   :undoc-members:
   :show-inheritance:

    :class: Person
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
    def __str__(self):
        """
        Returns string representation of Person.
        :return: str
        """
    def __repr__(self):
        """
        Returns string representation of Person.
        :return: str
        """
    def __eq__(self, other):
        """
        Returns True if self equals other.
        :param other: Person
        :return: bool
        """
    def __ne__(self, other):
        """
        Returns True if self not equals other.
        :param other: Person
        :return: bool
        """
    def get_name(self):
        """
        Returns name of Person.
        :return: str
        """
    def get_sex(self):
        """
        Returns sex of Person.
        :return: str
        """
    def get_birth_year(self):
        """
        Returns Person's birth year.
        :return: str
        """
    def get_death_year(self):
        """
        Returns Person's death year.
        :return: str
        """
    def convert_to_dict(self):
        """
        Converts Person to dictionary
        :return: dict
        """