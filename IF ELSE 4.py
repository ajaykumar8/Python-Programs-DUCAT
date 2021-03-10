print("Menu driver Program to find if number in even, odd or positive , negative")

def even_odd():
    print("You selected to check if No. is Even or Odd")
    x=int(input("Enter the Number:"))
    if x%2==0:
        print("Number is even")
    elif x==0:
        print("Number is Zero")
    else:
         print("Number is odd")


def pos_neg():
    print("You have selected to check if the no. is positive or negative")
    x= int(input("Enter the number:"))
    if x > 0:
        print("number is Positive:")
    elif x ==0:
        print("Number is Zero")
    else :
        print("Number is Negative:")

print("Menu-\n",
      "1.Check if number is even or odd-\n",
      "2.Check if number is positive or negative-\n")

num = int(input("Select any number corresponding to the given menu to perform following functions:"))

if num==1:
    even_odd()

elif num == 2:
    pos_neg()

else:
    print("Invalid Input")

           
              
