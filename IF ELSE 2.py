print("Eligiblity for Admission to professional course in a college ")
# input maths marks
maths = int(input("Marks in Maths:" ))

#Input Physics marks
physics = int(input("Marks in Physics:" ))

#Input Chemistry marks
chemistry = int(input("Marks in chemistry:" ))

sum = int(maths)+ int(physics)+int(chemistry)
print(sum)

pm = int(physics)+ int(maths)

if maths >= 60 and physics >= 50 and chemistry >= 40: 
    print("Eligible through Criteria 1 ")
elif sum >= 200:
    print("ELigibility through Criteria 2")
elif pm >= 150:
    print("Eligibility through Criteria 3")
else :
    print("No Criteria Fulfilled")

                
