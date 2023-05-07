print("Hello World!")

if 5 > 2:
  print("Five is greater than Two")
else:
  print("None")

#this is a comment- a single line comment
"""
this is also a comment
written in 
multiple lines
"""

x = 5
y = "John"
print(x)
print(y)

#at first x is declared as 4 then, x is newly declared as John. So x's declaration changes when printed
x = 4
x = "John"
print(x)

x = str(3)
y = int(4)
z = float(5)
print(x)
print(y)
print(z)

#prints the data type of the variable declared
x = 5.0
y = "John"
print(type(x))
print(type(y))

#assign multiple variables in a single line
x, y, z = "Red", "yellow", "Green"
print(x)
print(y)
print(z)
#whereas x = y = z = "Orange" assigns same value to multiple variables in a single line

#assigning a list
fruits = ["apple", "banana", "orange"]
#now unpacking the list
x, y, z = fruits
#now printing the list
print(x)
print(y)
print(z)

#printing multiple variables in a single print command
x = "I"
y = "am"
z = "Nobody"
print(x, y, z)
#we can also use print(x + y + z) instead of above command

#print(x + y  + z) doesn't work exacty the same when it comes to int
x = 2
y = 5
print(x + y) #it adds the integers

#also, print(x + y) doesn't work for when x is an int and y is str

#global variable
x = "awesome" #here x is a global variable it can be called inside a function
def myfunc():
    print(x + " programming language")
myfunc()

x = "awesome" #here x is a global variable
def myfunc():
  x = "fantastic" #here x is declared inide the function. so global var won't be called
  print(x + " programming language") #output will be fantastic programming language
myfunc()
print(x + " programming language") #this print statement is outside the function so global var will be used
#output will be awesome programming language

#use of global keyword
def myfunc():
  global x #global keyword should always be first. missing it will cause error.
  x = "awesome" #here x is declared inside the function but global keyword is used so this var can be used globally
myfunc()
print(x + " programming language") #x inside the fuction is used globaly so it will be printed here

x = "fantastic" #x dlecared as global var
def myfunc():
  global x #here x = awesome is declared as the new global var so x = awesome is used globally not fantastic 
  x = "awesome"
myfunc()
print(x + " programming language") #eventhough fantastic is declared globally, global var is declared inside the function so new global var will be used
#hence output will be awesome programming language
