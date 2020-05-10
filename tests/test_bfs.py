#!/usr/bin/env python3
import unittest
import networkx as nx
from Medusa.graphs import bfs

class TestBFS(unittest.TestCase):
    def test_disconnected_graph(self):
        G = nx.Graph()
        node_list = ['A', 'B', 'C', 'D', 'E', 'F']
        G.add_nodes_from(node_list)
        self.assertEqual(list(G.nodes), node_list)
        bfs.breadth_first_search(G, 'A', 1)
        self.assertEqual(G.nodes['A']['distance'], 0)
        self.assertEqual(G.nodes['B']['distance'], -1)
        self.assertEqual(G.nodes['C']['distance'], -1)
        self.assertEqual(G.nodes['D']['distance'], -1)
        self.assertEqual(G.nodes['E']['distance'], -1)
        self.assertEqual(G.nodes['F']['distance'], -1)

    def test_sequential(self):
        G = nx.Graph()
        node_list = ['A', 'B', 'C', 'D', 'E', 'F']
        G.add_nodes_from(node_list)
        edge_list = [('A','C'),('A', 'B'),('C','E'),('B', 'D'),('D','F')]
        G.add_edges_from(edge_list)
        bfs.breadth_first_search(G, 'A', 1)
        self.assertEqual(G.nodes['A']['distance'], 0)
        self.assertEqual(G.nodes['B']['distance'], 1)
        self.assertEqual(G.nodes['C']['distance'], 1)
        self.assertEqual(G.nodes['D']['distance'], 2)
        self.assertEqual(G.nodes['E']['distance'], 2)
        self.assertEqual(G.nodes['F']['distance'], 3)

    def test_parallel_2(self):
        G = nx.Graph()
        node_list = ['A', 'B', 'C', 'D', 'E', 'F']
        G.add_nodes_from(node_list)
        edge_list = [('A','C'),('A', 'B'),('C','E'),('B', 'D'),('D','F')]
        G.add_edges_from(edge_list)
        bfs.breadth_first_search(G, 'A', 2)
        self.assertEqual(G.nodes['A']['distance'], 0)
        self.assertEqual(G.nodes['B']['distance'], 1)
        self.assertEqual(G.nodes['C']['distance'], 1)
        self.assertEqual(G.nodes['D']['distance'], 2)
        self.assertEqual(G.nodes['E']['distance'], 2)
        self.assertEqual(G.nodes['F']['distance'], 3)

    def test_parallel_3(self):
        G = nx.Graph()
        node_list = ['A', 'B', 'C', 'D', 'E', 'F']
        G.add_nodes_from(node_list)
        edge_list = [('A','C'),('A', 'B'),('C','E'),('B', 'D'),('D','F')]
        G.add_edges_from(edge_list)
        bfs.breadth_first_search(G, 'A', 3)
        self.assertEqual(G.nodes['A']['distance'], 0)
        self.assertEqual(G.nodes['B']['distance'], 1)
        self.assertEqual(G.nodes['C']['distance'], 1)
        self.assertEqual(G.nodes['D']['distance'], 2)
        self.assertEqual(G.nodes['E']['distance'], 2)
        self.assertEqual(G.nodes['F']['distance'], 3)

    def test_parallel_4(self):
        G = nx.Graph()
        node_list = ['A', 'B', 'C', 'D', 'E', 'F']
        G.add_nodes_from(node_list)
        edge_list = [('A','C'),('A', 'B'),('C','E'),('B', 'D'),('D','F')]
        G.add_edges_from(edge_list)
        bfs.breadth_first_search(G, 'A', 4)
        self.assertEqual(G.nodes['A']['distance'], 0)
        self.assertEqual(G.nodes['B']['distance'], 1)
        self.assertEqual(G.nodes['C']['distance'], 1)
        self.assertEqual(G.nodes['D']['distance'], 2)
        self.assertEqual(G.nodes['E']['distance'], 2)
        self.assertEqual(G.nodes['F']['distance'], 3)

    def test_parallel_5(self):
        G = nx.Graph()
        node_list = ['A', 'B', 'C', 'D', 'E', 'F']
        G.add_nodes_from(node_list)
        edge_list = [('A','C'),('A', 'B'),('C','E'),('B', 'D'),('D','F')]
        G.add_edges_from(edge_list)
        bfs.breadth_first_search(G, 'A', 5)
        self.assertEqual(G.nodes['A']['distance'], 0)
        self.assertEqual(G.nodes['B']['distance'], 1)
        self.assertEqual(G.nodes['C']['distance'], 1)
        self.assertEqual(G.nodes['D']['distance'], 2)
        self.assertEqual(G.nodes['E']['distance'], 2)
        self.assertEqual(G.nodes['F']['distance'], 3)

    def test_parallel_6(self):
        G = nx.Graph()
        node_list = ['A', 'B', 'C', 'D', 'E', 'F']
        G.add_nodes_from(node_list)
        edge_list = [('A','C'),('A', 'B'),('C','E'),('B', 'D'),('D','F')]
        G.add_edges_from(edge_list)
        bfs.breadth_first_search(G, 'A', 6)
        self.assertEqual(G.nodes['A']['distance'], 0)
        self.assertEqual(G.nodes['B']['distance'], 1)
        self.assertEqual(G.nodes['C']['distance'], 1)
        self.assertEqual(G.nodes['D']['distance'], 2)
        self.assertEqual(G.nodes['E']['distance'], 2)
        self.assertEqual(G.nodes['F']['distance'], 3)

    def test_parallel_7(self):
        G = nx.Graph()
        node_list = ['A', 'B', 'C', 'D', 'E', 'F']
        G.add_nodes_from(node_list)
        edge_list = [('A','C'),('A', 'B'),('C','E'),('B', 'D'),('D','F')]
        G.add_edges_from(edge_list)
        bfs.breadth_first_search(G, 'A', 7)
        self.assertEqual(G.nodes['A']['distance'], 0)
        self.assertEqual(G.nodes['B']['distance'], 1)
        self.assertEqual(G.nodes['C']['distance'], 1)
        self.assertEqual(G.nodes['D']['distance'], 2)
        self.assertEqual(G.nodes['E']['distance'], 2)
        self.assertEqual(G.nodes['F']['distance'], 3)












