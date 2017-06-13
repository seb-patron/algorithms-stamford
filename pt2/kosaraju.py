# below imports and recursion limit increase are based on couresera forum recomendation
# from resource import setrlimit
# from sys import setrecursionlimit
# setrecursionlimit(80000)
# # setrlimit(resource.RLIMIT_STACK, (10**10, 10**10))
# sys.setrecursionlimit(1500)


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

s = myStack()
s.push(1)
s.push(2)
s.push(3)
print s.get()
print s.size()
print s.pop()
print s.get()