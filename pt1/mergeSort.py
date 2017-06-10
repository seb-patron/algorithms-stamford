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

def mergeSorty(array):
     mid = int(len(array))/2
     if len(array) < 2:
          return array
     a = mergeSorty( array[ : mid] )
     b = mergeSorty( array[mid :] )

     result = list()
     i = 0; j = 0 
     while i < len(a) and j < len(b):
          if a[i] < b[j]:
               result.append(a[i])
               i = i + 1
          else:
               result.append(b[j])
               j = j + 1

     result += a[i:]
     result += b[j:]

     return result


ls = [1, 3, 2, 5, 8, 7, 6, 4]
nls = mergeSorty(ls)
print nls