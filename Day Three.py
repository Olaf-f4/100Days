# Dibbers

print("The Love Calculator is calculating your score...")
name1 = input()
name2 = input()

combined_names = name1 + name2
lower_names = combined_names.lower()
first_digit = sum(lower_names.count(c) for c in "true")
second_digit = sum(lower_names.count(c) for c in "love")
score = int(str(first_digit) + str(second_digit))
print(score)



# Love Calculator - Hers

print("The Love Calculator is calculating your score...")
name1 = input()
name2 = input()

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))


# Love Calculator - Olaf

print("The Love Calculator is calculating your score...")
name1 = input().lower()
name2 = input().lower()

list1 = ([*name1])
list2 = ([*name2])

true = ([*"true"])
love = ([*"love"])

store1 = 0
store2 = 0

for x in list1:
    for y in true:
        if x == y:
            store1 += 1

for x in list2:
    for y in true:
        if x == y:
            store1 += 1

for x in list1:
    for y in love:
        if x == y:
            store2 += 1

for x in list2:
    for y in love:
        if x == y:
            store2 += 1

combined = int(str(store1) + str(store2))
print(combined)
print(f"{store1}{store2}")

if (combined < 10) or (combined > 90):
    print(f"Your score is {combined}, you go together like coke and mentos.")
elif (combined >= 40) and (combined <= 50):
    print(f"Your score is {combined}, you are alright together.")
else:
    print(f"Your score is {combined}.")

#
# # Pizza thing
#
# print("Thank you for choosing Python Pizza Deliveries")
# size = input("What Size Pizza, S, M, L\n")
# add_pepperoni = input("Add Pepperoni, Y or N\n")
# extra_cheese = input("Add extra cheese, Y or N\n")
#
# bill = 0
#
# if bill == 0:
#     if size == "S":
#         bill += 15
#     elif size == "M":
#         bill += 20
#     else:
#         bill += 25
#
#     if add_pepperoni == "Y":
#         if size == "S":
#             bill += 2
#         else:
#             bill += 3
#     if extra_cheese == "Y":
#         bill += 1
#
# print(f"Your bill comes out to ${bill}.\n"
#       f"Pizza Size = {size}\n"
#       f"Extra Pepperoni = {add_pepperoni}\n"
#       f"Extra Cheese = {extra_cheese}")
#
#
#
#
#
#
#
#
#
#
# # Leap Year
#
# year = int(input())
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not leap year")
#
#
#
#
#
#
#
#
#
#
#
# height = float(input())
# weight = int(input())
#
# BMI = round(weight / (height ** 2), 2)
# print(BMI)
#
# # Your BMI is x, you are x.
#
# classification = ""
#
# if BMI < 18.5:
#     classification = "underweight"
# elif BMI < 25:
#     classification = "normal weight"
# elif BMI < 30:
#     classification = "slightly overweight"
# elif BMI < 35:
#     classification = "obese"
# else:
#     classification = "clinically obese"
#
#
# print(f"Your BMI is {BMI}, you are {classification}.")
