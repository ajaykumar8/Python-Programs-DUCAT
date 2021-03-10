print("Program to Find Area of a Rectangle and Circumference of a circle")

def rectangle():
    print("Rectangle selected ")
    length = int(input("enter the length of rectangle:"))
    breadth = int(input("enter the breadth of rectangle:"))
    area= length*breadth
    print("area of the rectangle is :", area)

def circle():
    print("Circle selected")
    radius=int(input("enter the radius:"))
    area=3.14*(radius**2)
    print(area)


print("Menu-\n"
      "1. Circle-\n"
      "2. Rectangle-\n")

x= int(input("Enter the corresponding number from the given menu to calculate the area of the shape:"))

if x == 1:
    circle()
elif x == 2:
    rectangle()
else  :
    print("Wrong Input")
