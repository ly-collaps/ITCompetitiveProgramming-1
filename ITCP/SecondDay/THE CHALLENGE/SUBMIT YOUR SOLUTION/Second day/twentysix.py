sentence = input("please enter a sentence: ")
words = sentence.split()
def printing(words):
    size = max(len(word) for word in words)
    print('*' * (size+4))
    for word in words:
        print('* {a:<{b}} *'.format(a=word, b=size))
    print('*' * (size+4))

printing(words)