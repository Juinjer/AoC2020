f = open("input.in", "r")
res = 0
for x in f:
    policy, word = x.split(": ")
    number, letter = policy.split(" ")
    lower, upper = number.split("-")
    count=0
    for i in word:
        if i==letter:
            count+=1
    if count>=int(lower) and count<=int(upper):
        res+=1

print(res)
f.close()