# Modify the code below
"""
File: newton.py
Project 6.1

Compute the square root of a number (uses function with loop).

1. The input is a number, or enter/return to halt the
   input process.

2. The outputs are the program's estimate of the square root
   using Newton's method of successive approximations, and
   Python's own estimate using math.sqrt.
"""


import math

def getSquare(x):   
   
   # Initialize the tolerance and estimate
   tolerance = 0.000001
   estimate = 1.0

   # Perform the successive approximations
   while True:
      estimate = (estimate + x / estimate) / 2
      difference = abs(x - estimate ** 2)
      if difference <= tolerance:
         break

   # Output the result
   print("The program's estimate is", estimate)
   print("Python's estimate is", math.sqrt(x))
   


def main():
   # Receive the input number from the user
   n = input("Enter a positive number or enter/return to quit: ")
   n = float(n)
   while True:      
      getSquare(n)
      n = input("Enter a positive number or enter/return to quit: ")
      if n=='':
         return
      else:
         n = float(n)

if __name__ == "__main__":
   main()