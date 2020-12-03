f = open("input3.in","r")
inp = []
arr = []
for x in f:
    inp.append(x)
c = -1
for i in inp:
    arr.append([])
    c+=1
    for j in i:
        if j=='\n':
            continue
        else:
            arr[c].append(j)
counter = 0
d=0
r=0
while(d<len(arr)):
    if arr[d][r]=='#':
        counter+=1
    d+=1
    r+=3
    r%=len(arr[0])
print(counter)