# has to check for a valid NRIC
# check for 9 characters
# check that the first letter is either S or T,
# while True:
#     test_id = input("What is your NRIC.")
#     if test_id == "end":
#         len(test_id)






# # # Lesson 8 - Input Validation

# # ## Recap 1: List Manipulation
# # You have a list of student index numbers who attended the Math Enrichment class. 
# # However, some students’ attendance were recorded more than once due to a human error.
# # Your task is to clean the list and produce a list of unique Student Indexes

# # Given a list of student index numbers (with duplicates), create a cleaned list where each student appears once.
# # Sort the cleaned list in ascending order.
# # - Print the final list and also print how many duplicates were removed.
# # - Print the count of how many students attended the Math Enrichment Class.

# # student_indexes = [1042, 1099, 1031, 1120, 1075, 1042, 1108, 1019, 1063, 1099, 1156, 1027, 1084, 1111, 1031, 1143, 1055, 1108, 1070, 1132, 1055, 1168, 1020, 1084, 1175]

# # ## Task 1: Data Format Check

# # ### Task 1a
# # Ask the user to input their first name until it is a valid name. 
# # A valid name only contains alphabets.
# # Keep asking for a name until a valid name is input.

# # ### Task 1b
# # Ask the user to input their age until it is a valid number. 
# # Keep asking for a name until a valid number is input.

# # ### Task 1c
# # Ask the user to input a valid username. A valid username must contain alphabets and numbers, but not contain special characters

# # ## Task 2: Length Check (using a while loop)

# # ### Task 2a
# # Ask the user to input their phone number until it is valid using a while loop.
# # Make sure to check if the input is the correct data type as well!

# # ### Task 2b
# # Ask the user to a username and check if it is between 5 to 18 characters long.

# # ## Task 3: Range Check (using a while loop)

# # ### Task 3a
# # Ask the user to input their birth year and check if it is between 1900 and the current year. Keep asking until a correct value is given

# # 1. string must be digit
# # 2. birth_year >= 1900
# # 3. birth_year <= 2026
# while True:
#     birth_year = input("What is your birth year")
#     if birth_year.isdigit() and birth_year >= 1900 and birth_year <= 2026:
#         # print("Sorry, this is an invalid year.")
#         break
#     else:
#         # print("Thank you, Please continue.")
#         print("Sorry, this is an invalid year.")

# # ### Task 3b
# # Ask the user to input their volume setting and check if it is between 0 and 100.
# while True:
#     volume = input("What volume would you like")
#     if volume.isdigit() and volume >= 0 and volume <= 100:
#         ("Thank you. The volume you desire is now set.")
#         break
#     else:
#         # print("Thank you, Please continue.")
#         print("Sorry, this volume is not existant in our speakers")

# # ## Task 4: Mocking Text Generator
# # Create a program that will turn regular sentences into a “SpongeBob Mocking” meme.
# # For example, the program will turn “Hello my name is James” into “HeLlO mY nAmE iS jAmEs”

# # 1. Using input(), ask the user for a sentence
# # 2. Use loops to iterate through each letter in the sentence
# # 3. Alternate between .upper() and .lower() for each letter
# # 4. Print the result.
# sentence = input("What is your sentence? ")
# new_sentence = ""
# is_upper = True
# for char in sentence:
#     if char.isalpha():
#         if is_upper:
#             new_sentence += char.upper()
#         else:
#             new_sentence += char.lower()
#         is_upper = not is_upper
#     else:
#         new_sentence += char
# print(new_sentence)

# sentence = input("Hello, what sentence would you like to put inside this space.")
# while True:
#     if i % 0:
        
# ## Task 5: Slice String
# word = “SINGAPORE”


# # Slice the string and print these words:
# # a. MALAY
# # b. LAY
# # c. ASA
word = "MALAYSIA"
word[:5]
print(word[:5])
word[2:5]
print(word[2:5])
word[3:8:2]
print(word[3:8:2])
word[::2]
print(word[::2])
sentence = "Phyton Makes Coding Fun"
word1 = sentence[0:6]
print(word1)
word2 = sentence[7:12]
print(word2)
phrase1 = sentence[13:]
print(phrase1)
skip_word = sentence[13:19:2]
print(skip_word)
# # ## Task 6: Palindrome
# # Ask the user for an input and check if it is a palindrome, until the input is ‘end’.
# while True
#     pali = input("Please input a word, and I can check whether it is a palindrome. Thank you!")
#     if pali == "end":
#         break
#     # You can try this list of words:
#     # - civic, kayak, level, madam, radar, refer, rotator, tenet, racecar, deified, stats, wow
#     pali[::-1]
#     if pali == pali[::-1]:
#         print(pali)
#         print("Thank you, the word you have inputted is a palindrome.")
#     else:
#         print(pali)
#         print("Sorry, tthe word is not a palindrome")


# ## Task 7: Presence and Existence Checks
# You are hosting a Birthday Party and have invited your friends.

# Create a list with your friends’ names
# - e.g. [“Alice”, “Bob”, Carl”, “Dylan”]

# Write a program to ask for the visitor’s name and check if:
# - Name is entered (presence check)
# - Name is in your friend list (existence check)

# Ask for an input again if a name was not entered.
# Accept the visitor if they are in the list, else deny their entry.
# friends = ["Alice", "Bob", "Carl", "Dylan"]

# while True:
#     valid = True
#     name = input("What is your name?")
#     # presence check
#     if name == "":
#         valid = False

#     if valid:
#         break
# # check for existence
# if name in friends:
#     print("Thank you. Please come in")
# else:
#     print("Sorry, please leave. Thank you!")



# ## Task 8: Format Check
# Ask the user to input their NRIC you need to check:
# 1. First and last character are alphabets in upper case
# 2. First letter must be S, T, F, G, or M.
# 3. Have 7 digits between the alphabets
# 4. Be 9 characters long

# ## Task 9: Password Validation
# A website requires all passwords to
# 1. Be at least 8 characters long
# 2. Contain an upper and lower case
# 3. Contain a number
# 4. No other characters except alphabets or numbers.

# Write a program that will ask the user for a password, and check if the password fits all criteria

# You may use some of the following passwords to test your program:
# - PassW0rd
# - H3ll0W0r1d
# - BestF00d
# - pa55Me