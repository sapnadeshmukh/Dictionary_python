marks={"sapna":21,"abhi":22,"bitti":23,"baby":3}

for i in marks:
    if (marks[i]%2==0):
        print(i,":",marks[i],"even")
    else:
        print(i,":",marks[i],"odd")

# Access keys without function
marks={"sapna":21,"abhi":22,"bitti":23,"baby":3}
for i in marks:
    print(i)

# Access values without function

marks={"sapna":21,"abhi":22,"bitti":23,"baby":3}
for i in marks:
    print(marks[i])

# sort by keys
color_dict = {'red':3,
          'green':7,
          'black':8,
          'white':90}

for key in sorted(color_dict):
    print( (key, color_dict[key]))