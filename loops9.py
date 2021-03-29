rows = 4
k=rows-1
for i in range(0,rows+1):
    for j in range(1,k):
        print(end="")
    for j in range(1,i+1):
        print(i,end=" ")
        j=j+1
    print()
