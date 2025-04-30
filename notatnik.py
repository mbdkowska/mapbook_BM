# import folium
# map=folium.Map(location=(52.23, 21.0), zoom_start=6)
# folium.Marker(location=(52.23, 21.0),popup="<h1>Maja</h1>").add_to(map)
# map.save("mapa.html")


 users: list = [
     {'name': 'Maja', 'location': 'Inowrocław', 'posts': 100},
     {'name': 'Dobrawa', 'location': 'Iława', 'posts': 700},
     {'name': 'Jakub', 'location': 'Warszawa', "posts": 50},
     {'name': 'Bartosz', 'location': 'Łódż', 'posts': 9},
     {'name': 'Patrycja', 'location': 'Kutno', 'posts': 34},
]
import requests
from bs4 import BeautifulSoup

def get_coordinates(city:str)->list:
    url=f'https://pl.wikipedia.org/wiki/{city}'
    response = requests.get(url).text
    response_html=BeautifulSoup(response,"html.parser")
    longitude=float(response_html.select(".latitude")[1].text.replace(",","."))
    latitude=float(response_html.select(".longitude")[1].text.replace(",","."))
    print(latitude, longitude)
    return [latitude,longitude]

for user in users:
    get_coordinates(user["location"])