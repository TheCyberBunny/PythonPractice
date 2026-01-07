#Python is an OOP lanugage (Object-Oriented Programming)

#we can create custom classes and generate objects based on those classes

class Dog:
    #In Python, we override __init__() to create our constructor
    #Notice it has the double underscore
    #we pass in 'Self' which references our freshly created object in our __init__
    #we take in arguments that are our classes attributes
    #Then we set them inside the __init__
    #We can also set default values
    def __init__(self, name, age, breed, color="brown"):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color

    def bark(self): #pass in the self object to access self attributes (remember our scopes!)
        return f"{self.name} barked at a car"
    
    #__str__ acts as my toString() method
    def __str__(self):
        return f"My name is {self.name}, I am a {self.color} {self.breed}"


Wonton = Dog("Wonton", 2, "Poodle", "White")
print(Wonton)

print(Wonton.bark())

#Pillars of OOP: Abstraction, Inheritance, Polymorphism, and Encapsulation
#Abstraction - the idea of showing only what the user needs to know and hiding the implementation details
#inheritance - child classes can reuse and extend the behavior of a parent class
#Polymorphism - 'many forms' meaning one interface but multiple implementations
#Encapsulation - the practice of bundling data/attributes and methods into a single unit and restricting access to some of the object's components


#Inheritance - lets us define classes that inherit from another class
#Parent class is the class being inherited from
#child class is the class that inherits from another (also called a derived class)



class Animal:
    def __init__(self, name, age):
        self.name = name

        #Encapsulation is about protecting data inside of a class
#We can make private properties using a __ prefix
        self.__age = age

    #To modify a private property, we need getter/setter methods
    def get_age(self): return self.__age
    def set_age(self, age): 
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

    def speak(self):
        return f"{self.name} has made a noise"
    

class Cat(Animal):
    def __init__(self, name, age, breed, color, hairLength):
        #call the parent class constructor using the super() method
        super().__init__(name, age)
        self.breed = breed
        self.color = color
        self.hairLength = hairLength

    def scratch(self):
        return f"{self.name} has scratched the chair!"
    
    #polymorphism example - we are overriding the definition of the speak function
    def speak(self):
        return f"{self.name} meowed at the door"
    
Ash = Cat("Ash", 2, "Maine Coone", "brown", "medium-hair")
print(Ash.scratch())
print(Ash.speak())
#print(Ash.__age) #this will throw an error because the property is private
print(Ash.get_age())
Ash.set_age(3)
print(Ash.get_age())