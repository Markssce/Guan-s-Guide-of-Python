import random
def fun(x,y):
    A_G=0
    U_Z=0
    for a in x:
        if "A" <=a<= "G":
            A_G=A_G+1
        elif "U" <=a<= "Z": # Error
            U_Z=U_Z+1
    y[0]=A_G
    y[1]=U_Z
    return
x=[]
for i in range(30):
    a=random.randint(0,25)
    c=chr(a)
    x.append(c)
result=[]
fun(x,result)
print("A~G字母个数:", result[0], "U~Z字母个数:",result[1])
x.sort(reverse=True)
i = 1
for a in x:
    print("{:4s}".format(a),end="")
i=i+1
if i % 5==0:
    print("")