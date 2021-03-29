sum_odd=0
sum_even=0

for i in range(101):
    if i%2==1:
        sum_odd+=i
    else:
        sum_even+=i

print("Sum of Odd Numbers:",sum_odd)
print("Sum of Even Numbers:",sum_even)
