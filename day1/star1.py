f =  open("input.in","r")
arr = []
for x in f:
    arr.append(int(x))
f.close()

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i]+arr[j]==2020:
            print(arr[i],arr[j])
            print(arr[i]*arr[j])