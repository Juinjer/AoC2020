arr = [x.strip() for x in open("input6.in","r")]
arr.append('')
res = set()
same = True
count = 0
for x in arr:
    if x == '': 
        if same == True:
            count+=len(res)
        res = set()
        same = True
    else:
        if len(res)==0:
            for y in x:
                res.add(y)
        else:
            res = res.intersection(set(x))
            if len(res) ==0:
                same= False
print(count)