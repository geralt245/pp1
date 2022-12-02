import json

film = {
    "title": "2001: A Space Odyssey",
    "director": "Stanley Kubrick",
    "genre": "Science-Fiction",
    "year": "1968",
    "country": ["USA", "UK"]
}


with open("favourite.json", "w") as file:
    json.dump(film, file, indent = 3)