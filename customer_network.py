import networkx as nx
import csv as csv
import itertools as its
import matplotlib as mt

#Read in the edge csv, create the graph from the edges
G = nx.read_edgelist("EdgeList.csv", delimiter = ",", create_using = nx.Graph(), nodetype = str, data=True, edgetype=str)

#How many nodes and edges do we have?
print(G.number_of_nodes())
print(G.number_of_edges())
#print the specific edges and nodes
#print(G.nodes())
#print(G.edges())

print(nx.draw(G))

print("hello")