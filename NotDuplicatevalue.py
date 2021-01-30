new=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]
u_value = set( i for dic in new for i in dic.values())
a=(list(u_value))
print(sorted(a))

