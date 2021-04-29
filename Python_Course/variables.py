# -- Strings --

FirstName = "Tegster"
LastName = "Singh"
Fullinfo= "Tegster loves to program in Python"
print(FirstName)
print(LastName)

print(FirstName * 2)


# -- Numbers and Floats --

age = 26
height = 72

applePrice = 10
discount = 0.3

result = applePrice * (1 - discount)

print(result)


# -- Changing variables values --
# Variables are names for values.

a = 25
b = a

# Here we've given the value '25' the names 'a' and 'b'.

print(a)
print(b)

b = 22

# Here we've given the value '22' the name 'b'. The name 'a' is still a name for '25'!

print(a)
print(b)

#Print the data type of the variable x:
x = 15
print(type(x))

#String Formatting

#named indexes:
String1 = "My name is {firstname}, I'm {age}".format(firstname = "Tegster", age = 26)
#numbered indexes:
String2 = "My name is {0}, I'm {1}".format("Tegster",26)
#empty placeholders:
String3 = "My name is {}, I'm {}".format("Tegster",26)

print(String1)
print(String2)
print(String3)

#Boolean Expression and assigning Boolean Expressions to Variables

print(10 > 9)
print(10 == 9)
print(10 < 9)

# We can assign the result of experession result to a variable
y = (10 == 10)
x = (10 == 9)

print(x)
print(y)
