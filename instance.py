import utils


class Instance:
    def __init__(self, I, M, cij, wi, b):
        self.I = I
        self.M = M
        self.cij = cij
        self.wi = wi
        self.b = b

    def vertex_labels(self):
        return {i: f'{i} ({self.wi[i]})' for i in self.I}

    def edge_labels(self, edges):
        return {(i, j): str(self.cij[i][j]) for i, j in edges}

    def undirected_edges(self):
        return [(i, j) for i in self.I for j in self.I if i < j]


def instance_from_dict(obj):
    return Instance(*[obj[field] for field in ['I', 'M', 'cij', 'wi', 'b']])


def example_instance():
    # orte
    I = list(range(4))
    # touren
    M = list(range(2))

    # distanzen
    cij = [[0, 10, 20, 30],
           [10, 0, 20, 30],
           [20, 20, 0, 30],
           [30, 30, 30, 0]]

    # nachfragemenge i
    wi = [0, 8, 10, 2]

    # wagenkapazität
    b = 18

    return Instance(I, M, cij, wi, b)


def visualize_instance(inst: Instance):
    utils.plot_graph(inst.I, inst.undirected_edges(), inst.vertex_labels(), inst.edge_labels(inst.undirected_edges()), 'instance', 'graph')
