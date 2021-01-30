my_dict = {
    'a': 500,
    'b': 456,
    'c': 309,
    'd': 40,
    'e': 100,
    'f': 20
}

all_values = my_dict.values()
a=list(all_values)
all_keys=my_dict.keys()
b=list(all_keys)

i=0
max_num1=0
max_num2=0
max_num3=0
new=[]
while i<len(a):
    if a[i]>max_num1:
        max_num1=a[i]
        max_key1=b[i]
    i=i+1

new.append(max_key1)

j=0
while (j<len(a)):
    if (max_num1>a[j] and max_num2<a[j]):
        max_num2=a[j]
        max_key2=b[j]

    j=j+1
new.append(max_key2)
k=0
while(k<len(a)):
    if (max_num2>a[k] and max_num3<a[k]):
        max_num3=a[k]
        max_key3=b[k]

    k=k+1
new.append(max_key3)

print(new)