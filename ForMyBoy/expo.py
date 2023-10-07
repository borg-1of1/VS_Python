"""
File: expo.py
Project 11.3

Defines a function to raise a number to a given power.
The complexity is O(n), where n is the exponent.
"""

def expo(base, exponent):
    # Write your function here
    l=1
    while(l <= exponent):
        if l == 1:
            num = base
            l = l+1
        else:
            num = num * base
            l = l+1


def main():
    """Tests with powers of 2."""
    for exponent in range (5):
        print(exponent, expo(2, exponent))

if __name__ == "__main__":
    main()
