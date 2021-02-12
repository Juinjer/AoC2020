import math
f = open("input4.in","r")
arr = [x.strip() for x in f]
def getID(arr):
    idd = []
    for x in arr:
        rowmax = 127
        rowmin = 0
        cmax = 7
        cmin = 0
        for i in range(len(x)):
            if x[i]=='F':
                rowmax = math.floor(rowmax-(rowmax-rowmin)/2)
            elif x[i]=='B':
                rowmin = math.ceil(rowmin+(rowmax-rowmin)/2)
            elif x[i]=='L':
                cmax = math.floor(cmax-(cmax-cmin)/2)
            elif x[i]=='R':
                cmin = math.ceil(cmin+(cmax-cmin)/2)
        idd.append(rowmax*8+cmax)
    return idd

seats = sorted(getID(arr))
for i in range(len(seats)-1):
    if seats[i]==seats[i+1]-2:
        print(seats[i]+1)