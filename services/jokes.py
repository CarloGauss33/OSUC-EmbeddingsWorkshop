import requests

BASE_URL = "https://v2.jokeapi.dev/joke/Dark?blacklistFlags=religious"

def get_joke():
    """ This method gets a random joke from the API """
    response = requests.get(BASE_URL).json()
    print(response['joke'])
    return response['joke']

