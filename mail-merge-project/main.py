import time
# Open document that needs to be automated
with open("./Input/Letters/starting_letter.docx") as file:
    contents = file.read()

# Create a list of names from a name data text file
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

name_list = []
# append names to a list and create a birthday
# invite for each name in the list
for name in range(len(names)):
    names_list = names[name].replace("\n", '')
    name_list.append(names_list)
    birthday_invites = contents.replace("[name]", name_list[name])
    print("Printing invites...")
    time.sleep(0.5)
    print(birthday_invites)
    with open(f"./Output/ReadyToSend/letter_for_{name_list[name]}.docx",
              mode="w") as file:
        file.write(birthday_invites)

print("All files have been created")
