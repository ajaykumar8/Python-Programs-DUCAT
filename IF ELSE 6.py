print("Welcome to WDC bank")
def withdraw():
    print("Withdrawal selected")
    w=int(input("Amount you want to withdraw: "))
    w=w-b
    print("Amount Dispensing",w)

def deposit():
    print("Deposit Selected")
    d=int(input("Enter the amount you want to deposit: "))
    b=d+c
    print("AMount Deposited",d)
   # print("Updated Balance",)

def check_balance():
    print("Your Last Balance is:",d)


print("Menu-\n"
      "1.Withdraw-\n"
      "2.Deposit-\n"
      "3.Check Balance-\n")
x= int(input("Press the number corresponding to Menu Options:"))

if x ==1:
    if d >= 500:
        withdraw()
    else:
        print("Not able to withdraw cash. Balance less than 500")

elif x ==2:
    deposit()

elif x ==3:
    check_balance()

else :
    print("INVALID INPUT")






    
