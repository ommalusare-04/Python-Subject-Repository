str=input("enter the string:")
count=0
li=list(str)
for i in li:
    if i in "aeiouAEIUO":
        count+=1

print(f"there are {count} vowels.")