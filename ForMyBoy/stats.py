import statistics
from collections import Counter

lyst = [ 3,1,7,1,4,10]
n = len(lyst)

def my_mean(values,length):
    value = 0
    i = 0
    for v in values:
        value = v + value
        i = i+i
    meanCalc = value/length
    print("The mean is: ",meanCalc)

def my_mode(values):
    c = Counter(values)    
    print("The mode is: ",[k for k, v in c.items() if v == c.most_common(1)[0][1]])

def my_median(values,length):
    index = length//2
    if length% 2:
        print("The median is :",sorted(values)[index])
    print("The median is: ",sum(sorted(values)[index-1:index+1])/2)

print("The list of values is :", lyst)
my_mode(lyst)
my_median(lyst,n)
my_mean(lyst,n)

print("The easy way to calculate mean, media, and mode!")
print("The list of values is :", lyst)
print("The mode is: ",statistics.multimode(lyst))
print("The median is :",statistics.median(lyst))
print("The mode is: ",statistics.mean(lyst))
