number = int(input())

for num in range(1, number + 1):
    if num > 1:
        print()
    for num_1 in range(1, num + 1):
        print(f"*", end='')
for num_2 in range(number - 1, 0, -1):
    print()
    for num_3 in range(1, num_2 + 1):
        print(f"*", end='')

