import math
import multiprocessing as mp
import networkx as nx
from functools import partial

def min_span_tree(G, proc_num):
    """
    Implementation of Boruvka's algorithm to find minimum spanning trees using
    multiprocessing to process

    Inputs
        G     (nx obj):  networkx undirected graph
        proc_num (int): number of processors
    Outputs
        F (nx obj): a minimum spanning tree of G
    """
    # Initialize F to be a forest composed of the nodes in G
    F = nx.Graph()
    F.add_nodes_from(G.nodes)

    # Create manager so processes can share information about nodes
    # and edges in graphs F and G
    manager = mp.Manager()
    G_nodes = manager.dict()
    for node in G.nodes:
        G_nodes[node] = -1
    G_edges = manager.list()
    for edge in G.edges:
        u, v = edge
        G_edges.append((edge, G.get_edge_data(u, v)['weight']))

    num_components = nx.number_connected_components(F)
    n = 1
    while(num_components > 1):
        print("="*60)
        print("Iteration number", n)
        # Store a list of all connected components in F
        components = manager.list()
        idx = 0
        for component in nx.connected_components(F):
            # component = [node_list[], label])
            components.append([list(component), idx])
            idx += 1
        cheapest_edges = manager.list([(None, math.inf) for i in range(nx.number_connected_components(F))])
        # Create and execute a pool of processors that will label
        # nodes according to the component they are members of
        labeling_pool = mp.Pool(proc_num)
        label_func = partial(label_graph, G_nodes)
        labeling_pool.map_async(label_func, components)
        labeling_pool.close()
        labeling_pool.join()

        # Create and execute a pool of processors that will find
        # the cheapest edge associated with each component
        finding_pool = mp.Pool(proc_num)
        find_func = partial(find_cheapest_edge, G_nodes, components, cheapest_edges)
        finding_pool.map(find_func, G_edges)
        finding_pool.close()
        finding_pool.join()

        print("Components",components)
        print("CheapEdges",cheapest_edges)
        for i in range(num_components):
            if cheapest_edges[i][0] != None:
                u, v = cheapest_edges[i][0]
                w = cheapest_edges[i][1]
                print("Adding ({}, {}), weight={}".format(u, v, w))
                F.add_edge(u, v, weight=w)
        num_components = nx.number_connected_components(F)
        n += 1
    return F


def label_graph(G_nodes, comp_slice):
    # comp_slice[0] holds the set of nodes members of the component
    # comp_slice[1] holds the label
    size = len(comp_slice[0])
    for i in range(size):
        G_nodes[comp_slice[0][i]] = comp_slice[1]

def find_cheapest_edge(G_nodes, components, cheapest_edges, edge):
    u, v = edge[0]
    weight = edge[1]
    u_idx = G_nodes[u]
    v_idx = G_nodes[v]
    if u_idx != v_idx:
        if weight < cheapest_edges[u_idx][1]:
            cheapest_edges[u_idx] = ((u, v), weight)
        if weight < cheapest_edges[v_idx][1]:
            cheapest_edges[v_idx] = ((u, v), weight)



def main():
    G = nx.Graph()
    G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    G.add_edge('A', 'D', weight=4)
    G.add_edge('A', 'B', weight=7)
    G.add_edge('B', 'C', weight=11)
    G.add_edge('B', 'D', weight=9)
    G.add_edge('B', 'E', weight=10)
    G.add_edge('C', 'E', weight=5)
    G.add_edge('D', 'E', weight=15)
    G.add_edge('D', 'F', weight=6)
    G.add_edge('E', 'F', weight=12)
    G.add_edge('E', 'G', weight=8)
    G.add_edge('F', 'G', weight=13)

    F = min_span_tree(G, 2)
    print("NODES:", F.nodes)
    print("EDGES:", F.edges)


if __name__ == '__main__':
    main()
