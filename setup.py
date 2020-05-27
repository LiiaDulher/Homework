from distutils.core import setup
setup(name="spam",
      version="1.0",
      scripts='main.py',
      pymodules=['family_graph.py', 'get_data.py', 'get_names.py', 'main.py', 'person.py'],
      data_files=[('data', ['data/male_first_names.txt', 'data/female_first_names.txt'])])
