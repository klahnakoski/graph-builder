from collections import namedtuple

Arrow = namedtuple("Arrow", ["src", "des"])


class Graph:
    def __init__(self):
        self.arrows = []

    def __str__(self):
        return "\n".join(
            str(s.value) + "=>" + str(d.value)
            for s, d in self.arrows
        )


graph = Graph()


class Builder:
    """
    Accumulate a chain of connections
    """
    def __init__(self, graph, start):
        self.graph = graph
        self.rhs = start

    def __lshift__(self, other):
        if not isinstance(other, Thing):
            other = Thing(other)
        self.graph.arrows.append(Arrow(other, self.rhs))
        self.rhs = other
        return self

    def __rshift__(self, other):
        if not isinstance(other, Thing):
            other = Thing(other)
        self.graph.arrows.append(Arrow(self.rhs, other))
        self.rhs = other
        return self


class Thing():

    def __init__(self, value):
        self.graph = graph
        self.value = value

    def __lshift__(self, other):
        b = Builder(self.graph, self)
        return b << other

    def __rshift__(self, other):
        b = Builder(self.graph, self)
        return b >> other

    def __rlshift__(self, other):
        b = Builder(self.graph, self)
        return b >> other

    def __rrshift__(self, other):
        b = Builder(self.graph, self)
        return b << other

    def __str__(self):
        return str(self.value)


a = Thing("a")
b = Thing("b")
c = Thing("c")

a << b << c

a << c >> b

5 >> c


print(graph)
