odd_square={}

for i in range(1,11):
    if i%2==1:
        odd_square[i]=i*i
print(odd_square)


# Iterating through a Dictionary
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    # print(i)  #To get key
    print(squares[i]) #To get value