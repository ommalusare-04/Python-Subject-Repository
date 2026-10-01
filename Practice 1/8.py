n=int(input("enter the number of pyramid levels:"))
for i in range(1,n+1):
    for j in range(1,n*2):
        if j>=n-i+1 and j<=n+i-1:
            if i%2==0:
                print("@",end="")
            if i%2!=0:
                print("*",end="")
        else:
            print(" ",end="")
    print()