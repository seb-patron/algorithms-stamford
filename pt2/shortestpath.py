# PROGRAMMING ASSIGNMENT 4:
# STANFORD ALOGRITHMS PT 1 COURSERA

# Shortest path via: Breadth First Search
# finds shortest path from start node to end node
# if no node passed as end node, finds all paths from start node, and returns dict of all distances

# Pseudo code

# graph = dict who's keys are nodes, and values are a list of connected nodes
# distance_from_start = dict that contains all nodes that are connected (or found), and value of distance from start node
# 
# 
# shortestpath(graph, starting node n, ending node end=NULL):
# 
#    que = que data structure
#    add n to que
#    distance_from_start = dict()
#    distance_from_start[n] = 0
# 
#    while length of que > 0
# 
#         current_node = que.pop
#         for node in graph[current_node]:
# 
#              if node not in marked:
#                   que.add(node)
#                   distance_from_start[node] = distance_from_start[node] + 1
#                   if node == end: return distance_from_start[end]


marked = dict()

def shortestPath(graph, start_node, end_node=None):
     # if end_node == None: end_node = -1

     que = myQueue(); que.enqueue(start_node)
     distance_from_start = dict()
     distance_from_start[start_node] = 0

     while que.size() > 0:
          current_node = que.dequeue()

          for node in graph[current_node]:
               if node not in distance_from_start:
                    que.enqueue(node)
                    distance_from_start[node] = distance_from_start[current_node] + 1
                    if node == end_node: return distance_from_start[node]

     return distance_from_start




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
     answer = shortestPath(graph, 1)
     print answer
     # print "MinCut is ", min(mincuts)





run()