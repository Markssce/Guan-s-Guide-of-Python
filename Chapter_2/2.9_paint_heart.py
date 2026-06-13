# Paint a heart shape to celebrate birthday with star★
space = " "
star_shape = "★"
name = input("Enter name: ")
n = len(name)
print("{}Dear.{}, Happy birthday!".format(space*5, name))
print("{}{}{}{}{}".format(space*9, star_shape*2, space*2, star_shape*2, space*9))
print("{}{}{}".format(space*8,star_shape*7,space*9))
for i in range(1,5):
    print("{}{}{}".format((7+i)*space, (9-2*i)*star_shape, (7+i)*space))
