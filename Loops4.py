inp= int(input("Enter any Positive Number to print factorial:"))
factorial=1
for i in range(1,inp+1):
    factorial = factorial*i

print("The factorial of ",inp, "is",factorial)
