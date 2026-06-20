from PIL import Image 
from PIL import ImageFilter as IF
im = Image.open(r"/Users/mercury/Documents/Python/Chapter_6/6_5.png") 
# im = im.transpose(Image.FLIP_LEFT_RIGHT) # 水平反转
# im = im.convert("L") # 转换成 8 位灰度图像
im = im.point(lambda x: 225 if x > 127 else 0) # 将灰度值 127 以上的转换成 255（白），127 以下的转换成 0（黑）
# im = im.convert("RGB")
# r,g,b = im.split()
# om=Image.merge("RGB",(b,g,r))
im = im.filter(IF.EMBOSS)
im.show()
# om.show()
