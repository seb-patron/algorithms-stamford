# BELOW IS RECURSIVE kosaraju that works
# THESE GLOBAL VARIABLES MUST BE UNCOMMENTED FOR BELOW TO WORK
marked = dict()
finish_time = dict()
total_scc = list()


counter = 0

def recursive_scc(graph, start_node):
     marked = dict()
     scc_stack = myStack()
     i = len(graph)-1
     while i > 1:
          s = recursiveDFS(graph, marked, i,  scc_stack)
          i -= 1
          print s
     print finish_time
     print 'lol stack', lol_stack.get()
     lv = max(finish_time, key=finish_time.get)
     print lv, finish_time[lv]

     rev = reverseGraph(graph)
     marked2 = dict()
     # while len(finish_time) > 0:
     while lol_stack.size() > 0:
          print 'made it to qhile lolstack call'
          ls = list()
          # node = max(finish_time, key=finish_time.get)
          # del finish_time[node]
          node = lol_stack.pop()
          recursiveDFS2(rev, marked2, node)

          for n in marked2:
               if n in finish_time:
                    ls.append(n)
                    del finish_time[n]
          total_scc.append(ls)


def recursiveDFS(graph, marked, node, stack=None):
     if stack == None: stack = myStack()
     global counter
     marked[node] = True
     for neighbor in graph[node]:
          if neighbor not in marked:
               # marked[node] = True
               recursiveDFS(graph, marked, neighbor, stack)

     if node not in finish_time: lol_stack.push(node)
     counter = counter + 1
     finish_time[node] = counter
     stack.push(node)
     
     return stack.get()

def recursiveDFS2(graph, marked, node, stack=None):
     if stack == None: stack = myStack()
     marked[node] = True
     for neighbor in graph[node]:

          if neighbor not in marked:

               if neighbor in graph:
                    recursiveDFS2(graph, marked, neighbor, stack)
               else:
                    total_scc.append([neighbor])
                    marked[neighbor] = True

     # if node not in finish_time: lol_stack.push(node)
     # counter = counter + 1
     # finish_time[node] = counter
     stack.push(node)
     
     return stack.get()

def reverseGraph(graph):
     reversed_graph = dict()
     for node in graph:
          # print 'node in graph loop, current node:',node
          for edge in graph[node]:
               if edge not in reversed_graph: reversed_graph[edge] = list()
               reversed_graph[edge].append(node)

     return reversed_graph

def importGraph(filename):
     file = open(filename)
     graph = {}
     for line in file:
          node = int(line.split()[0])
          edge = int(line.split()[1])

          # if node is not in graph yet creates key and list as value
          if node not in graph:
               graph[node] = list()
          
          graph[node].append(edge)
     return graph

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



g = {1: [4], 2: [8], 3: [6], 4: [7], 5: [2], 6:[9], 7: [1], 8: [5, 6], 9: [7, 3]}
print g
# recursive_scc(g, 1)
lol_stack = myStack()
recursive_scc(g, 1)
print total_scc

counter = 0
lol_stack = myStack()
total_scc = list()
g2 = importGraph('./testcases/test2.txt')
print 'running test2 on g', g2
recursive_scc(g2, 1)
print total_scc

lol_stack = myStack()
counter = 0
total_scc = list()
g3 = importGraph('./testcases/test5.txt')
print 'running test3 on g', g3
recursive_scc(g3, 1)
print total_scc

# Answer: 3,3,3,0,0