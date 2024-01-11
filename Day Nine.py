# Scores 91 - 100: Grade = "Outstanding"
#
# Scores 81 - 90: Grade = "Exceeds Expectations"
#
# Scores 71 - 80: Grade = "Acceptable"
#
# Scores 70 or lower: Grade = "Fail"

# Grading Program

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_Grades = {}
for x in student_scores:
    if student_scores[x] > 90:
        student_Grades[x] = "Outstanding"
    elif student_scores[x] > 80:
        student_Grades[x] = "Exceeds Expectations"
    elif student_scores[x] > 70:
        student_Grades[x] = "Acceptable"
    else:
        student_Grades[x] = "Fail"
# TODO-2: Write your code below to add the grades to student_grades.👇


# 🚨 Don't change the code below 👇
print(student_Grades)


# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# nesting a list in a dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting dictionary in a dictionary

travel_log2 = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "Total Visits": 12},
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

print(travel_log2["France"])

# Nesting dictionary in a list

travel_log3 = [
    {
        "Country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "Total Visits": 12
    },
    {
        "Country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "Total Visits": 12
    }
]

print(travel_log3[1])

