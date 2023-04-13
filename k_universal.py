"""
Code Challenge: Solve the k-Universal Circular String Problem.
    Input: An integer k.
    Output: A k-universal circular string.

Sample Input:
    3

Sample Output:
    00111010    
"""

from itertools import product
from random import randint, choice
from debruijin2 import debruijin
from genome_path import PathToGenome

def find_eulerian_cycle(graph):
    vertices = graph
    start = []

    keys = list(vertices.keys())
    maxGraph = max(list(graph.keys()), key=int)
    start_vertex = choice(keys)
    start.append(start_vertex)


    stack = [start[0]]
    tour = []

    while stack: 
        v = stack[-1]

        if vertices[v]:
            w = vertices[v][0]
            stack.append(w)
            # print("stack:", stack)
            del vertices[v][0]

        else: 
            tour.append(stack.pop())
    # print("--------------------------")
    return tour

def k_universal(k):
    Patterns = ["".join(i) for i in product('01', repeat=k)]
    deb_graph = debruijin(Patterns)
    # print(Patterns)
    cycle = find_eulerian_cycle(deb_graph)
    # print(cycle)
    # print(deb_graph)
    path = list(reversed(cycle))
    text = PathToGenome(path)

    return text[:-k+1]



p1 = "./data/dataset_203_11 (7).txt"
with open(p1, "r") as file:
    data = int(file.read())

# print(k_universal(3))
with open("./file9.txt", "w") as file:
    file.write(k_universal(data))
