import re
fhand = open('regex_sum_214351.txt')
testr = fhand.read()
prse = re.findall('([0-9]+)', testr)
sum = 0
for i in prse:
    sum += int(i)
print sum
