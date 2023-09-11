numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
# print ('x' * x_count)                             #alternative way without nested loop, imagining in Python, you cannot multiply a str by int
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
