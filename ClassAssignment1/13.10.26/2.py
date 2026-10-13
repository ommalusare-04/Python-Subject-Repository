f = open(r"C:\Users\OM\Desktop\PythonRepo\ClassAssignment1\13.10.26\myfile.txt", "r")
li = f.readlines()

print("Total number of lines:", len(li))
print("Second line:", li[1])
print("Fourth line:", li[3])
f.close()
