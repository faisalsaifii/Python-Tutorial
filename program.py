# Single line comment
'''
    Multi Line Comment
'''

# print() -> prints stuff
# Separation of strings is through <space> by default
print(10 , "Blablabla")
# Use sep argument to change the separating character being used
print("1", "2", sep=",")
# By default the end is \n
# Use end argument to change the ending of print function
print("First line", end=" ")
print("Next line")

# // -> Removes decimal digits
print(7//2)
# % -> Remainder
print(3%2)
# ** -> Exponent(^)
print(5**2)
# Python handles numbers using BEDMAS
print((1-2)+2*6/2**2)

# VARIABLES
# Global -> Can be accessed anywhere in the program
# Local -> Declared insider a function which can only be used inside the function
# Naming Convention: Includes letters, numbers, underscore (CANNOT START WITH A NUMBER)
_Variable12 = 1
print(_Variable12)

# Multiple Declarations
x,y = 1,2

# Swapping Variables
x,y = y,x

# STRINGS
# Contained in " " or ' '
# Use " " when your string contains ' ' and vice versa
print("I'm Faisal")

# \ before a char -> Escaping a character in a string
print('I\'m Faisal')

# r -> Bypassing \n while using print()
print(r"this is not on a \new line")

# Adding Strings
firstName = "Faisal"
print(firstName + " Saifi")
# Multiplying Strings
print(firstName + ' ' * 5)
# Slicing Up Strings
print(firstName[0])
# You can also go from left to right
print(firstName[-1]) # Last Character is -1 then -2 and so on
print(firstName[2:5]) # slice up a section of a string
print(firstName[:]) #start from beginning to end
len(firstName) # Gives length of string

#LISTS
players = [1,2,3,4,5] #Initialise a list
print(players[2]) #Print specific element of a list
players[2] = 23 #Initialise element of list
print(players) #Print the whole list
print(players + [9,8,7,6]) #Add lists
players.append(120) #Add element to a list
print(players) 
print(players[:2]) #Print Portion of list
players[:3] = [0,0,0] #Initialising portion of list
players[:2] = [] #Delete items from list
players[:] = [] #Empty entire list
print(players)

#if statement
age=27
if age<21:
    print("No beer for you!")
else:
    print("Take all you want!")
name = "Potter"
if name == "Potter":
    print("You are a wizard Harry");
elif name == "Ron":
    print("Bloody Hell Harry!")
else:
    print("Wait a minute, who are you?")

# for loop
foods = ["burger" , 'pizza' , 'pasta']
for f in foods[:2]:
    print(f)
    print(len(f))
# range
for x in range(3):
    print(x)
for x in range(5,10):
    print(x)
for x in range(10,50,5): #High Limit, Lower limit, increment
    print(x)

n=0
# while loop
while n < 3:
    print(n)
    n+=1

# break keyword
x=26
for n in range(101):
    if n is x:
        print("Yep! ", n, " is the number")
        break

# continue keyword
for n in range(101):
    if n is x:
        continue

# Functions
def func(parameter1=0, parameter2 = 0): # = 0 -> Setting default value for parameter
    print(parameter1, "This is printed by a function\n")
    return parameter1 + parameter2 # RETURNING VALUES

# Parameters -> Placeholders
# Arguments -> Actual values that get passed through

# Calling a function
x = func(10) # 10,5 -> Arguments

# KEYWORD ARGUMENTS
# Passing a specified argument
x = func(parameter2=5)

# FLEXIBLE NUMBER OF ARGUMENTS
# Common Practice: Name flexible argument "args"
def flexible_arg(*args):
    print(args)

flexible_arg(1,2,3,4,5)

# UNPACKING ARGUMENTS
def function_that_takes_three_args(arg1,arg2,arg3):
    print(arg1,arg2,arg3)
# The list's elements are gonna be put into all the entries
# Note: The number of elements passed must be equal to the number of arguments
arglist = [1,2,3,4]
# function_that_takes_three_args(*arglist) -> Error
function_that_takes_three_args(*arglist[:3])