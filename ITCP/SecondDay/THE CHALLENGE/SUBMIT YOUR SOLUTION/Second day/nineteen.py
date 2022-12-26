number = int(input("please enter a number: "))
sum = 0
for devisor in range(1,number):
    if number%devisor == 0:
        sum = sum + devisor
if sum == number :
    print(number, " is a perfect number")
else:
    print(number, " is not a perfect number")