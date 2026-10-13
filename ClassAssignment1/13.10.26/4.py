f = open(r"C:\Users\OM\Desktop\PythonRepo\ClassAssignment1\13.10.26\myfile.txt", "r")
data = f.read()
f.close()
li = data.split()
print("Total number of words:", len(li))
unique = []
for word in li:
    if word not in unique:
        unique.append(word)
print("Unique words:", unique)