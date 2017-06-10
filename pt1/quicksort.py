# PROGRAMMING ASSIGNMENT 3:
# STANFORD ALOGRITHMS PT 1 COURSERA

# Note:
# There's a weird edge case where if initial end is not length of array - 1 and for loop doesnt go to end + 1,
# the sort is not complete. Both cannot be removed either. It likely has something to do with the recursion at
# some level

# Psuedo code
# 
# def Quicksort(array, start index, end index):
#    if array length < 2 return
#
#    choose pivot (assume its first element)
#    partition(array, pivot, end index)
#    quicksort(array, start index, pivot -1)
#    quicksort(array, pivot + 1, end index)
#
#    return array
#
#
#
# def partition(array, start index, end index):
#
#    pivot = array[start index]
#    i, j = start index + 1
# 
#    for j to end index + 1: //idk why i need + 1 but it fails to properly sort if this + 1 and end = len - 1 are not set
#         if array[j] < pivot: do nothing/continue
# 
#         else if array[j] > pivot:
#              swap array[j] and array[i]
#              i++
#    end loop
#    swap array[start] (aka pivot) and array[i - 1]
#    return i - 1
# 
# 
# 
# // picks median of 3 random indexs
# def choose_pivot(array, start index, end index):
# 
#    rand1, rand2, rand3 = random number between start index end index
# 
#    find median of array @ rands
#    swap array[start] and array[median]

from random import randrange

def quicksort(array, start=None, end=None):
     # exception handling if start and end = None/ are not passed in
     if start == None: start = 0
     if end == None: end = len(array) - 1

     if start >= end: return # base case only 1 element to sort
     
     # to run w/ pivot always as first element comment out below choose_pivot call
     choose_pivot(array, start, end)
     pivot = partition(array, start, end)

     quicksort(array, start, pivot - 1)
     quicksort(array, pivot + 1, end)

     return array




def partition(array, start=None, end=None):
     # !!!!! add exception handling if start and end = None/ are not passed in !!!!
     pivot = array[start]
     i = start + 1; #j = start + 1

     for j in range(i, end+1):
          if array[j] > pivot:
               continue
          elif array[j] < pivot:
               array[j], array[i] = array[i], array[j]
               i = i + 1
     
     array[start], array[i - 1] = array[i - 1], array[start]
     return i-1



# picks median of 3 random indexes
def choose_pivot(array, start, end):
     rand1 = randrange(start, end); rand2 = randrange(start, end); rand3 = randrange(start, end)
     
     # rand2 is median
     if array[rand1] <= array[rand2] <= array[rand3] or array[rand3] <= array[rand2] <= array[rand1]:
          array[start], array[rand2] = array[rand2], array[start]
     # rand1 is median
     elif array[rand2] <= array[rand1] <= array[rand3] or array[rand3] <= array[rand1] <= array[rand2]:
          array[start], array[rand1] = array[rand1], array[start]
     # rand3 is median
     elif array[rand1] <= array[rand3] <= array[rand2] or array[rand2] <= array[rand3] <= array[rand1]:
          array[start], array[rand3] = array[rand3], array[start]
     # return




def run():
     with open('mergesort.txt') as f:
          arr = []
          for line in f:
               i = int(line)
               arr.append(i)
     nls = quicksort(arr)
     rand1 = randrange(10,20)
     print nls, rand1
# ls = [3, 1, 7, 5, 8, 2, 6, 4]
# end = len(ls) - 1
# nls = quicksort(ls, 0, end)
# print nls
run()