sentence = input("Enter a sentence: ")
li = sentence.split()
longest = ""
for word in li:
    if len(word) > len(longest):
        longest = word
print("List of words:", li)
print("Longest word:", longest)