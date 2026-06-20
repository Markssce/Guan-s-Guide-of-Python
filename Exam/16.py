import matplotlib.pyplot as plt
from PIL import Image
try:
    im = Image.open("/Users/mercury/Documents/Python/exam_data/Tulips.jpg")
    im = im.convert("L")
    w, h = im.size
    hd = [0] * w * h
    n = 0

    for i in range(w):
        for j in range(h):
            pixel = im.getpixel((i, j))
            hd[n] = pixel
            n = n+1
    # print(hd)
    plt.hist(hd, 256)
    plt.show()
    
except FileNotFoundError:
    print("File not found")
finally:
    print("Over!")