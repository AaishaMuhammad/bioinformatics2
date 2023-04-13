"""
Code Challenge: Solve the String Reconstruction Problem.
    Input: An integer k followed by a list of k-mers Patterns.
    Output: A string Text with k-mer composition equal to Patterns. (If multiple answers exist, you may return any one.)

Sample Input:
    4
    CTTA ACCA TACC GGCT GCTT TTAC

Sample Output:
    GGCTTACCA
"""

from debruijin2 import debruijin
from eulerian_path import find_eulerian_path, degree_finder
from genome_path import PathToGenome

def genome_reconstruction(Patterns):
    deb_graph = debruijin(Patterns)
    start, end = degree_finder(deb_graph)
    path = list(reversed(find_eulerian_path(deb_graph, start, end)))
    text = PathToGenome(path)

    return text

# pattern = "CTTA ACCA TACC GGCT GCTT TTAC"
# inp = pattern.split(" ")
# print(genome_reconstruction(inp))


p2 = "./data/dataset_203_7 (1).txt"
with open(p2, "r") as file:
    data = file.readlines()[1].split(" ")


with open("./file8.txt", "w") as file:
    file.write(genome_reconstruction(data))
