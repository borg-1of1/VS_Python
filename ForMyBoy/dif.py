import difflib

file1 = input("Enter the first file name: ")
file2 = input("Enter the second file name: ")

f1 = open(file1)
f2 = open(file2)

lines1 = f1.readlines()
lines2 = f2.readlines()

i = 0

f1.seek(0)
f2.seek(0)

for line1 in f1:
    if lines1[i] != lines2[i]:
        print("no")
        print(lines1[i]+"\n"+ lines2[i]+"\n")
        exit(0)
    i = i+1
else:
    print("yes")

f1.close()
f2.close()
