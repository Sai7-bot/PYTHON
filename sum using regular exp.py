import re
fname = input("Enter file name: ")
s = 0
fh = open(fname)
for line in fh:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        s = s + int(number)
print(s)
