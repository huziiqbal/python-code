# #QUESTIONS BASED ON OOP

# #NUMBER 1

class Car :
  def __init__(self,brand,model,year):
    self.brand = brand
    self.model = model
    self.year = year
  def info(self):
    print(f'Today We are talking about {self.brand} {self.model} which was launched in {self.year}')

no1 = Car("BMW","X5",2020)
no2 = Car("toyota","fortuner",2022)

no1.info()
no2.info()

# NUMBER 2

class Rectangle:
  def __init__(self,length, width):
    self.length = length
    self.width  = width

  def area(self):
   print(f'The area of the rectangle with dimentions you gave is {self.length * self.width}')

first_figure = Rectangle(10,23)
second_figure = Rectangle(34,73)

first_figure.area()
second_figure.area()

# IMPROVED NUMBER 2

class Rectangle:
  def __init__(self,length, width):
    self.length = length
    self.width  = width

  def area(self):
   print(f'The area of the rectangle with dimensions you gave is {self.length * self.width}\n')

while True:

    l=int(input("enter the length of the rectangle you want area of "))
    w=int(input("enter the width of the rectangle you want area of "))

    first_figure = Rectangle(l,w)
    first_figure.area()

    t=int(input("Do you want area of another rectangle ?\n" "if yes then press 1 and if no then press 0 " ))
    if t==0:
       break

    # NUMBER 3

class Person :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info (self):
        print(f'hello my name is {self.name} and I am {self.age} years old')
a=Person("HUZAIFA",20)
a.info()

class Person :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info (self):
        print(f'hello my name is {self.name} and I am {self.age} years old')
a=Person("HUZAIFA",20)
a.info()

       #NUMBER 4

class Circle :
     def __init__(self,radius):
        self.radius = radius
     def area_circumference(self):
         print(f'area of the circle whose radius you gave is {3.14*self.radius*self.radius} Units')

a=Circle(20)
a.area_circumference()

            #  NUMBER 5

class Students:
    def __init__(self,name,marks_of_english,marks_of_maths,marks_of_science):
       self.n = name
       self.m  =  marks_of_english
       self.e =  marks_of_maths
       self.s =  marks_of_science
    def Average_Grade(self):
        k=(self.m +self.e +self.s)//3
        if k>=90:
         grade = "A"
        elif k>=75:
         grade = "B"
        else:
         grade = "C"
        print(f'The average marks of {self.n} are {k}.\nAnd the grade is : {grade}')

Student_one=Students("HUZAIFA",87,93,98)
Student_one.Average_Grade()


