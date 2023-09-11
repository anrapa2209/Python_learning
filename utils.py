def find_max(numbers):
    maximum = numbers[0]
    for check in numbers:
        if check > maximum:
            maximum = check
    return maximum
