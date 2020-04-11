NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph:
    def __init__(self, data=None):
        self.nodes = []
        self.edges = []
        self.attrs = {}
        if data:
            self.validate_data(data)
            for item in data:
                self.validate_item(item)
                if item[0] == NODE:
                    self.validate_node(item)
                    self.nodes.append(Node(item[1], item[2]))
                elif item[0] == EDGE:
                    self.validate_edge(item)
                    self.edges.append(Edge(item[1], item[2], item[3]))
                elif item[0] == ATTR:
                    self.validate_attr(item)
                    self.attrs[item[1]] = item[2]

    def validate_data(self, data):
        if not isinstance(data, list):
            raise TypeError("data must be list type.")

    def validate_item(self, item):
        if not isinstance(item, tuple):
            raise TypeError("data must be tuple type.")
        if not (len(item) == 3 or len(item) == 4):
            raise TypeError("Malformed item.")
        else:
            if len(item) == 3:
                if item[0] != NODE and item[0] != ATTR:
                    raise ValueError("Malformed item.")
            if len(item) == 4:
                if item[0] != EDGE:
                    raise ValueError("Malformed item.")

    def validate_node(self, item):
        if not isinstance(item[1], str) or not isinstance(item[2], dict):
            raise ValueError("Malformed node.")

    def validate_edge(self, item):
        if not isinstance(item[1], str) or not isinstance(item[2], str) or \
           not isinstance(item[3], dict):
            raise ValueError("Malformed edge.")

    def validate_attr(self, item):
        if not isinstance(item[1], str) or not isinstance(item[2], str):
            raise ValueError("Malformed attr.")
