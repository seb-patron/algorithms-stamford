# PROGRAMMING ASSIGNMENT 4:
# STANFORD ALOGRITHMS PT 1 COURSERA

# Breadth First Search

# Pseudo code

# graph = dict who's keys are nodes, and values are a list of connected nodes
# marked = dict that contains all nodes that are connected (or found), and value true
# if node is not found it will not be in marked
# 
# 
# BFS(graph, starting node n):
# 
#    que = que data structure
#    add n to que
# 
#    while length of que > 0
# 
#         current_node = que.pop
#         for node in graph[current_node]:
# 
#              if node not in marked:
#                   que.add(node)
#                   marked[node] = True

import random
marked = dict()

def breadthFirstSearch(graph, start_node=None):
     if start_node == None: start_node = random.choice(graph.keys())
     que = myQueue(); que.enqueue(start_node)

     while que.size() > 0:

          current_node = que.dequeue()
          for node in graph[current_node]:

               if node not in marked:
                    que.enqueue(node)
                    marked[node] = True

     return True




# The following is modified code from stackoverflow to implement a queue in python
class myQueue:
     def __init__(self):
         self.container = []  # inits queue with an empty list set as container

     def isEmpty(self):
         return self.size() == 0   # checks if queue is empty. returns True or False

     def enqueue(self, item):
         self.container.append(item)  # appending to the *container*, not the instance itself.

     def dequeue(self):
         return self.container.pop(0)  # pops from first element in the container

     def size(self):
         return len(self.container)  # length of the container

     def get(self):
          return self.container    # returns container



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
     graph = importGraph('graph.txt')
     # marked = dict()
     # runs repeated trials to find min cut
     # copiedGraph = copy.deepcopy(graph) # copies graph for repeat trials
     breadthFirstSearch(graph, 1)
     print marked
     # print "MinCut is ", min(mincuts)





run()