# Homework
## Theme: Building a family tree of royal dynasties
### Description
Goal of this project is to analyze dynastic marriages of royal families, and crate a graph, which shows them.
Also program should show, whether marriage between two persons is possible. 
### Input
Name of person, written with spaces or underscores between words, who's information can be found in Wikipedia.
### Output
Family tree of that person.
### Input
Names of  two persons, who's marriage needs to be checked.
### Output
Whether the marriage is possible and if not, than reason for it.
## Program structure
### data
Contains fails with male and female names.
### docs
Contains results of Homeworks and documentation as html page.
### examples
#### API_example.py
Contains example of Wikipedia API usage.
#### json_parse
Contains example of working with json file from Wikipedia.
### modules
#### person.py
Contains class Person, to represent an element in Vertex.
#### family_graph.py
Contains class FamilyGraph to represent a family tree.
Inside class FamilyGraph contains: class Vertex, class Edge.
Class Edge contains class RelationType, which represents different relationships between vertices.
#### get_data.py
Contains functions to get data from Wikipedia and parse it to find needed information.
#### get_names.py
Contains function to get male and female names from files.
#### main.py
Contains main function, class Menu to work with user and function to extend graph.
### tests
#### test_adt.py
Contains testing of work classes Person and FamilyGraph.
## Example of work
````
Choose:
1 : print family, 2 : check marriage, 3 : exit
>1
Enter name(use space or underscores between words):Henry_VIII_of_England
{   '1. Name:': 'Henry VIII of England(1491-1547)',
    '2. Partners:': [   'Catherine of Aragon(1485-1536)',
                        'Elizabeth Blount(1498-8201)',
                        'Anne Boleyn(1501-1536)',
                        'Jane Seymour(1508-1537)'],
    '3. Children:': [   {   '1. Name:': 'Henry,_Duke_of_Cornwall(1511-1511)',
                            '2. Partners:': [],
                            '3. Children:': []},
                        {   '1. Name:': 'Mary_I_of_England(1516-1558)',
                            '2. Partners:': [],
                            '3. Children:': []},
                        {   '1. Name:': 'Henry_FitzRoy,_Duke_of_Richmond_and_Somerset(1519-1536)',
                            '2. Partners:': [],
                            '3. Children:': []},
                        {   '1. Name:': 'Elizabeth_I_of_England(1533-1603)',
                            '2. Partners:': [],
                            '3. Children:': []},
                        {   '1. Name:': 'Edward_VI_of_England(1537-1553)',
                            '2. Partners:': [],
                            '3. Children:': []}]}
Choose:
1 : print family, 2 : check marriage, 3 : exit
>2
Enter name(use space or underscores between words):Henry_VIII_of_England
Enter name(use space or underscores between words):Mary_I_of_England
Marriage is impossible. They are relatives.
Choose:
1 : print family, 2 : check marriage, 3 : exit
>3
```