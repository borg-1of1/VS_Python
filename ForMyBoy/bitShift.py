startingNum = int(input("Enter the initial number: "))
numberShift = int(input("Enter the number of bits to shift: "))

rightShifted = startingNum>>numberShift

print("The result of shifting {} right by {} bits is: {}.".format(startingNum,numberShift,rightShifted))

leftShifted = startingNum<<numberShift14

print("The result of shifting {} left by {} bits is: {}.".format(startingNum,numberShift,leftShifted))
