s=int(input("enter the first number:"))
n=int(input("enter the last number"))

print(f"square from {s} to {n}:")
for i in range(s,n+1):
    print(i*i)