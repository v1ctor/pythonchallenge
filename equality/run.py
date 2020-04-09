

import re

f = open("input.txt")

data = f.read().replace('\s', '')

s = "[a-z]([A-Z]{3}[a-z][A-Z]{3})[a-z]"

m = re.findall(s, data)

for g in m:
    print(g[3], end="")

print()

