age = int(input())
year = 52
life = 90

life_left = life - age
weeks_left = year * life_left

print(f"You have {weeks_left} weeks left.")



height = float(input())
weight = float(input())

meters_squared = height**2
conversion = int(weight / meters_squared)

print(type(conversion))
print(f"BMI = {conversion}")


# ~~~

# String
print("Hello"[4])
print("123" + "345")

# Integer
print(123 + 345)

# Float
print(3.14159)

# Boolean

# True
# False

# ^ Make sure capital letter

#num_char = len(input("What is your name?"))
#new_num_char = str(num_char) # Conversion int -> String
#print("Your name has " + new_num_char + " characters.")

a = str(123)
print(type(a))

two_digit_number = input("Input two-digit number here\n")
print(type(two_digit_number))
separate_one = int(two_digit_number[0])
separate_two = int(two_digit_number[1])

add = separate_one + separate_two
print(add)




print("Welcome to the tip calculator.")
bill = float(input("What was the total Bill? $"))
party = float(input("How many people to split the bill? "))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

split = bill / party
print(f"Split not-including tip {split}")

decimal = percentage / 100
tip = decimal * split
full = "{:.2f}".format(tip + split)
print(f"tip {tip}")
print(f"Full split including tip ${full}")


