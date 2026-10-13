f = open("myfile.txt", "r")
data = f.read()

count = 0

for ch in data:
    if ch.lower() in "aeiou":
        count += 1

print("Total vowels:", count)

f.close()