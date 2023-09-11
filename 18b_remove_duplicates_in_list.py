numbers = [22, 9, 96, 25, 13, 8, 94, 100, 25, 100]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
numbers = uniques
print(numbers)