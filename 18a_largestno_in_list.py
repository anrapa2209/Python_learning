numbers = [56, 80, 5, 9, 111, 22, 13]
largest = numbers[0]                    #initially assume that the first item in this list is the largest no.
for check in numbers:
    if check > largest:
        largest = check
print(largest)


