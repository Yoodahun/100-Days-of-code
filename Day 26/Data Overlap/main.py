
with open("file1.txt") as file1:
    file1_list = file1.readlines()

with open("file2.txt") as file2:
    file2_list = file2.readlines()

result = [int(n) for n in file1_list if n in file2_list]


# Write your code above 👆

print(result)
