"""
Code Challenge: Implement MaximalNonBranchingPaths.
    Input: The adjacency list of a graph whose nodes are integers.
    Output: The collection of all maximal nonbranching paths in this graph.

Sample Input:
    1: 2
    2: 3
    3: 4 5
    6: 7
    7: 6

Sample Output:
    1 2 3
    3 4
    3 5
    7 6 7
"""

from collections import defaultdict
import numpy as np
import pandas as pd


def read_data(file_path):
    fileInput = []
    path = []
    temp = []

    with open(file_path, "r") as fstream:
        fileInput = fstream.readlines()

    for line in fileInput:
        temp.append(line.rstrip())
        path.append(temp)
        temp = []

    graph = {}
    for element in path:
        temp = element[0].split(": ")
        graph[temp[0]] = temp[1].split(" ")
    

    return graph

def degree_finder(graph):
    degrees = defaultdict(int)
    for k in graph:
        for v in graph[k]:
            degrees[k] += 1
            degrees[v] -= 1
    
    return degrees

def load_adj_mat(graph_edges): # this method creates adjacent matrix
    st = set()
    for key in graph_edges.keys():
        st.add(key)
        for value in graph_edges[key]:
            st.add(value)
    
    st = list(np.sort([int(x) for x in list(st)]))
    st = [str(x) for x in st] # lexicographical order
    adj_mat = pd.DataFrame(np.zeros((len(st),len(st)),dtype=int),index=list(st),columns=list(st))
    
    for key in graph_edges.keys():
        for value in graph_edges[key]:
            adj_mat.loc[key,value] = 1
            
    #print(adj_mat)
    return adj_mat

def i_dfs(matrix,u,status):
    path = "" + u
    while True:
        status[u] = 'G'
        v = matrix.columns[matrix.loc[u].isin([1])].tolist()[0]
        
        path += " " + v

        if status[v] == 'G':
            break
        
        u = v
    return path

def MaximalNonBranchingPaths(graph):
    matrix = load_adj_mat(graph)
    Paths = []
    Set = set()
    
    #ICycle inits
    status = {}
    icycle_paths = []
    
    for key in graph.keys():
        if (not(matrix.loc[key].sum() == 1 and matrix[key].sum() == 1)):
            if (matrix.loc[key].sum() > 0):
                outgoing_nodes = matrix.index[matrix.loc[key].isin([1])].tolist()
                Set.add(key)
                for outnode in outgoing_nodes:
                    path = key + ""
                    while(matrix.loc[outnode].sum()==1 and matrix[outnode].sum()==1):
                        Set.add(outnode)
                        path = path + " " + outnode
                        outnode = matrix.index[matrix.loc[outnode].isin([1])].tolist()[0]

                    Set.add(outnode)
                    Paths.append(path + " " + outnode)

    icycle_nodes = [key for key in graph.keys() if key not in Set]
    for node in icycle_nodes:
        status[node] = 'W'
    
    for node in icycle_nodes:
        if status[node] == 'W':
            icycle_paths.append(i_dfs(matrix,node,status))
    
    Paths += icycle_paths
    return (Paths,matrix,icycle_paths)



# p1 = "./testfile.txt"
# p2 = "./data/dataset_6207_2.txt"

data_dict = read_data(p2)
paths, matrix, ic = MaximalNonBranchingPaths(data_dict)
print(paths)

with open("./file12.txt", "w") as file:
    for path in paths:
        file.write(path + "\n")
