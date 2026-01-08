#File handling refers to the process of creating, opening, reading, writing, and deleting files using Python
#Python has built-in functions and methods to make this easy

#Important to know for data persistence and processing
#automation of many real-world tasks
#handling large data sets

#open() is the key function and takes 2 parameters; filename and mode
#4 modes available:
#"r" - read; the default mode for reading; throws an error if file does not exist
#"a" - append the end of the file; creates a file if it does not exist
#"w" - write; creates a new file if it does not exist
#"x" - create; returns an error if file does not exist

#We can also specify if the file should be handled as binary or text using "b" and "t" respectively

#myFile = open('./PythonWeek1/resources/myNewestFile.txt', "w")

myFile = open('./PythonWeek1/resources/myNewestFile.txt', "r")
print(myFile.read())

#this will read one line, calling it again will read the next line
#print(myFile.readline())

#this will read only the first 4 characters
#print(myFile.read(4))

myFile.close()

#we can also access files using exact paths
#myFile2 = open('C://Users/KelseyLinton/Documents/PythonPractice/PythonWeek1/resources/myNewestFile.txt', "r")
#print(myFile2.read())

#we can use the with statement to automatically close the file after its suite finishes
# with open('./PythonWeek1/resources/myNewestFile.txt', "r") as myFile3:
#     print(myFile3.read())

pokemonTeam = []

for i in range(6):
    pokemon = input("Enter a Pokemon for your team: ")
    pokemonTeam.append(pokemon)

#each time we run this, it will overwrite the previous content
with open('./PythonWeek1/resources/myPokemonTeam.txt', "w") as teamFile:
    for pokemon in pokemonTeam:
        teamFile.write(pokemon + "\n")
    print("Your Pokemon team has been saved!")
    
with open('./PythonWeek1/resources/myPokemonTeam.txt', "r") as teamFile:
    print("Your Pokemon team consists of:")
    print(teamFile.read())

#To delete a file, we need to import the OS module
import os
os.remove('./PythonWeek1/resources/myNewFile.txt')
print("File deleted successfully.")