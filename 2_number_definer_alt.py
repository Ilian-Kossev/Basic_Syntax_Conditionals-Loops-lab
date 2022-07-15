number = float(input())
absolute_value = abs(number)
if number == 0:
    print("zero")
elif 0 < absolute_value <= 1:
    if number < 0:
        print("small negative")
    else:
        print("small positive")
elif 1 < absolute_value <= 1000000:
    if number < 0:
        print("negative")
    else:
        print("positive")
elif absolute_value > 1000000:
    if number < 0:
        print("large negative")
    else:
        print("large positive")