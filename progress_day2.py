#numbers- int, float, complex
x = 2
y = 3.4
z = 1j #complex numbers are written with only j as the imaginary part

print(type(x))
print(type(y))
print(type(z))

x = 1 #int
y = 2.8 #float
z = 1j #complex

a = float(x) #convert int to float
b = int(y) #convert float to int
c = complex(x) #convert int to complex

print(a, b, c)
print(type(a))
print(type(b))
print(type(c))

#generating a random number
import random #importing random module
print(random.randrange(0, 7)) #printing a random nummber between 0 to 7

#how to convert an int/float/complex into str?
x = str(2)
y = str(3.14)
z = str(1j)
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

a = "hello" #single line string
print(a)

#multiple lines string
b = """     
       vneqiovnive
       vnwionwiiwi
       oirghiornii
    """
print(b)
print(type(a))
print(type(b))

#strings as arrays
a = "hello"
print(a[1]) #since first character starts from 0 the output will be 'e'

#looping through strings
for x in "banana":
  print(x)
#this prints each letter of the word banana one by one in new lines

#finding string length
a = "Hello World"
print(len(a)) #this prints length of the string. (including spaces)

#check string
a = "hello world"
print("hello" in a) #this cheks whether the word is present in the string or not and sends boolean answer

#check string with condition
a = "hello world apples bananas carrots"
if "bananas" in a:
  print("Yes, bananas is present in the string")
else:
  print("No")

a = "hello world apples bananas carrots"
if "dosa" in a:
  print("Yes, bananas is present in the string")

else:
  print("No")

a = "hello world apples bananas carrots"
if "channa" not in a:
  print("No, channa is not present in the string")
