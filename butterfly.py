

row=int(input("Enter rows number"))

for i in range(1,row+1):
    print("*"*i,end="")
    print(" "*((row-i)*2),end="")
    print("*"*i)

for i in range(row,0,-1): 
    print("*"*(i-1),end="")
    print(" "*((row+1-i)*2),end="")
    print("*"*(i-1))
