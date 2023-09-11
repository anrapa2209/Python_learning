message = input(">")
words = message.split(' ')
emojis = {
    ":)": "Happy",
    ":(": "Sad",
    "<3": "Heart"
}
output = ""
for word in words:                  #get each word and map it to an emoji
    output += emojis.get(word, word) + " "
print(output)