class FamilyGraph:
    """Representation of a family graph using an adjacency map."""

    class Vertex:
        """Lightweight vertex structure for a graph."""
        __slots__ = '_element'

        def __init__(self, person):
            """Do not call constructor directly. Use Graph's insert_vertex(x)."""
            self._element = person

        def element(self):
            """Return element associated with this vertex."""
            return self._element

        def __hash__(self):  # will allow vertex to be a map/set key
            return hash(id(self))

        def __str__(self):
            return str(self._element)

        def __repr__(self):
            return str(self._element)

        def __eq__(self, other):
            return str(self) == str(other)

    class Edge:
        """Lightweight edge structure for a graph."""
        __slots__ = '_origin', '_destination', '_type'

        class RelationType:
            """
            Class represents different relations between vertices.
            """
            def __init__(self, type):
                self.type = type

            def __eq__(self, other):
                return self.type == other.type

            def __str__(self):
                return self.type

            def __repr__(self):
                return self.type

            def __invert__(self):
                if self.type == "parent":
                    return FamilyGraph.Edge.RelationType("child")
                elif self.type == "child":
                    return FamilyGraph.Edge.RelationType("parent")
                elif self.type == "wife":
                    return FamilyGraph.Edge.RelationType("husband")
                elif self.type == "husband":
                    return FamilyGraph.Edge.RelationType("wife")
                return self

        def __init__(self, u, v, type):
            """Do not call constructor directly. Use Graph's insert_edge(u,v,x)."""
            self._origin = u
            self._destination = v
            self._type = type

        def endpoints(self):
            """Return (u,v) tuple for vertices u and v."""
            return self._origin, self._destination

        def opposite(self, v):
            """Return the vertex that is opposite v on this edge."""
            if not isinstance(v, FamilyGraph.Vertex):
                raise TypeError('v must be a Vertex')
            return self._destination if v is self._origin else self._origin
            # raise ValueError('v not incident to edge')

        def type(self):
            """Return element associated with this edge."""
            return self._type

        def __hash__(self):  # will allow edge to be a map/set key
            return hash((self._origin, self._destination))

        def __str__(self):
            return '({0},{1},{2})'.format(self._origin, self._destination, self._type)

        def __repr__(self):
            return '({0},{1},{2})'.format(self._origin, self._destination, self._type)

    # ------------------------- Graph methods -------------------------
    def __init__(self):
        """Create an empty directed graph.
        """
        self._outgoing = {}
        self._incoming = {}

    def _validate_vertex(self, v):
        """Verify that v is a Vertex of this graph."""
        if not isinstance(v, self.Vertex):
            raise TypeError('Vertex expected')
        if v not in self._outgoing:
            raise ValueError('Vertex does not belong to this graph.')

    def vertex_count(self):
        """Return the number of vertices in the graph."""
        return len(self._outgoing)

    def vertices(self):
        """Return an iteration of all vertices of the graph."""
        return list(self._outgoing.keys())

    def edge_count(self):
        """Return the number of edges in the graph."""
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total

    def edges(self):
        """Return a set of all edges of the graph."""
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())  # add edges to resulting set
        return result

    def get_edge(self, u, v):
        """Return the edge from u to v, or None if not adjacent."""
        self._validate_vertex(u)
        self._validate_vertex(v)
        return self._outgoing[u].get(v)  # returns None if v not adjacent

    def degree(self, v):
        """Return number of outgoing edges incident to vertex v in the graph.
        """
        self._validate_vertex(v)
        adj = self._outgoing
        return len(adj[v])

    def incident_edges(self, v):
        """Return all outgoing edges incident to vertex v in the graph.
        """
        self._validate_vertex(v)
        adj = self._outgoing
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None):
        """Insert and return a new Vertex with element x."""
        v = self.Vertex(x)
        for u in self.vertices():
            if v == u:
                return u
        self._outgoing[v] = {}
        self._incoming[v] = {}  # need distinct map for incoming edges
        return v

    def insert_edge(self, u, v, type):
        """Insert and return a new Edge from u to v with auxiliary element x.
        Raise a ValueError if u and v are not vertices of the graph.
        Raise a ValueError if u and v are already adjacent.
        """
        if self.get_edge(u, v) is not None:  # includes error checking
            raise ValueError('u and v are already adjacent')
        e = self.Edge(u, v, FamilyGraph.Edge.RelationType(type))
        self._outgoing[u][v] = e
        self._incoming[v][u] = e
        e = self.Edge(v, u, ~FamilyGraph.Edge.RelationType(type))
        self._outgoing[v][u] = e
        self._incoming[u][v] = e

    def adjacent_vertices(self, v, type=None):
        """
        Returns all adjacent vertices if type if None,
        otherwise returns vertices, which connected with special type of edge.
        """
        vertices = []
        if type is not None:
            for edge in self.incident_edges(v):
                if edge._type == FamilyGraph.Edge.RelationType(type):
                    vertices.append(edge.opposite(v))
        else:
            for edge in self.incident_edges(v):
                vertices.append(edge.opposite(v))
        return vertices

    def graph_intersection(self, other):
        """
        Returns True if at least 1 vertex from self is in other.
        :param other: FamilyGraph
        :return: bool
        """
        for v in self.vertices():
            for u in other.vertices():
                if str(u) == str(v):
                    return True
        return False

    def draw(self, vertex):
        """
        Draws graph from given vertex down.
        :param vertex: Vertex
        :return: dict
        """
        if vertex.element().get_sex == "f":
            partner_type = "husband"
        else:
            partner_type = "wife"
        graph = {"1. Name:": str(vertex),
                 "2. Partners:": [str(v) for v in self.adjacent_vertices(vertex, partner_type)],
                 "3. Children:": [self.draw(v) for v in self.adjacent_vertices(vertex, "child")]}
        return graph
