import multiprocessing as mp
import networkx as nx
from functools import partial

def breadth_first_search(G, source, num_p):
    """
    Implementation of breadth-first-search in parallel.

    Args:
        G (nx obj): networkx graph
        source: node ID of the node from which to start bfs
        num_p (int): number of processors
    
    Returns:
        An added distance attribute for all nodes from source
    """

    # Create a manager, and initialize a commonly managed dictionary
    # which will be responsible for keeping the level of each node
    manager = mp.Manager()
    node_levels = manager.dict()
    for node in G.nodes:
        node_levels[node] = -1

    node_levels[source] = 0 # src distance to src is 0
    dist = 1
    curr_frontier = []
    curr_frontier.append(source)
    next_frontier = manager.list()

    while len(curr_frontier) != 0:
        next_neighbors = []
        for u in curr_frontier:
            next_neighbors.append([n for n in G[u]])
        pool = mp.Pool(num_p)
        attr_lvl = partial(attribute_lvl, dist, next_frontier, node_levels)
        pool.map_async(attr_lvl, next_neighbors)
        pool.close()
        pool.join()
        curr_frontier = next_frontier
        next_frontier = manager.list()
        dist += 1

    nx.set_node_attributes(G, node_levels, 'distance')
    print(node_levels)
    #for node in G.nodes:
    #    print("node {} has dist = {}".format(G.nodes[node]['distance']))

def attribute_lvl(level, next_frontier, node_levels, node_slice):
    # Iterate over all nodes that neighbor nodes in the current level
    for v in node_slice:
        # If neighbor has never been found before
        if node_levels[v] == -1:
            next_frontier.append(v)
            node_levels[v] = level

'''
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

    breadth_first_search(G, 'A', 4)
    breadth_first_search(G, 'B', 4)
    breadth_first_search(G, 'F', 4)


if __name__ == '__main__':
    main()

'''
