users: list = [
    {"name": "Maja", "location": "Inowrocław", "posts": 100},
    {"name": "Dobrawa", "location": "Iława", "posts": 700},
    {"name": "Jakub", "location": "Warszawa", "posts": 50},
    {"name": "Bartosz", "location": "Łódż", "posts": 9},
    {"name": "Patrycja", "location": "Kutno", "posts": 34},
]

print(f"Witaj {users[0]["name"]}")

for user in users:
    print(f"Twój znajomy {user['name']} z {user['location']} opublikował {user['posts']} postów.")






# for tekst in lista_tekstów:
  #  print(f' {tekst} rządzi')

