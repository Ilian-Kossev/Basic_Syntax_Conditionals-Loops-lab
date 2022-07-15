string_1 = input()
string_2 = input()
new_string = 0
for index in range(0, len(string_1)):

    for index_2 in range(index, index + 1):
        if not string_1[index] == string_2[index_2]:
            new_string += string_2[index_2]

    print(new_string)

