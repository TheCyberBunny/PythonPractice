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
