import utils


class Instance:
    def __init__(self, I, M, cij, wi, b):
        self.I = I
        self.M = M
        self.cij = cij
        self.wi = wi
        self.b = b


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
    b = 20

    return Instance(I, M, cij, wi, b)


def visualize_instance(inst: Instance):
    edges = [ (i,j) for i in inst.I for j in inst.I if i < j ]
    edgelbls = { (i,j): str(inst.cij[i][j]) for i,j in edges }
    nodelbls = { i: f'{i} ({inst.wi[i]})' for i in inst.I }
    utils.plot_graph(inst.I, edges, nodelbls, edgelbls, 'instance', 'graph')
