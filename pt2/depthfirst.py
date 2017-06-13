# PROGRAMMING ASSIGNMENT 4:
# STANFORD ALOGRITHMS PT 2 COURSERA

# Depth First Search

# Pseudo code

# graph = dict who's keys are nodes, and values are a list of connected nodes
# marked = dict that contains all nodes that are connected (or found), and value true
# if node is not found it will not be in marked
# 
# recursiveDFS(graph, marked, start_node):
# 
#    current_node = start_node
#    marked[current_node] = True
#    
#    for node in graph[current_node]:
#         if node not in marked:
#              recursiveDFS(graph, marked, node)

# iterativeDFS(graph, start_node)
# 
#    stack = myStack()
#    stack.push(start_node)
#    marked[start_node] = True
#    while stack length > 0
#         current_node = stack.pop()
#         for node in graph[current_node]:
#              if node not in marked:
#                   marked[node] = True
#                   stack.push(node)
import random
marked = dict()

def recursiveDFS(graph, marked, node):
     marked[node] = True
     for neighbor in graph[node]:
          if neighbor not in marked:
               # marked[node] = True
               recursiveDFS(graph, marked, neighbor)

def iterativeDFS(graph, start_node=None):
     if start_node == None: start_node = random.choice(graph.keys())

     stack = myStack()
     stack.push(start_node)
     marked[start_node] = True

     while stack.size() > 0:
          current_node = stack.pop()
          for node in graph[current_node]:
               if node not in marked:
                    marked[node] = True
                    stack.push(node)

# The following is modified code from stackoverflow to implement a queue in python
class myStack:
     def __init__(self):
         self.container = []  # inits queue with an empty list set as container

     def isEmpty(self):
         return self.size() == 0   # checks if queue is empty. returns True or False

     def push(self, item):
         self.container.append(item)  # appending to the *container*, not the instance itself.

     def pop(self):
         return self.container.pop()  # pops from first element in the container

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
     # recursiveDFS(graph, marked, 1)
     iterativeDFS(graph)
     print marked
     # print "MinCut is ", min(mincuts)





run()