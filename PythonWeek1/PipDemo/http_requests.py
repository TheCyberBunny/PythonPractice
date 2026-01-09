#first, we need to install the requests library if we haven't already
# You can do this by running: pip install requests
import requests

print("Enter a pokemon name or pokedex # to fetch its data:")
query = input()

#We will use the pokeapi to fetch pokemon data
url = f"https://pokeapi.co/api/v2/pokemon/{query.lower()}"

response = requests.get(url)
print(response) #this will just print the response code
#print(response.json()) #this will print the entire JSON response

#To make the output more readable, we can format the JSON response
name = response.json()['name']
dex_number = response.json()['id']
height = response.json()['height']
weight = response.json()['weight']

#Pokemon types are stored in a list of dictionaries
types = [t['type']['name'] for t in response.json()['types']]

#we can print the formatted data
print(f"Name: {name.capitalize()}")
print(f"Pokedex Number: {dex_number}") 
print(f"Height: {height / 10} m")  # height is in decimetres
print(f"Weight: {weight / 10} kg")  # weight is in hectograms
print(f"Types: {', '.join(types)}")

#we can also simplify this by defining a function
def get_pokemon(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"

    try:
        response = requests.get(url, timeout=5)

        # Handle HTTP errors (e.g. 404)
        response.raise_for_status()

        data = response.json()

        # Drill into and format the JSON response
        pokemon_info = {
            "name": data["name"].capitalize(),
            "pokedex_number": data["id"],
            "height": data["height"],
            "weight": data["weight"],
            "types": [t["type"]["name"] for t in data["types"]]
        }

        return pokemon_info

    except requests.exceptions.HTTPError:
        print(f" Pokémon '{pokemon_name}' not found.")
    except requests.exceptions.ConnectionError:
        print(" Network error. Check your internet connection.")
    except requests.exceptions.Timeout:
        print(" Request timed out.")
    except requests.exceptions.RequestException as e:
        print(f" Unexpected error: {e}")

    return None



pokemon_name = input("Enter a Pokémon name: ")
pokemon = get_pokemon(pokemon_name)

#remember our truthy values to check if pokemon is valid
if pokemon:
    print("\nPokémon Info")
    print("------------")
    print(f"Name: {pokemon['name']}")
    print(f"Pokedex Number: {pokemon['pokedex_number']}")
    print(f"Height: {pokemon['height']}")
    print(f"Weight: {pokemon['weight']}")
    print(f"Types: {', '.join(pokemon['types'])}")


#The logging module lets us track events that happen when some software runs
#it includes functions to log messages to a file or console
import logging

#There are 5 standard logging levels:
#DEBUG, INFO, WARNING, ERROR, CRITICAL

# The filename can either be a full path to the file (good for production environments)
# or it can be a relative path (from where you execute the file).
# Full path example: "/var/log/example/app.log"
logging.basicConfig(
 level=logging.DEBUG,  # sets the root logging level 
 filename='app.log',  # tells the root logger where to save the log file
 filemode='a',  # tells the root logger to append the logs (not save over)
 format='%(name)s - %(levelname)s - %(message)s'  # tells the root logger how to format the logs
)

logging.debug('Hello, Debug!')
logging.info('Hello, Info!')
logging.warning('Hello, Warning!')
logging.error('Hello, Error!')
logging.critical('Hello, Critical!')