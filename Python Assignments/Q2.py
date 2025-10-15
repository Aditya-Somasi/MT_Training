ages = [25, "Aditya", 42.5, "Advanced Analytics", 100, 3.1415, "ages Science", False, "2025", 7.0]
integer_count = 0
string_count = 0
float_count = 0


for item in ages:
    if type(item) == int:
        integer_count += 1
    elif type(item) == str:
        string_count += 1
    elif type(item) == float:
        float_count += 1
print("Number of integers:", integer_count)
print("Number of strings:", string_count)
print("Number of floats:", float_count)
