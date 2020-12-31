with open("my_file.txt", mode="a") as file:
    contents = file.write("\nWill it work? lets find out.")
    print(contents)
