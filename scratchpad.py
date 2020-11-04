print(1/2)

a = 5
print(a)

a = 30

my_greeting = 'hello my name is sam'

print(my_greeting + ' I am ' + str(a) + ' years old.')

my_income = 100

tax_rate = 0.1

my_taxes = my_income * tax_rate

print(my_taxes)

print("hello \nworld one two") #new line
print("hello \tworld one two") #new tab
###### Check the length of a string with len() ##################
print(len("hello")) # len() prints length of string - this includes spaces
# -------------------------------------------- #
###########  string indexing and slicing #####################
# -------------------------------------------- #
mystring = "Hello World"

print(mystring[0]) #this prints the first character of the string 'H'

print(mystring[8])
print(mystring[-1]) # -1 will always produce the last character of a string

mystring = "abcdefghijk"

print(mystring[2:]) #slices string from string with index of 2 onward 'cdefghijk'
print(mystring[:3]) #slices string up to index of 3 'abc'

print(mystring[3:6]) #slices starting position and ending position 'def'
print(mystring[1:3])

print(mystring[::2]) #jumping in stepsize 'acegik'

print(mystring[::-1]) #reverses string
# -------------------------------------------- #
###### immutability - strings are immutable ######
# -------------------------------------------- #
#concatenation

name = "Sam"

print(name[1:])

name2 = "P" + name[1:]

print(name2)

x = "Hello world"

greeting = x + ", isn't it beautiful outside today?"
print(greeting)

sleepy_letter = "z"

sleeping = sleepy_letter * 10

print(sleeping)
# -------------------------------------------- #
############# some useful built in methods for Python #################
# -------------------------------------------- #
x = 'Hello World'

x_cap = x.upper() #uppercase letters

print(x_cap)



print(x.split()) # splits up by whitespace by default and puts them into an array[list]

print(x.split("o")) #splits up by letter o
# -------------------------------------------- #
############# Formatting with the .format() method ###############################
# -------------------------------------------- #
print("this is a string {}".format("INSERTED"))

print("The {} {} {}".format('fox', 'brown', 'quick'))

print("The {2} {1} {0}".format('fox', 'brown', 'quick'))


print("The {q} {b} {f}".format(f = 'fox',b = 'brown',q = 'quick'))

result = 100/777

print("The result was {r}".format(r = result)) #prints The result was 0.12897001287001287

print("The result was {r:1.2f}".format(r = result)) #prints The result was 0.13

#String literal newer .format() method similar to Javascripts template literal method --  Comes with Python 3.6^
name = "Jose"

print(f"His name is {name}") #prints "His name is Jose"

name = "Sam"
age = 3

print(f"{name} is {age} years old")
# -------------------------------------------- #
################### Lists (Arrays) feat. append, pop, sort & reverse methods ############################
# -------------------------------------------- #
my_list = [1,2,3]

## Check tghe length on a list by using the len() function

len(my_list)
print(len(my_list)) # prints 3


mylist = ['one', 'two', 'three']
print(mylist[1]) # prints 'two'
print(mylist[1:]) # slices and starts at index 1 and goes until the end === 'two', 'three'

#concatenate lists together
another_list = ['four', 'five']

joined_lists = mylist + another_list

print(joined_lists)

joined_lists[0] = 'ONE'

print(joined_lists)

## ADD NEW ITEM TO END OF A LIST(ARRAY)

joined_lists.append('six') ## append only takes ONE argument

print(joined_lists)

joined_lists.append('seven') ## append only takes ONE argument

print(joined_lists)

## REMOVE the ITEM at END OF A LIST(ARRAY)

joined_lists.pop()

print(joined_lists)

# TO REMOVE ANY ITEM FORM AN ARRAY JUST INCLUDE THE INDEX NUMBER INSIDE OF THE PARENTHESIS

print(joined_lists.pop(0)) # --> removes 'ONE' from the list(array)

print(joined_lists)
# -------------------------------------------- #
##### SORTING LISTS ####
# -------------------------------------------- #
new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4,1,8,3] 

new_list.sort()

sorted_list = new_list

print(sorted_list)
# -------------------------------------------- #
#### REVERSING LISTS ####
# -------------------------------------------- #
num_list.sort()

rnum_list = num_list

rnum_list.reverse()

print(rnum_list)
# -------------------------------------------- #
#### DICTIONARIES ####
# -------------------------------------------- #
my_dict = {'key1' : 'value1', 'key2' : 'value2'}

print(my_dict['key1']) #prints value1

# good use for dictionaries would be for prices in a store

prices_lookup = {'apples' : 2.99, 'oranges' : 1.99, 'milk': 4.50}

print(prices_lookup['milk']) #prints 4.50

### Dictionaires can also hold lists and other dictionaries

d = {'k1':123, 'k2':[1,0,4,5,6,7], 'k3':{'insideKey':100}}

print(d['k2'][-1]) # prints 7

#assign a new dictionary

d = {'k1':100, 'k2':200}

d['k3'] = 300

print(d)

#overwrite a key value

d['k1'] = 'NEW VALUE'

print(d)
# USEFUL DICTIONARY METHODS

d = {'k1':100, 'k2':200, 'k3':300}

print(d)

# all values or all keys

print(d.keys())
print(d.values())
# -------------------------------------------- #
#### Tuples ######
# TUPLES ARE IMMUTABLE
# -------------------------------------------- #
t = (1,2,3)

mylist = [1,2,3]

print(type(t)) # class: tuple
print(type(mylist)) # class: list

# check length
print(len(t)) # prints 3

# you can add different data types to Tuples

t = ('one',2, 3.475)
print(t)

t[-1] #grabs last item
t[0] #grabs first item

# THERE ARE WAAY LESS METHODS AVAILABLE FOR TUPLES THAN LISTS

t = ('a','a','b','alphabet')
#The count method counts the amount of times an identical string or number is in your tuple
print(t.count('a')) #prints 2

#The index method shows you the first time a string or number is introduced into the tuple via its index number
print(t.index('a')) #prints 0

#WHAT ARE THE BENEFITS OF A TUPLE?? DATA INTEGRITY

t = (1,2,['a','c'])

# YOU CANNOT CHANGE ELEMENTS IN A TUPLE BC TUPLES ARE IMMUTABLE
# BUT YOU CAN CHANGE LISTS INSIDE TUPLES

t[2][0] = 'dog'

print(t[2][0])
print(t)
# -------------------------------------------- #
####### sets ###########
# -------------------------------------------- #
myset = set()

myset.add(1)

print(myset) # prints {1} --> it LOOKS like a dictionary but it is NOT.. Dictionaries have key:value pairs and sets do not.

myset.add(2)

print(myset) #prints {1,2}

myset.add(2) # -> if you try to add a value that is already in the set it will not repeat it (see below)

print(myset)  #prints {1,2} 

mylist = [1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3]

print(set(mylist)) # prints {1,2,3}


my_list =[2,2,2,2,2,1,1,1,1,3,3]
print(set(my_list)) # prints {1,2,3} <--- why does it print this if it is 'unordered'

print(set('Mississippi')) #prints {'s', 'p', 'M', 'i'}
# -------------------------------------------- #
### BOOLEANS ###
# -------------------------------------------- #
# Make sure to capitalize True and False or Python wont recognize it as a bool

print(1 > 2) # prints False
print(1 == 1) # prints True

b = None # makes b a None data type

print(((((100.25 / 2) + 50.125) * 2) ** 2) - 40100.0)

print(type(3 + 1.5 + 4))

l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

print(l_one[2][0])
print(l_two[2]['k1'])
# -------------------------------------------- #
#### comparison operator ######
# -------------------------------------------- #
# chaining comparison operators

1 < 2 and 2 > 3

'h' == 'h' and 2 == 2 # both need to be true

1 == 1 or 2 == 3 # just needs one to be true

not 1 == 1 # returns false -> just returns the opposite bool
# -------------------------------------------- #
############ if statements ###############
# -------------------------------------------- #
if 3 > 2:
    print('ITS TRUE') #prints'ITS TRUE'

hungry = False

if hungry:
    print('Feed Me')
else:
    print('Im not hungry') #prints 'Im not hungry'

loc = 'Auto Shop'

if loc == 'Auto Shop':
    print('Cars are cool')
elif loc == 'Bank':
    print('Money is cool')
elif loc == 'Store':
    print('Welcome to the store!')
else:
    print('I dont know much')
# -------------------------------------------- #
######## For Loops #############
# -------------------------------------------- #
## do NOT use list by itself as a variable name b/c its a built in python keyword

mylist = [1,2,3,4,5,6,7,8,9,10]

for jelly in mylist:
    print(jelly) 
# This prints
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
for jelly in mylist:
    print('hello') 
# This prints
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello

for num in mylist:
    # check for even numbers
    # if the number in mylists mod(modulo) of 2 is equal to zero, print that number 
    if num % 2 == 0:
        print(num) 
    else:
        print(f'Odd Number: {num}')
# This prints
# Odd Number: 1
# 2
# Odd Number: 3
# 4
# Odd Number: 5
# 6
# Odd Number: 7
# 8
# Odd Number: 9
# 10


mylist = [1,2,3,4,5,6,7,8,9,10]
list_sum = 0
for num in mylist:
    list_sum = list_sum + num
    print(list_sum) # prints a running tally seen below:
# 1
# 3
# 6
# 10
# 15
# 21
# 28
# 36
# 45
# 55
print(list_sum) #prints 55 which is  equivalent to print 1+2+3+4+5+6+7+8+9+10

mystring = 'Hello World'
for letter in mystring:
    print(letter)
#This prints:
# H
# e
# l
# l
# o

# W
# o
# r
# l
# d

# SHORTER SYNTAX THAN ABOVE
for letter in 'Hello World':
    print(letter)
    #This prints:
# H
# e
# l
# l
# o

# W
# o
# r
# l
# d 

for _ in 'Hello':
    print('Cool!')
# _ syntax if you dont intend to use the variable and need to iterate over something
# prints
# Cool!
# Cool!
# Cool!
# Cool!
# Cool!

cars = ['ford', 'taxi', 'truck', 'BMW']
for types in cars:
    print(types)
#prints
# ford
# taxi
# truck
# BMW
## ----------------- ##
tup = (1,2,3)

for item in tup:
    print(item)
#prints
# 1
# 2
# 3

my_tuple_pairs_list = [(1,2),(3,4),(5,6),(7,8)]
len(my_tuple_pairs_list) #prints 4
for item in my_tuple_pairs_list:
    print(item)
#prints
# (1, 2)
# (3, 4)
# (5, 6)
# (7, 8)

#tuple unpacking
for a,b in my_tuple_pairs_list:
    print(a)
    print(b)
#prints
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8

mylist = [(1,2,3),(5,6,7),(8,9,10)]

for item in mylist:
    print(item)
# prints
# (1, 2, 3)
# (5, 6, 7)
# (8, 9, 10)

for a,b,c in mylist:
    print(b)
#prints
# 2
# 6
# 9

## ITERATING THROUGH A DICTIONARY USING FOR LOOPS
d = {'k1':1,'k2':2,'k3':3}

for item in d:
    print(item)
#prints
# k1
# k2
# k3

#this only prints the keys and not the values
#if you want both keys and values do as below

for item in d.items():
    print(item)
#prints
# ('k1', 1)
# ('k2', 2)
# ('k3', 3)

for item in d.values():
    print(item)
#prints
# 1
# 2
# 3

for key,value in d.items():
    print(key, value)
#prints
# k1 1
# k2 2
# k3 3

# -------------------------------------------- #
#### WHILE LOOPS ####
# -------------------------------------------- #
# common example would be --> WHILE my dogs are hungry, keep feeding my dogs

# while some_bool_condition:
#   do something

# You can also combine while loops with else statements:

# while some_bool_condition:
#   do something
# else:
#   do something different  

x = 0

while x < 5:
    print(f'The current value of x is {x}')
#   x = x + 1 # <-- remember to include this or you will find yourself in an infite while loop of 0,0,0,0,0,0ssss!!!!!
    x += 1 # <-- better syntax but same as directly above
else:
    print('X IS NOT LESS THAN 5')
# prints
# The current value of x is 0
# The current value of x is 1
# The current value of x is 2
# The current value of x is 3
# The current value of x is 4
# -------------------------------------------- #
#### THREE USEFUL KEYWORDS TO USE WITH LOOPS IN PYTHON ######
# break, continue, pass
# we can use break continue and pass statements in our loops to add additional functionality for various cases. The three statements are defined by:
# break: breaks out of current closest enclosing loop
# continue: Goes to the top of the closest enclosing loop.
# pass: does nothing at all.

x = [1,2,3]

for item in x:
    #comment
    pass
#kind of like a placeholder to prevent syntax errors.

mystring = 'Sammy'

for letter in mystring:
    if letter == 'a':
        continue
    print (letter)

# prints
# S
# m
# m
# y

for letter in mystring:
    if letter == 'a':
        break
    print (letter)

# prints
# S

x = 0

while x < 5:
    if x == 2:
        break
    print(x)
    x += 1
# prints
# 0
# 1
print('--------------------')
print('SOME USEFUL BUILT IN FUNCTIONS AND OPERATORS')
# -------------------------------------------- #
###  SOME USEFUL BUILT IN FUNCTIONS AND OPERATORS #####
# -------------------------------------------- #
## RANGE FUNCTION
# -------------------------------------------- #
mylist = [1,2,3]

for num in range(3,10):
    print(num)
#prints
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# you could also include a step size (3,10,step-size goes here)
for num in range(0,10,2):
    print(num)
#prints
# 0
# 2
# 4
# 6
# 8

#using range as a generator to create lists or tuples --> more effient than having the whole list typed out in memory
list(range(0,11,2))
#[0, 2, 4, 6, 8, 10]

tuple(range(0,20,2))
#(0, 2, 4, 6, 8, 10, 12, 14, 16, 18)
# -------------------------------------------- #
## ENUMERATE
# -------------------------------------------- #
index_count = 0

for letter in 'abcde':
    print(f'At index {index_count} the letter is {letter}')
    index_count += 1
# prints
# At index 0 the letter is a
# At index 1 the letter is b
# At index 2 the letter is c
# At index 3 the letter is d
# At index 4 the letter is e

index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1
# prints
# a
# b
# c
# d
# e
#ALTERNATIVE TO THE ABOVE :

word = 'abcde'
for item in enumerate(word):
    print(item)
# prints
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')

word = 'abcde'
for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

#prints
# 0
# a


# 1
# b


# 2
# c


# 3
# d


# 4
# e

mylist1 = [1,2,3,4,5,6]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]
# very useful for zipping together multiple lists
for item in zip(mylist1,mylist2,mylist3):
    print(item)
# print
# (1, 'a', 100)
# (2, 'b', 200)
# (3, 'c', 300)
list(zip(mylist1,mylist2))
# -------------------------------------------- #
## 'in' operator
# -------------------------------------------- #
## check if a value is in a list
'dog' in ['rat', 'pig', 'cat']
#returns false
x = 1
x in [1,2,3]
#returns true
'a' in 'dinosaur'
#returns true

# -------------------------------------------- #
### MATHEMATICAL FUNCTIONS #####
# -------------------------------------------- #

mylist = [10,20,30,40,100]

min(mylist) #returns 10
max(mylist) #returns 100

#shuffle
from random import shuffle

mylist = [1,2,3,4,5,6,7,8,9,10]

shuffle(mylist)
print(mylist) # prints [3, 2, 1, 9, 8, 6, 7, 10, 4, 5]

#randint (random integer)
from random import randint
randint(0,100)
mynum = randint(0,100)
print(mynum)
# -------------------------------------------- #
## GET USER INPUT
# -------------------------------------------- #
result = input('Enter a number here: ')

if result == 2:
    print('Well how did you guess? ;)')
else:
    print('Wrong')

print(int(result))





