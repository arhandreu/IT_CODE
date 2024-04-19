# 1_______________________________
user_string = input()
print(user_string[::-1])

# 2___________________________________________________
string_find = "hhhhhhh"
left_index= string_find.find("h")
right_index = string_find.rfind("h")
string_ = ""

if left_index != -1:
    if right_index != -1 and left_index != right_index:
        string_ = string_find[left_index+1:right_index].replace("h", "H")
        string_find = string_find[:left_index+1] + string_ + string_find[right_index]

print(string_find)

# 3_____________________________________________________________
user_string = input()
count_words = len(user_string.split())
print(count_words)

# 4______________________________________________________________
user_string = " упе уке уке "
strr = user_string.strip()
print(strr.count(" ") + 1)

# 5___________________________________________________________________
user_string = input()
reverse_string = " ".join(user_string.split()[::-1])
print(reverse_string)

# 6__________________________________________________________________________
user_string = input()
list_fio = user_string.split()
print(list_fio[0], list_fio[1][0]+".", list_fio[2][0]+".")

# 7___________________________________________________________________________________
list_mat = [2, [2.5, [1+2j, [[], 3, "Иголка"]]]]
print(list_mat)

# 8______________________________________________________________________________
list_1 = [1, 2]
list_2 = [3, 4]
list_sum1 = list_1 + list_2
list_1.extend(list_2)
print(list_sum1, list_1)

# 9___________________________________________________________________________
list_1 = [1, 2]
list_2 = [3, 4, 4]
list_1.extend(list_2)
list_1.sort()
print(list(set(list_1)))

# 10____________________________________________________________________________________
numbers = input()
list_numbers = numbers.split()
set_numbers = set(list_numbers)
if len(list_numbers) == len(set_numbers):
    print("Уникальны")
else:
    print("Неуникальны")
    
# 11_________________________________________________________________________________________
date_dict = {'year': 2024, 'month': 4, 'day': 14}
print(*date_dict.values(), sep="-")

# 12________________________________________________________________________________________
numbers = input()
list_number = numbers.split(sep=",")
tuple_number = tuple(list_number)
print(list_number, tuple_number)

# 13_____________________________________________________________________________________
students = {"Schultz", "Django", "Brunhilde", "Fritz"}
employees = {"Schultz", "Django", "Calvin", "Butch", "Fritz"}
print(students | employees, students.union(employees))
print(students & employees, students.intersection(employees))
print(employees - students, employees.difference(students))
print(employees ^ students, employees.symmetric_difference(students))

# 14_____________________________________________________________________________________
array = [
        [11, 12, 13, 14, 15],
        [21, 22, 23, 24, 25],
        [31, 32, 33, 34, 35],
        [41, 42, 43, 44, 45],
        [51, 52, 53, 54, 55]
    ]
array_transp = [list(i) for i in zip(*array)]
print(array_transp)

# 15___________________________________________________________________________________
n = int(input())

for i in range(0,n+1):
    print(f"X{i*'xx'}X")
