arr = [x.strip() for x in open("test7.in","r")]
dic = dict()
for i in range(len(arr)):
    arr[i]=arr[i].split(" contain ")
    dic[arr[i][0]]=arr[i][1].split(", ")
    
def updaterec(dic):
    for key,val in dic:
        for x in val:
            if x.includes("no"):
                return 0
            elif x.includes("shiny gold"):
                return 1
            else: return x

def getVal(dic, arr):
    for x in arr:
        if "no" in x:
            return 0
        elif "shiny gold" in x:
            return 1
        else: return 1+getVal(dic,arr)
print(getVal(dic,['light red bags']))