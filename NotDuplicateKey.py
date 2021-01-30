dic={
    'ball':'red',
    'bat':4,
    'wickets':8,
    'ball':'green',
    'bat':3
    }
temp = []
for i in dic.items(): 
    if i not in temp: 
        temp.append(i)
a=dict(temp)
print(a)


