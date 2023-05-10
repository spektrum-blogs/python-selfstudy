#prints characters from position two to five
#starts from two and ends at position four. five not included
b = "Hello, World!"
print(b[2:5])

b = "Hello, World!" #go in reverse from H, since H is position 0.
print(b[-5:-2])

a = "Hello, World!"
print(a.upper())
b = "HELLO, WORLD!"
print(b.lower())

a = "Hello, World!"
print(a.replace("H", "L")) #replaces H with the word L

a = "Hello, World!" #complete string
print(a.split(",")) #this is done to remove the comma in between hello and world and show them as 2 individual strings
#if there is no comma in the string just type a.split()

#inorder to add integer into a string
a = "36"
b = "My name is John, I am {} years old"
print(b.format(a)) #format must be used to include int inside str

#not only int but any data type inside a string
c = 3
d = "goats"
e = 3.14
f = "I have {} {} under the price of {}"
print(f.format(c, d, e))

#both are same
a = "HELLO"
print(a.casefold())

b = "HELLO"
print(b.lower())

print(10 > 9)
print(4 < 6)
print(10 == 2)

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#to check whether an object is an integer or not
x = 5
print(isinstance(x, int))
