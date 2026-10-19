# def my_func(a,b):
#     rem=a%b
#     division=a/b

#     return rem,division

# num1=int(input("enter the first number:"))
# num2=int(input("enter the first number:"))
# print(my_func(num1,num2))

def table(n):
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")

n=int(input("enter the number:"))
table(n)