# import time
# input("How many minutes do you wish to study.")
# time.sleep(input * 60)
# print("Time's up!")
savings = 0
while savings <100:
    daily = input("How much did you save")
    daily = int(daily)
    savings += daily
else:
    print("Congratulations! You have saved 100 dollars")