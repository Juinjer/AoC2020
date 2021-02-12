arr = [x.strip() for x in open("input6.in","r")]
arr.append('')
test = set()
count = 0
for x in arr:
    if x == '':
        count+=len(test)
        test = set()
    else:
        for y in x:
            test.add(y)
print(count)