# Accepts value from s assume start and n number that is for start number + n number to print squares
# Eg s=3 n=4
# output : 9 16 25 36
s=int(input("enter the first number:"))
n=int(input("enter the last number"))

print(f"square from {s} to {n}:")
for i in range(s,s+n):
    print(i*i)