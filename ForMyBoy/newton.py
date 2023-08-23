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
# Initialize the tolerance
TOLERANCE = 0.000001
# this is the Newton's function
def newton(x,estimate):
   estimate = (estimate + x / estimate) / 2
   difference = abs(x - estimate ** 2)
   if difference <= TOLERANCE:
      return estimate
   else:
      return newton(x,estimate)

def main():
   while True:
      x = input("Enter a positive number or enter/return to quit: ")
      if x == "":
         break
      x = float(x)
      estimate = 1.0
      print("\nThe program's estimate is", newton(x,estimate))
      print("Python's estimate is ", math.sqrt(x))
      print("\n")
if __name__ == "__main__":
    main()