not_john = []

name = input("Enter your name: ").strip().lower()

while name != "john":
    not_john.append(name)
    name = input("Enter your name: ").strip().lower()

print(f"Incorrect names: {not_john}")

