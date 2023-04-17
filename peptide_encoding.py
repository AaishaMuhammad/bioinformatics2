"""
Code Challenge: Solve the Peptide Encoding Problem.
Peptide Encoding Problem: Find substrings of a genome encoding a given amino acid sequence.
    Input: A DNA string Text, an amino acid string Peptide, and the array GeneticCode.
    Output: All substrings of Text encoding Peptide (if any such substrings exist).

Sample Input:
    ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA
    MA

Sample Output:
    ATGGCC
    GGCCAT
    ATGGCC
"""

from collections import defaultdict

codons = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}

def protein_translator(Pattern):
    out = []
    # codons = [Pattern[i:i+3] for i in range(0, len(Pattern), 3)]
    # print(codons)

    for i in range(0, len(Pattern), 3):
        codon = Pattern[i:i+3]
        if codons[codon] == "STOP": break
        out.append(codons[codon])

    out = "".join(x for x in out)
    return out

def DnaReverse(txt):
    newtxt = list(txt)
    nucs = {
        "A":"T",
        "C":"G",
        "G":"C",
        "T":"A",
    }
    for i in range(len(txt)):
        newtxt[i] = nucs[txt[i]]
    newdna = "".join(newtxt)
    newdna = newdna[::-1]
    return newdna

def rna_converter(text):
    rna = list(text)
    for index, i in enumerate(rna):
        if i == "T": rna[index] = "U"
    rna = "".join(x for x in rna)

    return rna

def kmer_generator(k, text):
    kmers = []
    for i in range(len(text)-k+1):
        kmers.append(text[i:i+k])
    return kmers 

def peptide_encoding(text, pattern):

    kmers = kmer_generator(3*len(pattern), text)
    inverse_kmers = [DnaReverse(kmer) for kmer in kmers]
    rna_kmers = [rna_converter(kmer) for kmer in kmers]
    rna_inv_kmers = [rna_converter(kmer) for kmer in inverse_kmers]
    protein1 = [protein_translator(kmer) for kmer in rna_kmers]
    protein2 = [protein_translator(kmer) for kmer in rna_inv_kmers]
    out1 = [kmers[index] for index, i in enumerate(protein1) if i == pattern]
    out2 = [kmers[index] for index, i in enumerate(protein2) if i == pattern]

    return out1 + out2



p = "./data/genome2.txt"
with open(p, "r") as file:
    data = "".join(file.read().splitlines())


with open("./file15.txt", "w") as file:
    file.write("\n".join(x for x in peptide_encoding(data, "VKLFPWFNQY")))