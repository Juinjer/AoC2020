arr= [line.strip() for line in open('input4.in', 'r').readlines()]
fields={'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
passport = {}
count = 0
for line in arr:
        if not line:
            if fields.issubset(set(passport.keys())):
                count += 1
            passport = {}
        else:
            for pair in line.split(' '):
                k, v = pair.split(':')
                passport[k] = v
if fields.issubset(set(passport.keys())):
    count += 1
print(count)