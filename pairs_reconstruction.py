"""
Code Challenge: Solve the String Reconstruction from Read-Pairs Problem.
    Input: Integers k and d followed by a collection of paired k-mers PairedReads.
    Output: A string Text with (k, d)-mer composition equal to PairedReads.

Sample Input:
    4 2
    GAGA|TTGA TCGT|GATG CGTG|ATGT TGGT|TGAG GTGA|TGTT GTGG|GTGA TGAG|GTTG GGTC|GAGA GTCG|AGAT

Sample Output:
    GTGGTCGTGAGATGTTGA

"""

from eulerian_path import find_eulerian_path
from collections import defaultdict

def PathToGenome(path):
    genome = list(path[0])
    for item in path[1:]:
        genome.append(item[-1])
    out = "".join(genome)  
    return out 

def debruijin(kmers):
    uniques = defaultdict(list)
    k = len(kmers[0])
    k = int((k-1)/2)
    for kmer in kmers:
        
        prefix_mer = kmer[:k-1]+kmer[k] + kmer[k+1:2*k]
        suffix_mer = kmer[1:k]+kmer[k]+kmer[k+2:]
        uniques[prefix_mer].append(suffix_mer)
        uniques[prefix_mer].sort()  

    uniques = dict(sorted(uniques.items()))

    for key in list(uniques):
        if len(uniques[key]) == 0:
            del uniques[key]

    return uniques

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
    for end in ender:
        tour.insert(0, end)

    return tour

def GappedPathToGenome(Patterns, k, d):
    first_pat = [x[:k] for x in Patterns]
    last_pats = [x[k+1:] for x in Patterns]
    prefix_string = PathToGenome(first_pat)
    suffix_string = PathToGenome(last_pats)    
        
    if suffix_string.startswith(prefix_string[d+k+1]):
        output = prefix_string + suffix_string[-k-d-1:]
    return output

def pairs_reconstruction(Patterns, k, d):
    db_graph = debruijin(Patterns)
    start, end = degree_finder(db_graph)
    path = list(reversed(find_eulerian_path(db_graph, start, end)))
    text = GappedPathToGenome(path, k-1, d)
    return text


# data = "ACAC|CTCT ACAT|CTCA CACA|TCTC GACA|TCTC".split(" ")
# out = pairs_reconstruction(data, 4, 2)
# print(out)
# print(out == "GTGGTCGTGAGAGTTGA")

p = "./data/dataset_204_16 (1).txt"
with open(p, "r") as file:
    data = file.readlines()[1].split(" ")


with open("./file11.txt", "w") as file:
    file.write(pairs_reconstruction(data, 50, 200))