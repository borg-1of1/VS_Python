file1 = input("Enter the input file name: ")

# \t is the way to define a tab
with open(file1,'r') as f1:
    print("Name" + "\t" + "\t" + "Hours" + "\t" + "Total Pay" +"\n")
    for line in f1:
        words = line.split()
        pay = float(words[2]) * float(words[1])
        paid = "{:.2f}".format(pay)
        print(words[0] + "\t" + "\t" + words[1]+ "\t" + str(paid))
f1.close()

