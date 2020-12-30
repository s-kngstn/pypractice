with open("my_file.txt", mode="a") as file:
    contents = file.write("\nNew line.")
    print(contents)
