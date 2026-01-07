#Functions are how we package useful functionality into reusable blocks to use when needed

#Creating a function - we use the 'def' keyword, name the function, give it parameters
#then we write the code we want the function to execute

#function with 2 parameters
def addition_function(x:int, y:int):
    return x + y

#no parameters function
def bark():
    print("woof")

#calling functions
sum = addition_function(9, 10)
print(sum)
bark()

#Putting strings instead of integers will output strings
print(addition_function("Purple", "Green"))

#Scopes
# are of the code where an object/variable/function can be called upon and used

#Local: variables declared inside a block of code are only available inside that block
def local_variable():
    msg = "hi y'all"
    print(msg)

    #Enclosed: function is enclosed within another function
    #this function can access variables from the outer function
    def enclosed():
        msg = "enclosed hi y'all"
        print(msg)
    
    enclosed()
    print(msg)

local_variable()

#print(msg)    


#Global: accessed anywhere within the file they are declared in 
#as well as other files if they are brought in via import
MyCat = "Wonton"

#Built-in: defautl python methods and all the keywords live here. can be accessed from anywhere


#Arrays are not technically built into Python, we have to import the array module
#contain elements of the same type, stored sequentially and indexed from 0
#array(typecode, initializer)

# typecode: This is a single character that specifies the type of data that will be stored in the array. For example:
# 'i': Signed integer (4 bytes)
# 'f': Floating point (4 bytes)
# 'd': Double precision floating point (8 bytes)
# 'b': Signed integer (1 byte)
# 'u': Unicode character (2 bytes)
# 'l': Signed long integer (4 bytes) (platform-dependent)
# initializer: This is an optional parameter that initializes the array with elements. It can be a list, a tuple, or any iterable containing the initial values for the array.

import array
IntArray = array.array( 'i', [1, 2, 14, 6, 3, 99])

print(IntArray[2])
subset = IntArray[0:4]
print(subset)

for i in IntArray:
    print(i)

#find the length
print(len(IntArray))

#sorts in ascending order
print(sorted(IntArray))


#Lambda functions AKA Anonymous functions
#small, single-line functions that can have any number of arguments, but only one expression
#lambda args: expression

add = lambda x, y: x + y
print(add(3, 4))

Pokedex = [
    ("Bulbasaur", 1),
    ("Lapras", 131),
    ("Eevee", 133),
    ("Cubone", 104),
    ("Gengar", 94)
]
Pokedex.sort(key=lambda x: x[1], reverse = True)
print(Pokedex)
