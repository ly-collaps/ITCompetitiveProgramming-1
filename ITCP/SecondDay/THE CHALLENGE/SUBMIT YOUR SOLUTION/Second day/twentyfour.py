sentence = input("please entre a sentence: ")
words =sentence.split()
newWords = []
for word in words:
    lastChar = word[-1]
    remainedWord = word[0:-1]
    newWord = lastChar+remainedWord+'hay'  
    newWords.append(newWord)
print (' '.join(newWords))
