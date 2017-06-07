import json
import urllib

service = raw_input('Enter address: ')

url = urllib.urlopen(service).read()
info = json.loads(url)

solution = []

for i in range (0, 50, 1):
    solution.append(info['comments'][i]['count'])
print sum(solution)
