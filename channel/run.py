
from zipfile import ZipFile, ZipInfo
import re

start = "start from (\d+)"
nothing = "Next nothing is (\d+)"

with ZipFile("channel.zip", 'r') as obj:
    data = obj.read("readme.txt").decode("utf-8") 
    m = re.search(start, data)
    n = m.group(1)
    while n is not None:
        name = "{}.txt".format(n)
        print(obj.getinfo(name).comment.decode("utf-8"), end="")
        data = obj.read(name).decode("utf-8")
        m = re.search(nothing, data)
        if m is not None:
            n = m.group(1)
        else:
            n = None

