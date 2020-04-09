



f = open("input.txt")

for s in f.readlines():
    for ch in s:
        if ord(ch) >= 97 and ord(ch) <= 122:
            print(ch)
