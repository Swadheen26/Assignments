import requests
from sympy import *

def internet_search(query):
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url)
    # Extract and return relevant information from the response
    return response.text

def math_operation(expression):
    result = eval(expression)
    return result

def process_request(user_input):
    if "How rich is" in user_input:
        return internet_search(user_input)
    elif "raise to" in user_input:
        return math_operation(user_input.split("What is ")[1])
    else:
        return "Sorry, I couldn't understand your request."

# Example user input
user_input = "What is 23 raise to 3"
response = process_request(user_input)
print(response)
