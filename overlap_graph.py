data = "CT TG TG TC TT TC".split()

def Overlap(text):
    results = {}
    for item in text:
        results[item] = " ".join([x for x in text if x[:-1] == item[1:]])
        if results[item] == "":
            results.pop(item)
    return results

def OutputFormat(txt):
    out = []
    for key, value in txt.items():
        out.append(f"{str(key)}: {str(value)}")
    return "\n".join(out)


# OutputFormat(Overlap(data))
data2 = open("./data/dataset_198_10.txt").read().split()

with open("./file3.txt", "w") as file:
    file.write(OutputFormat(Overlap(data2)))