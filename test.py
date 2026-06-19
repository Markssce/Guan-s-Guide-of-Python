from PIL import Image 
im = Image.open("/Users/mercury/Documents/Python/Chapter_6/pic.png") 
im.show()
im = im.convert("L")
im.show()
im.save(r"/Users/mercury/Documents/Python/Chapter_6/pic-Tulips.png")