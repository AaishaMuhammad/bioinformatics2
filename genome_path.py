data = "AGCAGATC GCAGATCA CAGATCAT AGATCATC GATCATCG ATCATCGG".split()

def PathToGenome(path):
    genome = list(path[0])
    for item in path[1:]:
        genome.append(item[-1])
    out = "".join(genome)  
    return out  

print(PathToGenome(data))
if "AGCAGATCATCGG" == PathToGenome(data):
    print(True)
