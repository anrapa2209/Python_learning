print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)           #o/p will be a floating point number
print(10 // 3)          #o/p will be an integer
print(10 % 3)
print(10 ** 3)          #power
print(' ')
x = 10
#x = x + 3
#x += 3                 #assignment operator
x -= 3                  #assignment operator
print(x)
print(' ')
#operator precedence
x = 10 + 3 * 2              #BODMAS
x1 = 10 + 3 * 2 ** 2
x2 = (10 + 3) * 2 ** 2
print(x)
print(x1)
print(x2)
#order of precedence:
#paranthesis always takes priority
#exponentiation 2 ** 3
#multiplication or division
#addition or subtraction
print(' ')
x3 = (2 + 3) * 10 - 3
print(x3)