def read_names():
    """
    Reads male and female names from file and returns them in dictionary.
    :return: dict
    """
    names = {"male": [], "female": []}
    with open("../data/female-first-names.txt") as file:
        data = file.readlines()
        for line in data:
            name = line.strip().lower()
            names["female"].append(name)
    with open("../data/male-first-names.txt") as file:
        data = file.readlines()
        for line in data:
            name = line.strip().lower()
            names["male"].append(name)
    return names
