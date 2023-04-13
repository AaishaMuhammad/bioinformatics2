"""
Code Challenge: Implement StringSpelledByGappedPatterns.
    Input: Integers k and d followed by a sequence of (k, d)-mers (a1|b1), … , (an|bn) such that Suffix(ai|bi) = Prefix(ai+1|bi+1) for 1 ≤ i ≤ n-1.
    Output: A string Text of length k + d + k + n - 1 such that the i-th (k, d)-mer in Text is equal to (ai|bi)  for 1 ≤ i ≤ n (if such a string exists).

Sample Input:
    4 2
    GACC|GCGC ACCG|CGCC CCGA|GCCG CGAG|CCGG GAGC|CGGA

Sample Output:
    GACCGAGCGCCGGA
    
"""

def PathToGenome(path):
    genome = list(path[0])
    for item in path[1:]:
        genome.append(item[-1])
    out = "".join(genome)  
    return out 

def GappedPathToGenome(Patterns, k, d):
    first_pat = [x[:k] for x in Patterns]
    last_pats = [x[k+1:] for x in Patterns]
    prefix_string = PathToGenome(first_pat)
    suffix_string = PathToGenome(last_pats)
    
    for i in range(k+d+1, len(prefix_string)):
        if prefix_string[i] != suffix_string[i-k-d]:
            return "INVALID"
        
    output = prefix_string + suffix_string[-k-d:]
    return output


# data = "ACAGC|GCGAA CAGCT|CGAAT AGCTG|GAATC GCTGC|AATCA".split(" ")
# # print(data)
# out = GappedPathToGenome(data, 5, 1)
# print(out)

p2 = "./data/dataset_6206_4 (2).txt"
with open(p2, "r") as file:
    data = file.readlines()[1].split(" ")


with open("./file10.txt", "w") as file:
    file.write(GappedPathToGenome(data, 50, 200))