# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
s = 0
count = 0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count + 1
    m = line.find("0")
    s = s + float(line[m:])
print("Average spam confidence:", s/count)
