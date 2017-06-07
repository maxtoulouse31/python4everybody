# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
numlist = list()
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    atpos = line.find('Confidence:')
    host= line[atpos+12:38]
    flost= float(host)
    numlist.append(flost)
ava = sum(numlist)/27.0
print "Average spam confidence:", ava