# Body Mass Index 

weight_, height_ = eval(input("Enter your Weight(kg) and height(m): "))
BMI = weight_/(height_**2)
if BMI <18.5:
    print("BMI={:5.2f}, you're a little bit thin :()".format(BMI))
if 24 > BMI >18.5:
    print("BMI={:5.2f}, you're normal :)".format(BMI))
if 28 > BMI >24:
    print("BMI={:5.2f}, you're a little bit fat :()".format(BMI))
if BMI > 28:
      print("BMI={:5.2f}, you're a so fat :()".format(BMI))
      