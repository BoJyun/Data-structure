# https://medium.com/100-days-of-python/day-11-data-structure-graph-a4229c3dabaf
# https://www.bogotobogo.com/python/python_graph_data_structures.php
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

    def get_nighboirs_weights(self):
        return self._adjacent.values()


class Graph():
    def __init__(self):
        self._vertexDict = {}
        self._num_vertex = 0

    def __iter__(self):
        return iter(self._vertexDict.values())

    def add_vertex(self, node):
        if node in self._vertexDict:
            return self._vertexDict[node]
        else:
            new_vertex = Vertex(node)
            self._vertexDict[node] = new_vertex
            self._num_vertex += 1
            return new_vertex

    def add_edge(self, frm, to, w=0):
        if frm not in self._vertexDict:
            self.add_vertex(frm)
        if to not in self._vertexDict:
            self._vertexDict(to)

        self._vertexDict[frm].set_weight(to, w)
        self._vertexDict[to].set_weight(frm, w)

    def get_verSum(self):
        return self._num_vertex

    def get_vertexs(self):
        return self._vertexDict.keys()

    def get_vertex(self, id):
        if id in self._vertexDict:
            return self._vertexDict[id]
        else:
            return None


if __name__ == '__main__':
    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

    for v in g:
        for h in v.get_neighbors():
            v_id = v.get_id()

            print("'{0}','{1}',{2}".format(v_id, h, v.get_weight(h)))

    for v in g:
        print("g.vert_dict['{0}']={1}".format(v.get_id(), v.get_neighbors()))
