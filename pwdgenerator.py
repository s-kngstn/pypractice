import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Password Generator")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Random Letter
ran_letter = random.sample(letters, nr_letters)
str1 = ''.join(ran_letter)

#Random numbers
ran_number = random.sample(numbers, nr_numbers)
num1 = ''.join(ran_number)

#Random symbols
ran_sym = random.sample(symbols, nr_symbols)
sym1 = ''.join(ran_sym)

#Combine str1, num1, and sym1 together in a list
pw_shuffle = ran_letter + ran_number + ran_sym

#Randomize the list
random.shuffle(pw_shuffle)

#Change randomized list into a string
passwd = ''.join(pw_shuffle)
#Print random password string
print("Password created: ")
print(passwd)
