dict =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
count = 0
for l in dict.values():
   for i in l: 
       count =count+ 1
print(count)
      