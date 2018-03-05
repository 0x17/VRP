import instance

def savings_heuristic(inst: instance.Instance):
    sol = [ [0, i, 0] for i in inst.I[1:] ]
    #mergable_edges