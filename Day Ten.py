def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# TODO: Add more code here 👇
def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        month_days[1] += 1
        return month_days[month - 1]
    else:
        return month_days[month - 1]


# 🚨 Do NOT change any of the code below
month = int(input())  # Enter a month
year = int(input())  # Enter a year
days = days_in_month(year, month)
print(days)






# def fuck_dibber():
#     one = "Fuck"
#     two = "Dibber"
#     if one == "Fuck":
#         return True
#
# print(fuck_dibber())
# month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# month_days[1] += 1
# print(month_days[1])

# Functions with Output


# def format_name(f_name, l_name):
#     print(f_name.title())
#     print(l_name.title())
#
# first = ""
# last = ""
# format_name()
#
#
