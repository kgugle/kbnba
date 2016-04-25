import csv
import numpy as np
import networkx as netx
import pylab as plt

arr_size = 4097 #node size
# Reshape the input string into a numpy array then a graph
result = np.loadtxt(open("ADJMAT.csv","rb"),delimiter=",",skiprows=0)
result = result.astype(int)

print('completed CHECK!')

G = netx.Graph(result)


accumulator = 0
for initial_p in range (0,arr_size):
    print(initial_p)
    for connected_p in range (0,arr_size):
        p=netx.shortest_path_length(G,source = initial_p,target = connected_p, weight = None)
        accumulator+=p
print(accumulator)
print('final DOS: ')
print(float(accumulator)/float(arr_size*(arr_size-1)))
