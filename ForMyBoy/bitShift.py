startingNum = int(input("Enter the initial number: "))
numberShift = int(input("Enter the number of bits to shift: "))

rightShifted = startingNum>>numberShift

print("The result of shifting {} right by {} bits is: {}.".format(startingNum,numberShift,rightShifted))

leftShifted = startingNum<<numberShift

print("The result of shifting {} left by {} bits is: {}.".format(startingNum,numberShift,leftShifted))


# String and charater shifting
# Function for rotating left.  Takes in a string and number of characters to shift.  Returns the shifted string.
def leftShiftString(string, n):
    # converts the input string to a character list
    charList = list(string)
    # splits the character list at the indicate position 
    leftRotate = charList[n:]+charList[:n]
    # rejoins the split list after swapping positions
    leftRotatedString = "".join(leftRotate)
    # retuns the new string to the caller
    return leftRotatedString

# Function for rotating right.  Takes in a string and number of characters to shift.  Returns the shifted string.
def rightShiftString(string, n):
    charList = list(string)
    rightRotate = charList[-n:]+charList[:-n]
    rightRotatedString = "".join(rightRotate)
    return rightRotatedString

text = (input("Enter a message: "))
shift = int(input("Enter the distance: "))

leftShift =  leftShiftString(text,shift)
rightShift = rightShiftString(text,shift)

print("This is what happens when you shift '{}' left by {} places: {}.".format(text,shift,leftShift))
print("\n")
print("This is what happens when you shift '{}' right by {} places: {}.".format(text,shift,rightShift))

print(leftShift)
print("\n")
print(rightShift)