ages = [[1, 2, 3], [4, 5], [6, 7, 8]]
target = 5
found = False
for i in range(len(ages)):
    for j in range(len(ages[i])):
        if ages[i][j] == target:
            print(f"Found at index: [{i}][{j}]")
            found = True
            break
    if found:
        break

if not found:
    print("Not found")
