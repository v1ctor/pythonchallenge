import gzip
import difflib
from PIL import Image
import io

first = []
second = []
with gzip.open("deltas.gz", "rb") as f:
    content = f.read()
    content = content.decode("utf-8")
    rows = content.split("\n")
    tuples = list(map(lambda x: (x[:53], x[56:]), rows))
    first, second = zip(*tuples)

compare = difflib.Differ().compare(first, second)

b1 = b''
b2 = b''
b3 = b''

for line in compare:
    bs = bytes.fromhex(line[2:].strip())
    if line[0] == '+':
        b1 += bs
    elif line[0] == '-':
        b2 += bs
    else:
        b3 += bs

Image.open(io.BytesIO(b1)).show()
Image.open(io.BytesIO(b2)).show()
Image.open(io.BytesIO(b3)).show()

