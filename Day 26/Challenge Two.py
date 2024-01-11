# inp = 'What is the Airspeed Velocity of an Unladen Swallow?'
# sentence = inp
#
# result = {x: len(x) for x in sentence.split()}
#
# print(result)
#
#
# # Challenge Two
# this = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# weather_c = this
#
# weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}
# print(weather_f)
#
#
# # side note for myself
#
student_dict = {
    "student": ["Angela", "Brandon", "James", "Lilly"],
    "score": [56, 76, 86, 45]
}

# Looping through dictionaries normally
for (key, value) in student_dict.items():
    print(value)


# Using Pandas

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #print(row.score)

    if row.student == "Angela":
        print(row.score)



