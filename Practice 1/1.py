# Prints the sum of First 10 even numbers that are 20-10 so we take n = 20 
# In that 10 are odd numbers and 10 are even Numbers
n=20
sum=0 
for i in range(0,n+1):
    if i%2==0:
        sum+=i
print(sum)