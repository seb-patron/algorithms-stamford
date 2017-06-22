# BELOW IS RECURSIVE kosaraju that works
# # below imports and recursion limit increase are based on couresera forum recomendation
from resource import setrlimit
# from sys import setrecursionlimit
import sys

sys.setrecursionlimit(80000)

print(sys.getrecursionlimit())
# setrecursionlimit(80000)
# setrlimit(resource.RLIMIT_STACK, (10**10, 10**10))
# sys.setrecursionlimit(1500)
import random

def kosaraju(graph):
     # start_node = random.choice(graph.keys())
     # visited = dict()
     # stack = myStack()
     n = len(graph)-1
     stack = DFS_loop(graph)
     
     print ('stack order to transverse',stack.get())

     rev = reverseGraph(graph)

     print ('rev graph', rev)
     scc = list()
     visited = dict()

     while stack.size() > 0:
          node = stack.pop()
          print ('\nthis round, visited nodes ', visited)
          print ('stack is', stack.get())
          print ('node to chck is', node)
          if node not in visited:
               DFS_stack = myStack()
               # DFS(rev, visited, node, DFS_stack)
               iterativeDFS2(rev, visited, DFS_stack, node)
               print ('stack returned from DFS that is a scc', DFS_stack.get())
               ls = list()
               while DFS_stack.size() > 0:
                    x = DFS_stack.pop()
                    ls.append(x)
          # exceoptin makes sure only new scc's are added to scc list
          else:
               continue
          scc.append(ls)


     visited = dict()

     # Makes sure every node in graph was explored for scc
     for node in graph:
          for sublist in scc:
               if node in sublist:
                    # print ("Found it!", node)
                    visited[node] = True
                    continue
          # activates if node was not added as scc, adds it as a sinlge scc it is
          if node not in visited:
               # print ("ALERT: node not found", node)
               scc.append([node])
     
     return scc

def DFS_loop(graph):
     visited = dict()
     i = len(graph)
     stack = myStack() 
     while i > 0:
          print ('dfs loop on', i)
          node = str(i)
          iterativeDFS(graph, visited, stack, node)
          # if node not in stack.get():
          #      stack.push(node)
          if node not in stack.get():
               stack.push(node)
          i = i -1
     return stack


def iterativeDFS(graph, marked, Rstack, start_node=None):
     if start_node == None: start_node = random.choice(graph.keys())

     stack = myStack()
     stack.push(start_node)
     marked[start_node] = True

     while stack.size() > 0:
          current_node = stack.pop()
          print ('current node', current_node)
          for node in graph[current_node]:
               if node not in marked:
                    marked[node] = True
                    stack.push(node)
               else:
                    if node not in Rstack.get():
                         Rstack.push(node)

def iterativeDFS2(graph, marked, Rstack, start_node=None):
     if start_node == None: start_node = random.choice(graph.keys())

     stack = myStack()
     stack.push(start_node)
     marked[start_node] = True
     if start_node not in Rstack.get(): Rstack.push(start_node)
     while stack.size() > 0:
          current_node = stack.pop()
          
          for node in graph[current_node]:
               
               if node not in marked and node not in Rstack.get(): Rstack.push(node)
               if node not in marked:
                    print ('node not in marked', node)
                    marked[node] = True
                    stack.push(node)
               # else:
               #      if node not in Rstack.get():
               #           Rstack.push(node)
def DFS(graph, marked, node, stack):
     # if node not in marked: stack.push(node)
     marked[node] = True
     
     for neighbor in graph[node]:
          if neighbor in graph:
               if neighbor not in marked and len(graph[neighbor]) > 0:
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
          node = str(line.split()[0])
          edge = str(line.split()[1])

          # if node is not in graph yet creates key and list as value
          if node not in graph:
               graph[node] = list()
          
          graph[node].append(edge)

     i = 1
     while i < len(graph):
          i += 1
          s = str(i)
          if s not in graph:
               print (s, 'not in graph')
               graph[s] = []
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


def run():
     # g = {1: [4], 2: [8], 3: [6], 4: [7], 5: [2], 6:[9], 7: [1], 8: [5, 6], 9: [7, 3]}
     # print (g)
     # # recursive_scc(g, 1)
     # ans = kosaraju(g)
     # print (ans)
     # scc_sizes = [len(scc) for scc in ans]
     # print (scc_sizes)

     print ('\nNow rnning test2')
     g2 = importGraph('./testcases/test2.txt')
     print (g2)
     ans = kosaraju(g2)
     print (ans)

     print ('\nNow rnning test3')
     g3 = importGraph('./testcases/test3.txt')
     print (g3)
     ans = kosaraju(g3)
     print (ans)
     # Answer: 3,3,1,1,0

     print ('\nNow rnning test4')
     g4 = importGraph('./testcases/test4.txt')
     print (g4)
     ans = kosaraju(g4)
     print (ans)
     # Answer: 7,1,0,0,0 
     print ('\n now rinning test 5')
     g3 = importGraph('./testcases/test5.txt')
     ans = kosaraju(g3)
     print (ans)

     # Answer: 6,3,2,1,0


# run()


def assignment1():
     g = importGraph('scc.txt')
     print (len(g))
     answer = kosaraju(g)

     scc_sizes = [len(scc) for scc in answer]

     print ('\n\n the answers found are')
     print (scc_sizes)
# Answer: 3,3,3,0,0

assignment1()