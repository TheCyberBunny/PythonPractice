#Errors vs Exceptions
#All exceptions are errors, but not all errors are exceptions

#Errors - problems that prevent the program from running correctly
#this is a syntax error; there is no 'handling' of this, we just have to fix it
#print "this is an error"

#errors will come with error messages to help diagnose the issue
#Syntax error, Indentation error, name error, value error, Type Error zero division error, etc.


#Exception - is raised during runtime and can be detected and handled using try-except
try:
    x = int("spaghetti")
except ValueError:
    print("Conversion has failed")

#try-except-else-finally
try:
    number = int(input("Enter a number: "))
    result = 10 / number

except ValueError:
    print("Invalid input. Please enter a valid integer.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

#it is a good idea to add a generic catch-all exception block to handle anything we have not thought of
except Exception:
    print("I have no idea how you got here")

else:
    # Runs only if NO exception occurs
    print(f"Result: {result}")

finally:
    # Runs no matter what (exception or not)
    print("Execution complete.")

#We can use the raise keyword to manually raise(throw) an exception
#y = -5

#if y < 0:
 #   raise Exception("Sorry, no negative numbers allowed")

#We can create custom exceptions by creating our own custom exception class
class MyCustomException(Exception):
    def __init__(self, message = "this is not the exception you are looking for"):
        super().__init__(message)


user_num = input("Please enter an integer")

if not type(user_num) is int:
    raise MyCustomException()
print(user_num)