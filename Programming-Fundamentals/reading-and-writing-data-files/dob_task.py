names_list = []
birthdate_list = []

with open("DOB.txt", "r") as file:
    for line in file:
        words = line.split()
        names_list.append(" ".join(words[:2]))        # first 2 words
        birthdate_list.append(" ".join(words[2:]))    # last 3 words (or however many remain)

# Print nicely
print("Name\n" + "\n".join(names_list))
print("\nBirthdate\n" + "\n".join(birthdate_list))

    
