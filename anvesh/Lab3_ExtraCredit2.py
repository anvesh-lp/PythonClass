movies = {"IronMan": "Reobert downy jr", "CaptainAmerica": "Chris Evans", "GOG": "Chris Pratt",
          "Thor": "Chris Hemsworth", "Avengers": "Josh Brolin"}

for key, value in movies.items():
    print(key + " : " + value,end=" ")
print()
# Adding new entry
movies["Loki"] = "Tom Hiddleston"
for key, value in movies.items():
    print(key + " : " + value,end=" ")
print()
print(movies["IronMan"])
