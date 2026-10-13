li = []
n = int(input("Enter number of elements: "))

for i in range(n):
    item = input("Enter item: ")
    if item not in  li:
        li.append(item)

print(li)