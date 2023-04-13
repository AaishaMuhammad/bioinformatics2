"""
DeBruijn Graph from k-mers Problem: Construct the de Bruijn graph from a set of k-mers.

Input: A collection of k-mers Patterns.
Output: The adjacency list of the de Bruijn graph DeBruijn(Patterns).

Sample Input:
GAGG CAGG GGGG GGGA CAGG AGGG GGAG

Sample Output:
AGG: GGG
CAG: AGG AGG
GAG: AGG
GGA: GAG
GGG: GGA GGG

"""


def debruijin(kmers):
    uniques = {}
    k = len(kmers[0])
    for kmer in kmers:
        
        if kmer[: k-1] not in uniques:
            uniques[kmer[: k-1]] = []
        if kmer[1:] not in uniques:
            uniques[kmer[1:]] = []

    for kmer in kmers:
        uniques[kmer[: k-1]].append(kmer[1:])
        uniques[kmer[: k-1]].sort()

    uniques = dict(sorted(uniques.items()))

    for key in list(uniques):
        if len(uniques[key]) == 0:
            del uniques[key]

    return uniques

def OutputFormat(txt):
    out = []
    for key, value in txt.items():
        values = " ".join(x for x in value)
        out.append(f"{str(key)}: {str(values)}")
    return "\n".join(out)

pattern = "GAGG CAGG GGGG GGGA CAGG AGGG GGAG"
inp = pattern.split(" ")
print(OutputFormat(debruijin(inp)))

# data = open("./data/dataset_200_8.txt").read().split()

# with open("./file5.txt", "w") as file:
#     file.write(OutputFormat(debruijin(data)))

