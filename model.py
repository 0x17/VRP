from gurobipy import *

import utils


def set_gurobi_params(model):
    model.params.threads = 0
    model.params.mipgap = 0
    model.params.timelimit = GRB.INFINITY
    model.params.displayinterval = 5


def build_model(inst):
    try:
        model = Model("vrp")
        set_gurobi_params(model)

        # decision variables
        Xijm = [[[model.addVar(0.0, 1.0, 0.0, GRB.BINARY, f'Xi{i}j{j}m{m}') for m in inst.M] for j in inst.I] for i in inst.I]
        Yim = [[model.addVar(0.0, 1.0, 0.0, GRB.BINARY, f'Yi{i}m{m}') for m in inst.M] for i in inst.I]
        Zi = [model.addVar(-GRB.INFINITY, GRB.INFINITY, 0.0, GRB.CONTINUOUS, f'Zi{i}') for i in inst.I]

        # objective
        model.setObjective(quicksum(inst.cij[i][j] * Xijm[i][j][m] for m in inst.M for j in inst.I for i in inst.I))

        # constraints
        model.addConstrs((quicksum(inst.wi[i] * Yim[i][m] for i in inst.I) <= inst.b for m in inst.M), name='capacity')
        model.addConstrs((quicksum(Xijm[i][j][m] for j in inst.I) == Yim[i][m] for m in inst.M for i in inst.I), name='linksource')
        model.addConstrs((quicksum(Xijm[i][j][m] for i in inst.I) == Yim[j][m] for m in inst.M for j in inst.I), name='linksink')
        model.addConstrs((quicksum(Yim[i][m] for m in inst.M) == 1 for i in inst.I[1:]), name='eachloconce')
        model.addConstrs((Zi[i] - Zi[j] + len(inst.I) * quicksum(Xijm[i][j][m] for m in inst.M) <= len(inst.I) - 1 for i in inst.I[1:] for j in inst.I[1:] if i != j), name='nocycles')
        model.addConstrs((Xijm[i][i][m] == 0 for m in inst.M for i in inst.I), name='nonreflexive')

        model.update()

        model.write('mylp.lp')

        return {'vars': [Xijm, Yim], 'model': model}

    except GurobiError as e:
        print(e)


def parse_results(inst, Xijm):
    tours = [[(i, j) for i in inst.I for j in inst.I if Xijm[i][j][m].x == 1.0] for m in inst.M]
    print(tours)
    edges = [edge for m in inst.M for edge in tours[m]]
    utils.plot_graph(inst.I, edges, inst.vertex_labels(), inst.edge_labels(edges), 'solution')
