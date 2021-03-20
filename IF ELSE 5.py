print("Simple Calculator")

def add():
    print(" You selected Addition ")
    val1= int(input("Enter 1st Number:"))
    val2= int(input("Enter 2nd Number:"))
    val3= val1+ val2
    print("Additon of 1st and 2nd number is:", val3)

def subt():
    print("You selected Subtraction")
    val1= int(input("Enter 1st Number:"))
    val2= int(input("Enter 2nd Number:"))
    val3= val1-val2
    print("Subtraction of 1st and 2nd Number is:",val3)

def multiply():
    print("You selected  Multiplication")
    val1= int(input("Enter 1st Number:"))
    val2= int(input("Enter 2nd Number:"))
    val3= val1*val2
    print("Mulitplication of 1st and 2nd Number is :", val3)

def division():
    print("You selected Division:")
    val1= int(input("Enter 1st Number:"))
    val2= int(input("Enter 2nd Number:"))
    val3= val1//val2
    print("Division of 1st and 2nd Number is :",val3)

def inverse():
    print("You Selected Inverse")
    Val= int(input("Enter the number:"))
    val1=1/val
    print("Inverse of:",Val,"is",val1)
    
    
def square():
    print("You Selected Square")
    val=int(input("Enter the Number :"))
    val2=val1*val1
    print("Square of the given number is:",val2)

def cube():
    print("You Selected Cube")
    val1=int(input("Enter the Number:"))
    val2=val1*val1*val1
    print("Cube of Given number is:", val2)

print("Menu-\n"
      "1.Addition-\n"
      "2.Subtraction-\n"
      "3.Multiplication-\n"
      "4.Division-\n"
      "5.Square-\n"
      "6.Inverse
      "7.Cube-\n")

x=int(input("press number from 1 to 7 to perform the following function according to given menu: "))
    
if x==1:
      add()

elif x==2:
    subt()

elif x==3:
    multiply()

elif x==4:
    division()

elif x==5:
      square()

elif x==6:
    inverse()

elif x==7:
    cube()
      
      
else :
    
    print("Invalid Value")
