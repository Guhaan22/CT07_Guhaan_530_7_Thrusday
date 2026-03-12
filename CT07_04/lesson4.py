# # count = 0
# # while count< 5:
# #     print(count)
# #     count += 1
# #     input("What country would you like to visit")
# #     list.append(input)
# #     if input(end)
# # somewords =["great", "word", "evening", "holiday", "good"]
# # # print(len(somewords))
# # # print(somewords)
# # for words in somewords:
# #     print(words)
# countries = []
# while True:
#     reply = input("Which country would you like to go?")
#     if reply == "end":
#         break
#     else:
#         countries.append(reply)

# # end of while loop
# print(countries)
# # write the code using for loop
# for nations in countries:
foodies = []
while True:
    items = input("What food item would you like to input sir.")
    if items == "end":
        break
    else:
        foodies.append(items)

# end of while loop
print(foodies)
answer = input("what would you like to order?")
if answer in foodies:
    print("Yes, we sell that. You may have a seat if you wish")
else:
    print("Sorry, we do not sell this food. Please go to another restaurant. Goodbye.")
    


    
