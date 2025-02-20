from geopy.geocoders import Nominatim

def find_nearest_pharmacy():
    geolocator = Nominatim(user_agent="assistente_virtual")
    location = geolocator.geocode("farmácia mais próxima")  # Pode substituir pela sua localização
    if location:
        print(f"A farmácia mais próxima está em: {location.address}")
        text_to_speech(f"A farmácia mais próxima está em {location.address}")
    else:
        print("Não consegui localizar a farmácia mais próxima.")
        text_to_speech("Desculpe, não consegui localizar a farmácia mais próxima.")
