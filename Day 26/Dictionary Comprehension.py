# Example of Dic Comp

# new_dict = {new_key:new_value for (key,value) in dict.items}
# new_dict = {new_key:new_value for (key,value) in dict.items if test}
import random


names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Brandon', 'Eleanor']
student_score = {student: random.randint(1, 100) for student in names}

passed_students = {key: value for (key, value) in student_score.items() if value >= 60}
print(passed_students)


