import math
class Student:
    def __init__(self, a, b, c):
        self.No = a
        self.Name = b
        self.Score = c

    # def SetValue(self, a, b, c):
    #     self.No = a
    #     self.Name = b
    #     self.Score = c
    def Disp(self):
        print(self.No)
        print(self.Name)
        print(self.Score)
# p = Student("2552800", "Guo", 100) # 参数要和设定的个数匹配，否则报错。
# p.Disp()
# print(isinstance(p,Student))
# print(type(p))

class MyPoint:
    def SetValue(self, x, y):
        self.__x = x
        self.__y = y
    def Distance(self):
        return(math.sqrt(self.__x**2 + self.__y**2))
d = MyPoint()
# d.SetValue(3, 4)
# # print(d.__x, d.__y) # __x and __y is private.
# print(d.Distance())

# 定义表示一元二次方程的类 Equation，含有构造函数和求解方程根的函数。
class Equation:
    def __init__(self, x, y, z):
        self.a = x
        self.b = y
        self.c = z
    def slove(self):
        delta = self.b**2 - 4.0*self.a*self.c
        if (delta>=0):
            root_1 = (-self.b + math.sqrt(delta))/2*self.a
            root_2 = (-self.b - math.sqrt(delta))/2*self.a
            ans = [root_1, root_2]
            return ans
        else:
            return[]
# equ = Equation(1, 2, 1)
# print(equ.slove())

class StudentLeader(Student):
    def __init__(self, a, b, c, d):
        Student.__init__(self, a, b, c)
        self.Duty = d        
    # def New_SetValue(self,a,b,c,d):
    #     Student.SetValue(self,a,b,c)
    #     self.Duty = d  
    def New_Disp(self):
        Student.Disp(self)
        print(self.Duty)
    # def SetValue(self, a, b, c, d):
    #     self.No = a
    #     self.Name = b
    #     self.Score = c
    #     self.Duty = d
    # def Disp(self):
    #     print(self.No)
    #     print(self.Name)
    #     print(self.Score)
    #     print(self.Duty)

sLeader = StudentLeader("2250450", "Mercury","100", "TA")
sLeader.New_Disp() 

