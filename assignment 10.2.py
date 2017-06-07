name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for time in name:
	words = time.split()
	for word in words:
		counts[word] = counts.get(word,0)+1

lst=list()
for key, val in counts.items():
	lst.append( (val, key) )
lst.sort(reverse=True)
for val, key in lst[:10]:
	print key, val
	
	
	if not time.startswith("From") : continue