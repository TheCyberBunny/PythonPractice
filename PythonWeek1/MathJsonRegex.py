#The Math module contains many useful mathematical functions and constants.
import math

#min() and max() functions find the smallest and largest values in an iterable or among multiple arguments
x = min(2, 5, 15, 3, 77)
y = max(2, 5, 15, 3, 77)
print("Minimum value:", x, "Maximum value:", y)

#abs() function returns the absolute value of a number
z = abs(-7.25)
print("Absolute value:", z)

#pow() function returns the value of a number raised to the power of another number
a = pow(3, 4)  # 3 raised to the power of 4
print("3 raised to the power of 4 is:", a)

#sqrt() function returns the square root of a number
b = math.sqrt(64)
print("Square root of 64 is:", b)

#ceil() function rounds a number up to the nearest integer
c = math.ceil(4.2)
print("Ceiling of 4.2 is:", c)
#floor() function rounds a number down to the nearest integer
d = math.floor(4.7)
print("Floor of 4.7 is:", d)

#pi constant represents the mathematical constant π (pi)
e = math.pi
print("Value of pi is:", e)


#The JSON module can be used to work with JSON data.
#JavaScript Object Notation(JSON)
import json

#We can parse JSON objects and convert them into Python dictionaries
json_data = '{"name": "Alice", "age": 30, "city": "New York"}'
data = json.loads(json_data)
print("Name:", data["name"])
print("Age:", data["age"])

#we can also convert Python dictionaries into JSON objects
#dict, list, tuple, string, int, float, True, False, None can all be converted to JSON using dumps()
python_dict = {"fruit": "Apple", "color": "Red", "quantity": 5}
json_object = json.dumps(python_dict)  
print("JSON object:", json_object)

#dumps() method can take additional parameters to format the JSON output
formatted_json = json.dumps(python_dict, indent=4)
print("Formatted JSON object:\n", formatted_json)


#RegEx stands for Regular Expression, which is a sequence of characters that forms a search pattern
#Useful for finding substrings, data validation, text manipulation, and more
#The re module provides support for regular expressions in Python
import re

#We can use the search() function to search for a pattern within a string
pattern = r"cat"
text = "The cat is on the roof."
match = re.search(pattern, text)
if match:
    print("Pattern found:", match.group())

#We can use the findall() function to find all occurrences of a pattern in a string
text2 = "The cat sat on the mat with another cat eating a rat."  
matches = re.findall(pattern, text2)
print("All occurrences of 'cat':", matches)

#regex metacharacters can help us perform more complex searches
#[ ] - A set of characters
print(re.findall(r"[cr]at", text2))  # Finds 'cat' and 'rat'

# \d - Any digit 0-9
print(re.findall(r"\d", "There are 2 cats and 3 dogs."))

# ^ - Starts with
print(re.findall(r"^The", text))  # Checks if the text starts with 'The'

# $ - Ends with
print(re.findall(r"at$", text))  # Checks if the text ends with 'at'

#split() function splits a string at each match of the pattern
split_text = re.split(r"\s", "Split this text into words.")
print("Split text:", split_text)

#the sub() function replaces matches with a specified string
replaced_text = re.sub(r"cat", "dog", text)
print("Replaced text:", replaced_text)