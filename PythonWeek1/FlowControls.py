#Control flow statements in Python

#For

LoopPets = ["Fluffy", "Wonton", "Ash", "Wontina", "Wontessa"]

#loops through a collection of items
# for x in collection, do something
for pet in LoopPets:
    print(pet)



#While

#good for execution while a condition is true
count = 0
while (count < 5):
    print("From the while loop")
    count += 1 #remember += is our shorthand operator for count = count + 1

#Note, we can nest loops and mix and match them
#BUT, if you find yourself using 3 or more loops deep, there is likely a better way

#If-else

#We can check a condition and execute a block of code if it's true and another block if false
#Be careful! Python relies on indentation where other languages often use curly braces
#Always check your indents!
cheese = 6
if cheese > 5:
    print("Cheese is the greatest!")
else:
    print("Cheese is not the greatest")

#we can check multiple conditions using elif
#this will execute the FIRST true block and skip the rest
#Good for checking multiple mutually exclusive conditions

score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
#Else catches anything that is not caught by previous conditions
else:
   print("Grade: F")

#shorthand if
a = 9
b = 3

if a > b: print("a is greater than b")

#Shorthand if else
print("a is my favorite") if a > b else print("b is my favorite")

#Multiple conditions using logical operators AND OR NOT
c = 70
if a > b and c > a:
   print("Both conditions are true!")

if a > b or c < a:
   print("At least one condition is true")

if not a < b:
   print("a is not greater than b")

if a > 5:
    print("a is more than 5")
    if a > 10:
      print("and more than 10")
    else:
       print("but not more than 10")

#Match-case (Known as a switch statement in other languages)
choice = input("select a number between 1 and 3")

match choice:
   case "1":
      print("You picked number 1!")
   case "2":
      print("You picked number 2!")
   case "3":
      print("You picked number 3!")    
   case _: #the default case if none of the above are true
      print("You did not follow directions")   
