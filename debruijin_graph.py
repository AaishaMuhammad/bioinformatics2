def kmer_generator(k, text):
    kmers = []
    for i in range(len(text)-k+1):
        kmers.append(text[i:i+k])
    return kmers

def node_generator(k, text):
    nodes = []
    for i in range(len(text)-k+1):
        nodes.append(text[i:i+(k-1)])
    return nodes

def Overlap(kmers, nodes):
    adj_list = {}
    for node in nodes:
        temp = []
        for kmer in kmers:
            if kmer[:-1] == node:
                temp.append(kmer[1:])
        adj_list[node] = " ".join(temp)
    return adj_list
            
def OutputFormat(txt):
    out = []
    for key, value in txt.items():
        out.append(f"{str(key)}: {str(value)}")
    return "\n".join(out)



# data = "ACGTGTATA"
# print(OutputFormat(Overlap(kmer_generator(3, data), node_generator(3, data))))


data2 = open("./data/dataset_199_6 (1).txt").read().split()

with open("./file4.txt", "w") as file:
    file.write(OutputFormat(Overlap(kmer_generator(12, data2[1]), node_generator(12, data2[1]))))