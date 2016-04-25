import csv
import numpy as np
import networkx as netx
import pylab as plt

list_unsorted = []
arr_size = 4097 #node size
# Reshape the input string into a numpy array then a graph
result = np.loadtxt(open("ADJMAT.csv","rb"),delimiter=",",skiprows=0)
result = result.astype(int)

print('completed CHECK!')

G = netx.Graph(result)
for initial_p in range (0,arr_size):
	list_unsorted.append((initial_p,G.degree(initial_p)))

def getKey(item):
	return item[1]

list_sorted = sorted(list_unsorted, key=getKey)

print(list_sorted[-9:])
