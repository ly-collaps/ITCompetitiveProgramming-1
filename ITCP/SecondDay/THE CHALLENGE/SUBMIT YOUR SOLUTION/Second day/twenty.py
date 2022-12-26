number = int(input("please entre a positive number: "))
Anotherdevisor = False
for devisor in range(2,number):
    if number%devisor == 0 :
        Anotherdevisor = True
        break
if Anotherdevisor == True : print(number, "This is not a primary number")
else : print(number, "This is  a primary number")
