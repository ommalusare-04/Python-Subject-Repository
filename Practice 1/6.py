li=[]
n=int(input("enter the number of elements you want:"))
for i in range(n):
    item=input("enter the item:")
    li.append(item)
print(li)
print(list(reversed(li)))
