import shutil

copyFromFile = input("Enter the input file name: ")
copyToFile = input("Enter the output file name: ")

# Method 1 using shutil - Don't think this is in what you have learned
# shutil.copyfile(copyFromFile,copyToFile)

# Method 2 - Reading from one file into memory and then writing to the other until all data has been copied
# Open file
copyFrom = open(copyFromFile,'r')
# Read contents to end of file
copyText = copyFrom.readlines()
# Close file
copyFrom.close()

# Open file that will have data added to it
copyTo = open(copyToFile,'w')

# iterate through each line of text and write to the file
line = 1
for lineOfText in copyText:
    lineNumber = str(line)
    copyTo.write(lineNumber + " ")
    copyTo.write(lineOfText)
    line = line + 1

# Close the file when done
copyTo.close()
