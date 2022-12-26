
a=[0,2,1]
def IsMonoton(a): 
    for i in range(len(a)-1):
        if a[i]<= a[i+1]:
            return "monotome"
        elif a[i]>= a[i+1]:
            return "monotome"
        else:
            return "not monotome"

print("The array: ", a ,"is :", IsMonoton(a))
