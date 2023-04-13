"""
Code Challenge: Solve the Eulerian Cycle Problem.

     Input: The adjacency list of an Eulerian directed graph.
     Output: An Eulerian cycle in this graph.


Sample Input:
    0: 3
    1: 0
    2: 1 6
    3: 2
    4: 2
    5: 4
    6: 5 8
    7: 9
    8: 7
    9: 6

Sample Output:
    6 8 7 9 6 5 4 2 1 0 3 2 6

"""

from random import randint


# Reading data in the specific format provided
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

def find_eulerian_cycle(graph):
    vertices = graph
    start = []

    maxGraph = max(list(graph.keys()), key=int)
    start_vertex = randint(0, int(maxGraph))
    start.append(list(vertices.keys())[start_vertex])

    # print(start)

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




# p1 = "./testfile.txt"

# data_dict = read_data(p1)
# print(" ".join(find_eulerian_cycle(data_dict)))

p2 = "./data/dataset_203_2 (3).txt"
data_dict2 = read_data(p2)
with open("./file6.txt", "w") as file:
    file.write(" ".join(reversed(find_eulerian_cycle(data_dict2))))
