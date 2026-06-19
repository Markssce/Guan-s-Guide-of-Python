from PIL import Image
im = Image.open("/Users/mercury/Documents/Python/Chapter_6/6-6.png")
im.show()

im = im.convert("L")
im = im.point(lambda x:255 if x >200 else 0)
im.show()

count1 = 0
w, h = im.size
for i in range(w):
    for j in range(h):
        pixel = im.getpixel((i, j))
        if pixel != 0:
            count1 += 1

print(count1/(w*h)*100)

