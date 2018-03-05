import os


def plot_graph(vertices, edges, vertex_labels = {}, edge_labels = {}, out_name = 'graph', graphtype = 'digraph'):
    edgesym = '->' if graphtype == 'digraph' else '--'

    def optional_label(obj_id, label_dict):
        if obj_id in label_dict:
            return ' [label="' + label_dict[obj_id] + '"]'
        return ''

    ostr = graphtype  + ' {\n' + ';\n'.join([str(vertex) + optional_label(vertex, vertex_labels) for vertex in vertices] + [str(i) + edgesym + str(j) + optional_label((i, j), edge_labels) for i, j in edges]) + '\n}'

    with open(f'{out_name}.dot', 'w') as fp:
        fp.write(ostr)

    os.system(f'dot -Tpng -o {out_name}.png {out_name}.dot')
