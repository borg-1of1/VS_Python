"""
File: reverse.py
Project 11.2

Defines a function to reverse the elements in a list.
"""

def reverse(lyst):
    # Define your reverse function here without using the inbuilt reverse() method.
    reverser = slice(None,None,-1)
    lyst = lyst[reverser]
    return lyst
        

def main():
    """Tests with two lists."""
    lyst = list(range(4))
    lyst = reverse(lyst)
    print(lyst)
    lyst = list(range(3))
    lyst = reverse(lyst)
    print(lyst)

if __name__ == "__main__":
    main()
