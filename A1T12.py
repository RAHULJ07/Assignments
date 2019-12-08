List=[]
for i in list(range(2000,3201)):
    if(i%7==0 and i%5!=0):
        List.append(i)
print(List)
