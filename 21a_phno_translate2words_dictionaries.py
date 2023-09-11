ph_num = input('Please enter your phone number: ')
numbers = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
output = ""
for digit in ph_num:
    output += numbers.get(digit, "!") + " "               # + " " is to give a space between two words at the o/p
print(f"Your phone number in words: {output}")