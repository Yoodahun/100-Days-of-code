# List comprehension ####################################################
# number = [1 ,2 ,3]
# new_number = [ n + 1 for n in number]
# print(new_number)
#
# name = "Angela"
# letters_list = [ letter for letter in name]
# print(letters_list)
#
#
# double_list = [ n*2 for n in range(1,5)]
# print(double_list)
#
#
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
#
# long_name = [n.upper() for n in names if len(n) > 5 ]
# print(long_name)
##############################################################################
import random
import pandas

# students_score = {student: random.randint(1, 100) for student in names}
# print(students_score)
# passed_students = {student:student_score for (student, student_score) in students_score.items() if student_score >= 60}
# print(passed_students)

################################################################################################
#use Pandas DataFrame.

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a dataframe

for (key, value) in student_data_frame.items():
    print(value)

# Loop through rows of a dataframe
for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row)
    print(row.student)
