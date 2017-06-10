# implements week 1 merge sort
# Pseudocode
#
#    recursive call
#    if length of array > 1:
#         mergeSort(1st half), mergeSort(2nd half)
#
#
# merge:
#    c = outputArray a = 1st sorted Array(n/2) b = 2nd sorted Array(n/2)
#
#    i = 1; j = 1
#    for k = 1 to n
#         if a(i) < b(j):
#              c(k) = a(i)
#              i++
#         else if a(i) > b(j)
#              c(k) = b(j)
#              j++
#    end
#    return c

def sort_and_count(tup):
     array = tup[0]; count = tup[1]
     n = len(array); n2 = n / 2
     if len(array) == 1: return (array, 0) #returns a tuple with array and count of 0 as base case
     else:
          tup_b = sort_and_count((array[:n2], count))
          tup_c = sort_and_count((array[n2:], count))

          tup_d = merge_and_count_splitInv((tup_b[0], tup_c[0])) # take arrays in each tuple as argument

     return (tup_d[0], tup_b[1] + tup_c[1] + tup_d[1])

def merge_and_count_splitInv(tup):
     array1 = tup[0]; array2 = tup[1]

     result = list()
     i = 0; j = 0; count = 0 
     while i < len(array1) and j < len(array2):
          if array1[i] < array2[j]:
               result.append(array1[i])
               i = i + 1
          else:
               result.append(array2[j])
               j = j + 1
               count += len(array1) - i

     result += array1[i:]
     result += array2[j:]

     return (result, count)

def run():
     with open('mergesort.txt') as f:
          arr = []
          for line in f:
               i = int(line)
               arr.append(i)
     nls = sort_and_count((arr, 0))
     print nls[1]


# ls = [1, 3, 2, 5, 8, 7, 6, 4]
# nls = mergeSorty(ls)
# print nls

ls = [1, 3, 5, 2, 4, 6]
nls = sort_and_count((ls, 0))

print nls
run()