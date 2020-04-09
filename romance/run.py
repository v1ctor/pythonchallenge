import requests
import re
import bz2
from urllib.parse import unquote_to_bytes
from xmlrpc.client import ServerProxy


url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
s = "next busynothing is (\d+)"

def solve(n):
    result = ""
    while n is not None:
        r = requests.get(url, params={"busynothing" : n})
        result += r.cookies["info"]
        if r.text is "Yes. Divide by two and keep going.":
            n /= 2
            continue
        m = re.search(s, r.text)
        if m is not None:
            n = m.group(1)
        else:
            n = None
    print(result)




first = 12345

r = "BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90"

print(bz2.decompress(unquote_to_bytes(r.replace("+", " "))))

conn = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")

print(conn.phone("Leopold"))


# solve(first)

