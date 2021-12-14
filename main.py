with open(file="./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()

for index in range(len(names)):
    names[index] = names[index].strip("\n")

with open(file="./Input/Letters/starting_letter.txt") as template_letter:
    template = template_letter.read()

for name in names:
    stripped_name = name.strip("\n")
    new_letter = template.replace("[name]", stripped_name)
    with open(file=f"./Output/ReadyToSend/{name}.txt", mode="w") as custom_letter:
        custom_letter.write(new_letter)
