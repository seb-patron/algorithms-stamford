# BELOW IS RECURSIVE kosaraju that works
# THESE GLOBAL VARIABLES MUST BE UNCOMMENTED FOR BELOW TO WORK
import random

def kosaraju(graph):
     # start_node = random.choice(graph.keys())
     visited = dict()
     stack = myStack()
     n = len(graph)-1
     while n > 1:
          DFS(graph, visited, n, stack)
          n = n -1
     
     print (stack.get())

     rev = reverseGraph(graph)

     scc = list()
     visited = dict()

     print ('this is graph:', graph)
     print ('this is reversed', rev)

     while stack.size() > 0:
          node = stack.pop()

          if node not in visited:
               DFS_stack = myStack()
               DFS(rev, visited, node, DFS_stack)
               print ('stack from dfs that is a scc is', DFS_stack.get())
               ls = list()
               while DFS_stack.size() > 0:
                    x = DFS_stack.pop()
                    ls.append(x)
          else:
               continue
          scc.append(ls)

     print ('\nscc is', scc)
def DFS(graph, marked, node, stack):
     # if node not in marked: stack.push(node)
     marked[node] = True
     
     for neighbor in graph[node]:
          if neighbor not in marked:
               # marked[node] = True
               DFS(graph, marked, neighbor, stack)
     if node not in stack.get():
          stack.push(node)


def reverseGraph(graph):
     reversed_graph = dict()
     for node in graph:
          # print 'node in graph loop, current node:',node
          for edge in graph[node]:
               if edge not in reversed_graph: reversed_graph[edge] = list()
               reversed_graph[edge].append(node)
     
     for node in graph:
          if node not in reversed_graph:
               reversed_graph[node] = []
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



# g = {1: [4], 2: [8], 3: [6], 4: [7], 5: [2], 6:[9], 7: [1], 8: [5, 6], 9: [7, 3]}
# print (g)
# # recursive_scc(g, 1)
# kosaraju(g)

# print ('\nNow rnning test2')
# g2 = importGraph('./testcases/test2.txt')
# kosaraju(g2)

print ('\n now rinning test 5')
g3 = importGraph('./testcases/test5.txt')
kosaraju(g3)


# Answer: 3,3,3,0,0