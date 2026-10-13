# we take a string from user and return total number of vowels from the string.
str=input("enter the string:")
count=0
li=list(str) #we convert str in list
for i in li: # check every word one by one using for loop
    if i in "aeiouAEIUO":  #checks whether the word is vowel or not if vowel count increase by one
        count+=1

print(f"there are {count} vowels.") #shows count of total number of vowels.