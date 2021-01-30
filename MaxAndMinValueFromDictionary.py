# max value of dictionary
my_dict = {'x':23, 'y':56000, 'z': 6578,'j':34}
empty_list=[]
for i in my_dict:
    empty_list.append(my_dict[i])
print(empty_list)
i=0
max=empty_list[i]
while (i<len(empty_list)):
    if empty_list[i]>max:
        max=empty_list[i]
    i=i+1
print(max)


# min value of dictionary
my_dict = {'x':199, 'y':25, 'z': 9,'h':67}
empty_list=[]
for i in my_dict:
    empty_list.append(my_dict[i])
print(empty_list)
i=0
min=empty_list[i]
while (i<len(empty_list)):
    if empty_list[i]<min:
        min=empty_list[i]
    i=i+1
print(min)