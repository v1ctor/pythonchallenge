from PIL import Image
import re

im = Image.open("oxygen.png")
pix = im.load()
print(im.size)
result = ""
for i in range(0, im.size[0], 7):
        c = pix[i, 45]
        print(c)
        if c[0] == c[1] and c[1] == c[2]:
            result += chr(c[0])

print(result)

nums = re.findall("\d+", result)

print("".join(map(chr, map(int, nums))))
