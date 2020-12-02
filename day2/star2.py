f = open("input.in", "r")
count=0
for x in f:
    policy, word = x.split(": ")
    number, letter = policy.split(" ")
    lower, upper = number.split("-")
    
    if (word[int(lower)-1] == letter and word[int(upper)-1] != letter) or (word[int(lower)-1] != letter and word[int(upper)-1] == letter):
        count+=1
print(count)
f.close()