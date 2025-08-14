
#Required Parameters
my_list = []
num = 10, 20, 30, 40
an_list = [50, 60, 70]

#Appending num to my_list
for i in num:
    my_list.append(i)

#Inserting 15 at index[1]
my_list.insert(1, 15)

#Extending my_list with an_list
my_list.extend(an_list)

#Removing the last element of my_list
del my_list[-1]

#Finding and Printing the index of 30 in my_list
print(my_list.index(30))

#Sorting my_list
my_list.sort()

#Printing my_list
print(my_list)
