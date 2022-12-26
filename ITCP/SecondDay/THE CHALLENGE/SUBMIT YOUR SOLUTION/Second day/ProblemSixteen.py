number = input("please enter a number: ")
if number[0] == '-':
    numberp= number[1::]
    numberReversed = "-" + str(numberp[::-1])
else:
    numberReversed = number[::-1]
print("the reversed  number of ", number , " is ", numberReversed)