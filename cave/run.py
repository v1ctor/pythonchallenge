
from PIL import Image, ImageDraw

im = Image.open("cave.jpg")


print(im.size)

first = Image.new("RGB", (320, 240))
second = Image.new("RGB", (320, 240))


for i in range(im.size[0]):
    for j in range (im.size[1]):
        if i % 2 == 0 and j % 2 == 0:
            first.putpixel((i // 2, j // 2), im.getpixel((i, j)))

        elif i % 2 == 1 and j % 2 == 1:
            second.putpixel((i // 2, j // 2), im.getpixel((i, j)))


first.show()
second.show()

