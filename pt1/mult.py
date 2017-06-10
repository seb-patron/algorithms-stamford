# PROGRAMMING ASSIGNMENT 1:
# STANFORD ALOGRITHMS PT 1 COURSERA

# In this programming assignment you will implement one or more 
# of the integer multiplication algorithms described in lecture.

# To get the most out of this assignment, your program should 
# restrict itself to multiplying only pairs of single-digit 
# numbers. You can implement the grade-school algorithm if you 
# want, but to get the most out of the assignment you'll want to 
# implement recursive integer multiplication and/or Karatsuba's algorithm.

# So: what's the product of the following two 64-digit numbers?

# 3141592653589793238462643383279502884197169399375105820974944592

# 2718281828459045235360287471352662497757247093699959574966967627



def karatsuba(num1, num2):
     if num1 < 10 or num2 < 10:
          return num1 * num2
     
     n = max(len(str(num1)), len(str(num2))); n2 = n / 2
     a = num1 / (10**n2); b = num1 % (10**n2)
     c = num2 / (10**n2); d = num2 % (10**n2)

     ac = karatsuba(a, c); bd = karatsuba(b, d)

     ad_plus_bc = karatsuba(a+b, c+d) - ac- bd

     return (ac*(10**n)) + ((ad_plus_bc) * (10**n2)) +bd

i = 1234
j = 5678

k = 3141592653589793238462643383279502884197169399375105820974944592
l = 2718281828459045235360287471352662497757247093699959574966967627

print karatsuba(k, l)
# print high, low
# print ans

# print length