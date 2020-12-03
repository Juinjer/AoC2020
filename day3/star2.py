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
def var_slope(right, down, arr):
    counter = 0
    d=0
    r=0
    while(d<len(arr)):
        if arr[d][r]=='#':
            counter+=1
        d+=down
        r+=right
        r%=len(arr[0])
    return counter
print(var_slope(1,1,arr),var_slope(3,1,arr),var_slope(5,1,arr),var_slope(7,1,arr),var_slope(1,2,arr))
print(var_slope(1,1,arr)*var_slope(3,1,arr)*var_slope(5,1,arr)*var_slope(7,1,arr)*var_slope(1,2,arr))