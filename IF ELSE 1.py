print("Program to Input 5 Numbers and find Percentage")
Mth = input("Enter Marks obtained in Maths :")
Hin = input("Enter Marks obtained in Hindi :")
Eng = input("Enter Marks obtained in English :")
Ssc  = input("Enter Marks obtained in Social  :")
Eco = input("Enter Marks obtained in Economics :")
sum = int(Mth) + int(Hin) + int(Eng) + int(Ssc) + int(Eco)
print(sum)

percentage = float(sum)*(100/500)
print(percentage,"%")

if percentage >= 60:
    print("First Division")
elif percentage >= 50 or percentage <= 59:
    print("Second Divison")
elif percentage >= 40 or percentage <= 49:
    print("Third Division")
else :
    print("Failed")
