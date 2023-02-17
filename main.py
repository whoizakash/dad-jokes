import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

header = figlet_format("DAD JOKE 3000")

header = colored(header, color='magenta')
print(header)

user_input = input("What would you like to search for? ")
url = "https://icanhazdadjoke.com/search"

res = requests.get(
    url, headers={"Accept": "application/json"}, params={"term": user_input}).json()


num_jokes = len(res["results"])
results = res["results"]
if num_jokes > 1:
    print(f"I found {num_jokes} jokes about {user_input}. Here's one: ")
    print(choice(results)["joke"])
elif num_jokes == 1:
    print(f"I found one joke about {user_input}: ")
    print(res["result"][0]["joke"])
else:
    print(f"Sorry, coudn't find a joke with your term {user_input}!")
