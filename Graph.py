# https://medium.com/100-days-of-python/day-11-data-structure-graph-a4229c3dabaf

# Adjacency List

class Vertex():
    def __init__(self, node):
        self._id = node
        self._adjacent = {}

    def get_id(self):
        return self._id

    def get_weight(self, neighbor):
        return self._adjacent[neighbor]

    def set_weight(self, neighbor, weight=0):
        self._adjacent[neighbor] = weight

    def get_neighbors(self):
        return self._adjacent.keys()


class Graph():
    def __init__(self):
        self._vertexDict = {}
        self.num_vertex = 0

    def add_vertex(self, node):
        if node in self._vertexDict:
            return self._vertexDict[node]
        else:
            new_vertex = Vertex(node)
            self._vertexDict[node] = new_vertex
            self.num_vertex += 1
            return new_vertex
