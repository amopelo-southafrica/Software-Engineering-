
text = input("Enter a string: ")

result_chars = ""

for i in range(len(text)):
    if i % 2 == 0:
        result_chars += text[i].upper()
    else:
        result_chars += text[i].lower()

print("\nAlternate characters upper/lower:")
print(result_chars)


words = text.split()


for i in range(len(words)):
    if i % 2 == 0:
        words[i] = words[i].lower()
    else:
        words[i] = words[i].upper()


result_words = " ".join(words)

print("\nAlternate words lower/upper:")
print(result_words)