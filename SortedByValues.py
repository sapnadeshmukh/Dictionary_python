dict1={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
sorted_values = sorted(dict1.values()) # Sort the values
print(sorted_values)
sorted_dict = {}

for value in sorted_values:
    for key in dict1.keys():
        if dict1[key] == value:
            sorted_dict[key] = dict1[key]
            break

print(sorted_dict)

