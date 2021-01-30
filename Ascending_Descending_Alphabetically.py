# "Ascending orde"
y={'carl':40,'alan':2,'bob':1,'danny':3} 
l=list(y.items())
print(l) 
l.sort()            
dic1=dict(l)
print(dic1)

#"Descending order"
y={'carl':40,'alan':2,'bob':1,'danny':3} 
l=list(y.items())
l.sort(reverse=True) 
dict2=dict(l) 
print(dict2) 

# sorted by key
color_dict = {'red':2,
          'green':9,
          'black':11,
          'white':23}

for key in sorted(color_dict):
    print(key, color_dict[key])
	