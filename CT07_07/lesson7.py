# print("Hello from lesson 7")
# students = []
# student1 = ["Henry,", "12345678", "Scouts"]
# student2 = ["Joyce,", "87654321", "Scouts"]
# student3 = ["Ethan,", "37229802", "Scouts"]
# students.append(student1)
# students.append(student2)
# # students.append(student3)
# # for record in students:
# #     name, phone, cca = record # unpacking
# #     print("Name:", name)
# #     print("Phone:", phone)
# #     print("CCA:", cca)
# shelf1 = ["books", "notebooks"]
# shelf2 = ["lunchbox", "water bottle"]
# inventory = shelf1 + shelf2
# print(inventory)
# list1 = [3, 20, 2,65, 1,75]
# list2 = [6,15, 5,45, 4,20]
# sortedlist = sorted(numbers)
# print(sortedlist)
      
list1 = [3, 20, 2, 65, 1, 75]

# how to add to the list
list1.append(25) # how to add a new item to the list

# retrieve the 3rd item
print(list1[2])

# remove an item from the list?
del list1[3]
print(list1)

# loop through the list
for num in list1:
    if num > 20:
        print(num)






# # loop through every value here and print it out

# for loop to print out values from 0 - 9
# for i in range(0, 10):
#     print(i)

### use a while loop, print numbers from 0 - 9
# number = 0
# while number != 10:
#     print(number)
#     number = number + 1

