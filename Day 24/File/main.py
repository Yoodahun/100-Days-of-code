# with open("../my_text.txt") as file:
#     contents = file.read()
#
#     print(contents)

with open("../my_text.txt", mode="a") as file:
    file.write("\nThis is New text append")
