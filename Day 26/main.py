
number = [1 ,2 ,3]
new_number = [ n + 1 for n in number]
print(new_number)

name = "Angela"
letters_list = [ letter for letter in name]
print(letters_list)


double_list = [ n*2 for n in range(1,5)]
print(double_list)


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

long_name = [n.upper() for n in names if len(n) > 5 ]
print(long_name)
