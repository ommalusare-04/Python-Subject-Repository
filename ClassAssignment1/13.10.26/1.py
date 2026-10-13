f = open(r"C:\Users\OM\Desktop\PythonRepo\ClassAssignment1\13.10.26\myfile.txt", "r")

data = f.read()
count = 0

for ch in data:
    if ch.lower() in "aeiou":
        count += 1

print("Total vowels:", count)

f.close()