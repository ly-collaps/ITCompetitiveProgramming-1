n = int(input("please enter the number of numbers: "))
a = int(input("please enter the first devisor: "))
b = int(input("please enter the second devisor: "))
print("i   WORD")
for i in range(0,n):
    if i%a == 0 and i%b != 0 :print(i, " IT")
    if i%b == 0 and i%a != 0:print(i," CCC")
    if i%b == 0 and i%a == 0:print(i, " ITCCC")
    else:print(i," -")
    
