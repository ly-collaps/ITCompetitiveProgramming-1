word = input("please enter a word: ")
for letter in range(len(word)-1, -1, -1):
    print(word[letter], end ="")
