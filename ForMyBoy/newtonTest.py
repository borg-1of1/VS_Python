import math

def newton(x, estimate):   
   while True:
      # Initialize the tolerance and estimate
      tolerance = 0.000001
      # estimate = 1.0

      # Perform the successive approximations
      while True:
         estimate = (estimate + x / estimate) / 2
         difference = abs(x - estimate ** 2)
         if difference <= tolerance:
            break


      # Output the result
      print("The program's estimate is", estimate)
      print("Python's estimate is", math.sqrt(x))
      
      n = input("Enter a positive number or enter/return to quit: ")
      if n=='':
         break
      else:
         n = float(n)
         newton(n, 1)
   


def main():
   n = input("Enter a positive number or enter/return to quit: ")
   n = float(n)
   newton(n, 1)

if __name__ == "__main__":
   main()