dicti={}
user =int(input("enter your number "))
i=1
while i<= user:
    j=1
    a=0
    new=[]
    while(j<=10):
        a=j*i
        new.append(a)
        j=j+1
    dicti[i]=new

    i=i+1
   
print(dicti)

