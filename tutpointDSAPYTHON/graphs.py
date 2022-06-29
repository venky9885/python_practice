# V = {a, b, c, d, e}
# E = {ab, ac, bd, cd, de}


# Create the dictionary with graph elements
graph = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"]
}
# Print the graph
print(graph)
#!Display graph vertices


class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict
# Get the keys of the dictionary

    def getVertices(self):
        return list(self.gdict.keys())


# Create the dictionary with graph elements
graph_elements = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"]
}
g = graph(graph_elements)
print(g.getVertices())


#!Display graph edges

class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def edges(self):
        return self.findedges()
# Find the distinct list of edges

    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename


# Create the dictionary with graph elements
graph_elements = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"]
}
g = graph(graph_elements)
print(g.edges())


#!Adding a vertex
class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def getVertices(self):
        return list(self.gdict.keys())
# Add the vertex as a key

    def addVertex(self, vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx] = []


# Create the dictionary with graph elements
graph_elements = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"]
}
g = graph(graph_elements)
g.addVertex("f")
print(g.getVertices())


#!Adding an edge
class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def edges(self):
        return self.findedges()
# Add the new edge

    def AddEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]
# List the edge names

    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
                return edgename


# Create the dictionary with graph elements
graph_elements = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"]
}
g = graph(graph_elements)
g.AddEdge({'a', 'e'})
g.AddEdge({'a', 'c'})
print(g.edges())
