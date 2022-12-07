film_titles = ["The Dark Knight", "Lord of the Rings: The Fellowship of the Ring", "2001: A Space Odyssey", "Apocalypse Now", "Pulp Fiction"]

with open("films.txt", "w") as f:
    for i in range(0, len(film_titles)):
        if i == len(film_titles) - 1:
            f.write(film_titles[i])
        else:
            f.write(film_titles[i] + "\n")