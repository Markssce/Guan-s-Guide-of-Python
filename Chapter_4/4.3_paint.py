def paint_(n):
    i = 0
    while i < n:
        print("{}{}".format((10-i)*" ", (2*i+1)*"*"))
        i+=1
    
    
paint_(3)
paint_(5)
paint_(7)