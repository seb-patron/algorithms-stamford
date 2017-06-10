# PROGRAMMING ASSIGNMENT 4:
# STANFORD ALOGRITHMS PT 1 COURSERA

# Random Contraction Algorithm
# Your task is to code up and run the randomized contraction 
# algorithm for the min cut problem and use it on the above 
# graph to compute the min cut. (HINT: Note that you'll have 
# to figure out an implementation of edge contractions. 
# Initially, you might want to do this naively, creating a new 
# graph from the old every time there's an edge contraction. 
# But you should also think about more efficient implementations.) 
# (WARNING: As per the video lectures, please make sure to run 
# the algorithm many times with different random seeds, and 
# remember the smallest cut that you ever find.)

# appends minimum cut found in each iteration to a list, then selects smallest element is list and mincut

# Pseudo Code
# 
# 
# mincuts = list //keeps track of all mincuts found throughout repeated tests
# 
# def kargermincut(graph):
# 
#    while length of graph > 2:
#         a = random node in graph
#         b = random node in list of nodes in a //makes sure the nodes are actually connected
#         contract(graph, a, b)
# 
#    append result to mincut
# 
# 
# // contracts edges into a, removes b
# def contract(graph, a, b):
# 
#    for edge in graph[b]:
#         if edge is not a: //makes sure no self loops are added
#              add edge to graph[a]
#         remove edge from graph[b]
#         
#         if edge is not a:
#              add a to node[edge]
#    
#    del graph[b]




import random
import copy

mincuts = list()

def kargermincut(graph):
     while len(graph) > 2:
          a = random.choice(graph.keys())
          b = random.choice(graph[a])
          contract(graph, a, b)
     mincuts.append(len(graph[graph.keys()[0]]))

def contract(graph, a, b):
     for edge in graph[b]:
          # print edge
          if edge is not a:
               graph[a].append(edge)
               graph[edge].append(a)
          graph[edge].remove(b)
          # if edge != a:
          #      graph[edge].append(a)
     del graph[b]
     # print graph[a]


# imports graph as a python dict, whose values are a list of all connected nodes
def importGraph(filename):
    file = open(filename)
    graph = {}
    for line in file:
        node = int(line.split()[0])
        edges = []
        for edge in line.split()[1:]:
            edges.append(int(edge))
        graph[node] = edges
    return graph

def run():
     graph = importGraph('kargerMinCut.txt')
     trials = (len(graph) * (len(graph)- 1))/20
     print trials
     # runs repeated trials to find min cut
     for i in range(1, trials):  # we do repeated trials to find the minimum cut.
          copiedGraph = copy.deepcopy(graph) # copies graph for repeat trials
          kargermincut(copiedGraph)
     print "MinCut is ", min(mincuts)





run()