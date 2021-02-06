# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_heights = 0
length = 0
for student_height in student_heights:
    total_heights += student_height
    length += 1

average_heights = total_heights / length

print(round(average_heights))





