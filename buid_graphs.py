import networkx as nx
import matplotlib.pyplot as plt


num_nodes=4
base='../Data/'
in_file=base+"rdag"+str(4)+".txt"

with open(in_file,"r") as f:
    line=f.readline()
    line=line.strip('\n')
    count=1
    while line:
        count+=1
        links=list(line)
        print(links)

