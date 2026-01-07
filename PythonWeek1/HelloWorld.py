print("Hello, World!")

x = 5
MyString = "This is my string!"
MySingleQuoteString = 'this is also a valid string'

#by default, the print function ends with a new line
print(x)
print(MyString)

print(x, MyString)

print(x); print(MyString)

#This will throw an error
#print(x) print(MyString)

#we can do math in print functions
print(x + 9)

#mix data types
print("I have", 7, "cats.")

#variable types can be changed after they have been set
z = 4
z="Paul"

print(z)

#Casting lets us specify the data type of a variable
a = str(9) #a will be '9'
b = int(9) #b will be 9
c = float(9) #c will be 9.0

#the type() function will return the data type of a variable
print(type(a))

#variables are case-sensitive
A = 12
print(a, A)

#we can assign multiple variables in one line
X, Y, Z = "Pink", "Green", "Blue"
print(X)
print(Y)
print(Z)

#we can also assign the same value to multiple variables at once
dog = DOG = Dog = "Beagle"

#Collections - variables that hold multiple values
#Lists, Tuples, Sets, and Dictionaries are examples of Collections in Python

"""list is a collection that is ordered and changeable and allows duplicate values
Tuple is a collection that is ordered and UNchangeable and allows duplicate values
Set is a collection that is unordered, unchangeable, and unindexed. No duplicate values
Dictionary is a collection that is ordered and changeable but doesn't allow duplicate values"""

#Lists use square brackets and can contain different data types
#Python sees lists as objects with the data type 'list'
fruits = ["Orange", "Strawberry", "Apple"]
Or, St, Ap = fruits
print(Or)
print(St)
print(Ap)

stuff = ["purple", 32, False, "Green", 101.4]

#len() determines the length of the list
print(len(fruits))

#type() tells us the data type of the list
print(type(fruits))

#access an item in the list using the item's index
print(fruits[1])
#or use negative indexing to start from the end
print(fruits[-1])
#Or a range of indexes!
print(fruits[1:2])

#add an item to the end of the list
fruits.append("Grapes")
print(fruits)
#or at a specific index
fruits.insert(2, "Kiwi")
print(fruits)

#Tuples
#Tuples can contain different data types and are defines as objects of the data type 'tuple'
MyAnimalTuple = ("Cat", "Dog", "Bird", "Fish")
print(MyAnimalTuple)

#the len() function works for tuples too
print(len(MyAnimalTuple))

#Since tuples are immutable(unchangeable) we cannot use the append() function
#Instead, we would need to convert it to a list
AnimalList = list(MyAnimalTuple)
AnimalList.append("Frog")
print(AnimalList)

#Sets
#Sets are created using curly braces
Colors = {"Orange", "Blue", "Yellow"}

#Sets can use the add() and remve() functions for adding and removing elements
Colors.add("Pink")
Colors.remove("Orange")
print(Colors)

#Sets support intersection, difference, and union
SecondSet = {"Burger", "Fries", "Milkshake"}
intersection_set  = Colors & SecondSet
print("Intersection: ", intersection_set)

difference_set = Colors - SecondSet
print("Difference: ", difference_set)

union_set = Colors | SecondSet
print("Union: ", union_set)

#Dictionary
#Dictionaries are defined as key-value pairs with curly braces and separated by a colon
#Pairs are separated by commas
#The first value is treated as the key and the second as the value in each pair
FoodDictionary = {"Sushi": "Fish", "Burger": "Beef", "Pizza":"Pepperoni"}

#values() will return a list of all values in the dicitonary
FoodDictionary.values()

#The value of a specific item can be changed by referring to its key
FoodDictionary["Sushi"] = "Rice"

#We can add items by using a new index key and giving it a value
FoodDictionary["Pickle"] = "Cucumber"
print(FoodDictionary)

#we can see if a key exists in the dictionary
if "Burger" in FoodDictionary:
    print("Yes, there is a burger key in the dictionary")



#Operators
#These are symbols that define operation behaviors between data types

#+ can add together two values
print(11 + 3)
print("Cherry" + "Pie")

#Arithmetic operators support mathematical functions
# +, -, *, /, %, **(exponentation), //(floor division)

#Assignment operators assign values to variables
# =, +=, -=, *=, /=, etc.

#Comparison operators compare two values and will return a boolean
# ==, !=, >, <, >=, <=

#Logical Operators combine conditional statements
# and, or, not


#Getting User Input using the input() function

print("Plese enter your name")
name = input()
print(f"Hello {name}")

color = input(f"What is your favorite color, {name}?")
print(f"I like {color} too!")

