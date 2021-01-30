my_dict = {
    'a': 50,
    'b': 580,
    'c': 560,
    'd': 40,
    'e': 400,
    'f': 200
}

all_values = my_dict.values()
a=list(all_values)
i=0
max_num1=0
max_num2=0
max_num3=0
new=[]
while i<len(a):
    if a[i]>max_num1:
        max_num1=a[i]
    i=i+1
new.append(max_num1)
j=0
while (j<len(a)):
    if (max_num1>a[j] and max_num2<a[j]):
        max_num2=a[j]
    j=j+1
new.append(max_num2)
k=0
while(k<len(a)):
    if (max_num2>a[k] and max_num3<a[k]):
        max_num3=a[k]
    k=k+1
new.append(max_num3)
print(new)

