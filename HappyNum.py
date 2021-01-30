# num=int(input("enter num"))
# rem=0
# sum=0
# while(num>0):
#     rem=num%10
#     sum= sum +(rem*rem)
#     num=num//10
# print(sum)


def isHappyNumber(num):
    rem = sum = 0
    while(num > 0):
        rem = num%10
        sum = sum + (rem*rem)
        num = num//10
    return sum
num = int(input("enter number to check num is happynum or not= "))
result = num
while(result != 1 ):
    result = isHappyNumber(result)
    if(result == 1):
        print (num,"is a happy number")
    elif(result == 4):
        print(num, "is not a happy number")





