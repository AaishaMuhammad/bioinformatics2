"""
Code Challenge: Solve the Eulerian Path Problem.
    Input: The adjacency list of a directed graph that has an Eulerian path.
    Output: An Eulerian path in this graph.

Sample Input:
    0: 2
    1: 3
    2: 1
    3: 0 4
    6: 3 7
    7: 8
    8: 9
    9: 6

Sample Output:
    6 7 8 9 6 3 0 2 1 3 4

"""

from random import randint
from collections import defaultdict


# Reading data in the specific file formatting
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


# Finding the in-and-out degree of each node
def degree_finder(graph):
    degrees = defaultdict(int)
    for k in graph:
        for v in graph[k]:
            degrees[k] += 1
            degrees[v] -= 1
    start_point = [k for k,v in degrees.items() if v == 1]
    end_point = [k for k,v in degrees.items() if v == -1]
    return start_point, end_point


def find_eulerian_path(graph, starter, ender):
    vertices = graph
    start = []

    # maxGraph = max(list(graph.keys()), key=int)
    # start_vertex = randint(0, int(maxGraph))
    start.append(starter[0])

    print(start)

    stack = [start[0]]
    tour = []

    while stack: 
        v = stack[-1]
        if v == ender[0]:
            stack.pop(-1)

        elif vertices[v]:
            w = vertices[v][0]
            stack.append(w)
            # print("stack:", stack)
            del vertices[v][0]

        else: 
            tour.append(stack.pop())
    # print("--------------------------")
    tour.insert(0, ender[0])
    return tour




# p1 = "./testfile.txt"

# data_dict = read_data(p1)
# start, end = degree_finder(data_dict)
# print("Start:", start, "End:", end)
# # find_eulerian_path(data_dict, start, end)
# print(" ".join(find_eulerian_path(data_dict, start, end)))

p2 = "./data/dataset_203_6.txt"
data_dict2 = read_data(p2)
start, end = degree_finder(data_dict2)
with open("./file7.txt", "w") as file:
    file.write(" ".join(reversed(find_eulerian_path(data_dict2, start, end))))
