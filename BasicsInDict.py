# merge two dictionaries
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d3=d1.copy()
d3.update(d2)
print(d3)

# iterate over dictionaries using for loops.
d = {'Red': 1, 'Green': 2, 'Blue': 3} 
for i,j in d.items():
    print(i,j)


# sum all the items in a dictionary.
my_dict = {'data1':100,'data2':1,'data3':2}
sum=0
for i in my_dict.values():
    sum=sum+i
print(sum)

# multiply all the items in a dictionary.
my_dict = {'data1':100,'data2':-54,'data3':247}
multi=1
for i in my_dict.values():
    multi=multi*i
print(multi)

# remove a key from a dictionary.
myDict = {'a':1,'b':2,'c':3,'d':4}
if 'a' in myDict:
    del(myDict['a'])
print(myDict)



# map function
def myfunc(a):
  return len(a)
x = map(myfunc, ('apple','sapnad','one'))
print(x)
#convert the map into a list, for readability:
print(list(x))