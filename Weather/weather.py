import requests 
import os
from dotenv import load_dotenv

load_dotenv()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_city_coordinates(city, state, country, api_key):
    url = (
        f"http://api.openweathermap.org/geo/1.0/direct?q={city},"
        f"{state},{country}&limit=5&appid={api_key}"
    )
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Erro: {response.status_code}, {response.text}")
        return None

def get_weather(lat, lon, api_key):
    url = (
    f"http://api.openweathermap.org/data/2.5/weather?"
    f"lat={lat}&lon={lon}&appid={api_key}&units=metric"
)
    response = requests.get(url)
    
    if response.status_code == 200: 
        weather_data = response.json()
        return weather_data
    else:
        print(
            f"Erro ao obter clima: {response.status_code}, "
            f"{response.text}"
        )
        return None
    
def get_user_input(prompt, min_length=1, max_length=None): 
    while True: 
        user_input = input(prompt).strip()
        if not user_input: 
            print("Erro: Esse campo não pode ficar vazio.")
        elif min_length and len(user_input) < min_length:
            print(f"Erro: A entrada de letras deve ter no mínimo {min_length}"
                  f"caracteres"
                  )
        elif max_length and len(user_input) > max_length:
            print(
    f"Erro: A entrada deve ter no máximo {max_length} "
    "caracteres."
)
        else: 
            return user_input

api_key = os.getenv("API_KEY")

                  
while True:
    city = get_user_input("Digite o nome da cidade: ")
    state = get_user_input("Digite o código do estado (Sigla): ")
    country = get_user_input(
    "Digite o código do país (ex: 'US' para "
    "Estados Unidos): "
)

    coordinates = get_city_coordinates(city, state, country, api_key)
    if coordinates: 
        location = coordinates[0]
        print(
            f"Cidade: {location['name']}, "
            f"Estado: {location.get('state', 'N/A')}, "
            f"País: {location['country']}, "
            f"Latitude: {location['lat']}, "
            f"Longitude: {location['lon']}"
        )


        weather_data = get_weather(location['lat'], location['lon'], api_key)
        if weather_data:
            print(f"Temperatura: {weather_data['main']['temp']} °C")
            print(f"Condição: {weather_data['weather'][0]['description']}")
            print(f"Umidade: {weather_data['main']['humidity']}%")
    
    
    again = input(
    "Deseja buscar outra cidade?:\n(S) para sim e "
    "qualquer outra tecla para sair do programa: "
).strip().lower()
    if again == 's':
        clear_screen() 
    else:
        print("Saindo do programa.")
        break