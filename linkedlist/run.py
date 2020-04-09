


import re
import requests

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
s = "next nothing is (\d+)"

def solve(n):
    while n is not None:
        r = requests.get(url, params={"nothing" :n})
        print(r.text)
        print(r.cookies)
        if r.text is "Yes. Divide by two and keep going.":
            n /= 2
            continue
        m = re.search(s, r.text)
        if m is not None:
            n = m.group(1)
        else:
            n = None
        print("'{}'".format(n))



first = 12345

solve(first)
