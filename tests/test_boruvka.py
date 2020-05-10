#!/usr/bin/env python3
import unittest
import networkx as nx
from Medusa.graphs import boruvka

class TestBoruvka(unittest.TestCase):
    def test_sequential(self):
        G = nx.Graph()
        node_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        G.add_nodes_from(node_list)
        self.assertEqual(list(G.nodes), node_list)
        edge_list = [('A','D', {'weight':4}), ('A','B', {'weight':7}), ('B','C', {'weight':11}),
                    ('B','D', {'weight':9}), ('B','E', {'weight':10}), ('C','E', {'weight':5}),
                    ('D','E', {'weight':15}), ('D','F', {'weight':6}), ('E','F', {'weight':12}),
                    ('E','G', {'weight':8}), ('F','G', {'weight':13})]
        G.add_edges_from(edge_list)
        min_edge_list = [('A','D'),('A','B'),('B','E'),('C','E'),('D','F'),('E','G')]
        min_edge_list = set(min_edge_list)

        F = boruvka.min_span_tree(G, 1)
        self.assertEqual(list(F.nodes), node_list)
        self.assertEqual(set(F.edges), min_edge_list) 
        
    def test_parallel_2(self):
        G = nx.Graph()
        node_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        G.add_nodes_from(node_list)
        self.assertEqual(list(G.nodes), node_list)
        edge_list = [('A','D', {'weight':4}), ('A','B', {'weight':7}), ('B','C', {'weight':11}),
                    ('B','D', {'weight':9}), ('B','E', {'weight':10}), ('C','E', {'weight':5}),
                    ('D','E', {'weight':15}), ('D','F', {'weight':6}), ('E','F', {'weight':12}),
                    ('E','G', {'weight':8}), ('F','G', {'weight':13})]
        G.add_edges_from(edge_list)
        min_edge_list = [('A','D'),('A','B'),('B','E'),('C','E'),('D','F'),('E','G')]
        min_edge_list = set(min_edge_list)

        F = boruvka.min_span_tree(G, 2)
        self.assertEqual(list(F.nodes), node_list)
        self.assertEqual(set(F.edges), min_edge_list) 
 
    def test_parallel_3(self):
        G = nx.Graph()
        node_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        G.add_nodes_from(node_list)
        self.assertEqual(list(G.nodes), node_list)
        edge_list = [('A','D', {'weight':4}), ('A','B', {'weight':7}), ('B','C', {'weight':11}),
                    ('B','D', {'weight':9}), ('B','E', {'weight':10}), ('C','E', {'weight':5}),
                    ('D','E', {'weight':15}), ('D','F', {'weight':6}), ('E','F', {'weight':12}),
                    ('E','G', {'weight':8}), ('F','G', {'weight':13})]
        G.add_edges_from(edge_list)
        min_edge_list = [('A','D'),('A','B'),('B','E'),('C','E'),('D','F'),('E','G')]
        min_edge_list = set(min_edge_list)

        F = boruvka.min_span_tree(G, 3)
        self.assertEqual(list(F.nodes), node_list)
        self.assertEqual(set(F.edges), min_edge_list) 
 
    def test_parallel_4(self):
        G = nx.Graph()
        node_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        G.add_nodes_from(node_list)
        self.assertEqual(list(G.nodes), node_list)
        edge_list = [('A','D', {'weight':4}), ('A','B', {'weight':7}), ('B','C', {'weight':11}),
                    ('B','D', {'weight':9}), ('B','E', {'weight':10}), ('C','E', {'weight':5}),
                    ('D','E', {'weight':15}), ('D','F', {'weight':6}), ('E','F', {'weight':12}),
                    ('E','G', {'weight':8}), ('F','G', {'weight':13})]
        G.add_edges_from(edge_list)
        min_edge_list = [('A','D'),('A','B'),('B','E'),('C','E'),('D','F'),('E','G')]
        min_edge_list = set(min_edge_list)

        F = boruvka.min_span_tree(G, 4)
        self.assertEqual(list(F.nodes), node_list)
        self.assertEqual(set(F.edges), min_edge_list) 
 
    def test_parallel_5(self):
        G = nx.Graph()
        node_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        G.add_nodes_from(node_list)
        self.assertEqual(list(G.nodes), node_list)
        edge_list = [('A','D', {'weight':4}), ('A','B', {'weight':7}), ('B','C', {'weight':11}),
                    ('B','D', {'weight':9}), ('B','E', {'weight':10}), ('C','E', {'weight':5}),
                    ('D','E', {'weight':15}), ('D','F', {'weight':6}), ('E','F', {'weight':12}),
                    ('E','G', {'weight':8}), ('F','G', {'weight':13})]
        G.add_edges_from(edge_list)
        min_edge_list = [('A','D'),('A','B'),('B','E'),('C','E'),('D','F'),('E','G')]
        min_edge_list = set(min_edge_list)

        F = boruvka.min_span_tree(G, 5)
        self.assertEqual(list(F.nodes), node_list)
        self.assertEqual(set(F.edges), min_edge_list) 
 
    def test_parallel_6(self):
        G = nx.Graph()
        node_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        G.add_nodes_from(node_list)
        self.assertEqual(list(G.nodes), node_list)
        edge_list = [('A','D', {'weight':4}), ('A','B', {'weight':7}), ('B','C', {'weight':11}),
                    ('B','D', {'weight':9}), ('B','E', {'weight':10}), ('C','E', {'weight':5}),
                    ('D','E', {'weight':15}), ('D','F', {'weight':6}), ('E','F', {'weight':12}),
                    ('E','G', {'weight':8}), ('F','G', {'weight':13})]
        G.add_edges_from(edge_list)
        min_edge_list = [('A','D'),('A','B'),('B','E'),('C','E'),('D','F'),('E','G')]
        min_edge_list = set(min_edge_list)

        F = boruvka.min_span_tree(G, 6)
        self.assertEqual(list(F.nodes), node_list)
        self.assertEqual(set(F.edges), min_edge_list) 
 
    def test_parallel_7(self):
        G = nx.Graph()
        node_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        G.add_nodes_from(node_list)
        self.assertEqual(list(G.nodes), node_list)
        edge_list = [('A','D', {'weight':4}), ('A','B', {'weight':7}), ('B','C', {'weight':11}),
                    ('B','D', {'weight':9}), ('B','E', {'weight':10}), ('C','E', {'weight':5}),
                    ('D','E', {'weight':15}), ('D','F', {'weight':6}), ('E','F', {'weight':12}),
                    ('E','G', {'weight':8}), ('F','G', {'weight':13})]
        G.add_edges_from(edge_list)
        min_edge_list = [('A','D'),('A','B'),('B','E'),('C','E'),('D','F'),('E','G')]
        min_edge_list = set(min_edge_list)

        F = boruvka.min_span_tree(G, 7)
        self.assertEqual(list(F.nodes), node_list)
        self.assertEqual(set(F.edges), min_edge_list) 
 
    def test_parallel_8(self):
        G = nx.Graph()
        node_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        G.add_nodes_from(node_list)
        self.assertEqual(list(G.nodes), node_list)
        edge_list = [('A','D', {'weight':4}), ('A','B', {'weight':7}), ('B','C', {'weight':11}),
                    ('B','D', {'weight':9}), ('B','E', {'weight':10}), ('C','E', {'weight':5}),
                    ('D','E', {'weight':15}), ('D','F', {'weight':6}), ('E','F', {'weight':12}),
                    ('E','G', {'weight':8}), ('F','G', {'weight':13})]
        G.add_edges_from(edge_list)
        min_edge_list = [('A','D'),('A','B'),('B','E'),('C','E'),('D','F'),('E','G')]
        min_edge_list = set(min_edge_list)

        F = boruvka.min_span_tree(G, 8)
        self.assertEqual(list(F.nodes), node_list)
        self.assertEqual(set(F.edges), min_edge_list) 
 





















