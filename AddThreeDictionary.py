dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
result = {} 
for d in (dic1,dic2,dic3): 
    for k in d.keys():
        result[k] = result.get(k, 0) + d[k] 
print(result)