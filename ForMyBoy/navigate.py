# get file to be navigated
file1 = input("Enter the first file name: ")

# Opne file in read mode
my_file = open(file1,"r")

# Read data from file
data = my_file.read()

# Clean up file and remove \n and replace with ' ' and then split on "."
read_into_list = data.replace('\n',' ').split(".")

# get length of the list
lines = len(read_into_list)
lines = lines - 1
print("The file has %2d lines." % lines)

# Get the line the user wants to look at
pick =int(input("Enter the line you wish to see or 0 to exit: "))

# While the user has not picked 0, do the loop
while(pick != 0):
    print("This is the line you chose: ",pick)
    line = pick-1
    print(read_into_list[line])
    print('\n')
    pick =int(input("Enter the line you wish to see or 0 to exit: "))
if pick == 0:
    print("Thank you for using the navigator.  This application is closing.")

my_file.close()