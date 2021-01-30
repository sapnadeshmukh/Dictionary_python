def square (number):
    dic={}
    for i in range(1,number+1):
        dic[i]=i*i
    print(dic)


user=int(input("enter number"))
square(user)


