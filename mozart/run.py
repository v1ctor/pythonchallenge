from PIL import Image, ImageChops

img = Image.open("mozart.gif")

w, h = img.size

for col in range(h):
    box = 0, col, w, col + 1
    row = img.crop(box)
    b = row.tobytes()
    i = b.index(195)
    row = ImageChops.offset(row, -i)
    img.paste(row, box)

img.show()