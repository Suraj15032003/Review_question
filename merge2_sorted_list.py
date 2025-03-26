list1=[1,2,3,4]
list2=[1,2,3,4]
sorted_list =[]
for i in list1:
    sorted_list.append(i)
for i in list2:
    sorted_list.append(i)


#sorted_list.sort()
print(sorted_list)
sorted_values=[]
while sorted_list:
    min_value=sorted_list[0]
    for i in sorted_list:
        if i<min_value:
            min_value=i
    sorted_values.append(min_value)
    sorted_list.remove(min_value)
print(sorted_values)