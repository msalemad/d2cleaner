import requests
import json
import os

# Clave API para acceder a la API de Destiny 2 de Bungie
API_KEY = 'your_api_key_here'
# URL base para la API de Destiny 2
BASE_URL = 'https://www.bungie.net/Platform/Destiny2/'

# Encabezados para las solicitudes de la API
HEADERS = {
    'X-API-Key': API_KEY
}

def obtener_ids_personajes(membership_id, membership_type):
    # URL para obtener los IDs de los personajes del perfil
    url = f"{BASE_URL}Profile/{membership_id}/?components=200"
    # Realizar la solicitud a la API
    response = requests.get(url, headers=HEADERS)
    # Verificar errores en la respuesta
    if response.status_code != 200:
        try:
            error_message = response.json()
        except json.JSONDecodeError:
            error_message = response.content.decode('utf-8-sig')
        print(f"Error al obtener los IDs de los personajes: {error_message}")
        return {}
    # Parsear la respuesta JSON
    try:
        data = json.loads(response.content.decode('utf-8-sig'))
    except json.JSONDecodeError:
        print("Error: Respuesta de la API no es un JSON válido.")
        return {}
    # Verificar si la respuesta contiene los datos esperados
    if 'Response' not in data or 'characters' not in data['Response'] or 'data' not in data['Response']['characters']:
        print("Error: Respuesta de la API no contiene los datos esperados.")
        return {}
    # Extraer los IDs de los personajes de la respuesta
    characters = data['Response']['characters']['data']
    return {
        'Warlock': characters['warlock_id'],
        'Hunter': characters['hunter_id'],
        'Titan': characters['titan_id']
    }

def mover_item_a_la_boveda(character_id, item_id, membership_type):
    # URL para mover un objeto a la bóveda
    url = f"{BASE_URL}Actions/Items/TransferItem/"
    # Carga útil para la solicitud a la API
    payload = {
        'itemReferenceHash': item_id,
        'characterId': character_id,
        'membershipType': membership_type,
        'itemId': item_id,
        'vault': True
    }
    # Realizar la solicitud a la API
    response = requests.post(url, headers=HEADERS, json=payload)
    # Verificar errores en la respuesta
    if response.status_code != 200:
        print(f"Error al mover el objeto {item_id} a la bóveda: {response.json()}")

def obtener_inventario(membership_id, character_id):
    # URL para obtener el inventario de un personaje
    url = f"{BASE_URL}Profile/{membership_id}/Character/{character_id}/?components=201,205"
    # Realizar la solicitud a la API
    response = requests.get(url, headers=HEADERS)
    # Parsear la respuesta JSON
    data = json.loads(response.content.decode('utf-8-sig'))
    # Extraer inventario y equipamiento de la respuesta
    inventory = data['Response']['inventory']['data']['items']
    equipment = data['Response']['equipment']['data']['items']
    
    # Filtrar objetos en armas, armaduras y todo lo demás
    weapons = [item for item in inventory if item['bucketHash'] in weapon_buckets and item not in equipment]
    armor = [item for item in inventory if item['bucketHash'] in armor_buckets and item not in equipment]
    everything = [item for item in inventory if item not in equipment]
    
    return {
        'weapons': weapons,
        'armor': armor,
        'everything': everything
    }

def desequipar_items(character_id, tipo_item, membership_type):
    # Obtener el inventario del personaje
    inventory = obtener_inventario(membership_id, character_id)
    # Obtener los objetos a mover según el tipo de objeto
    items_to_move = inventory[tipo_item]
    # Mover cada objeto a la bóveda
    for item in items_to_move:
        mover_item_a_la_boveda(character_id, item['itemId'], membership_type)

def main():
    # ID de membresía del usuario
    membership_id = 'your_membership_id_here'
    # Tipo de membresía (14 para Epic Games, 3 para Steam, 2 para Xbox, 1 para PSN)
    membership_type = 14  # Epic Games
    # Obtener los IDs de los personajes
    character_ids = obtener_ids_personajes(membership_id, membership_type)
    while True:
        # Mostrar el menú para seleccionar la clase del personaje
        print("\033[1;34mSeleccione la clase de personaje:\033[0m")
        print("1. Warlock")
        print("2. Hunter")
        print("3. Titan")
        print("4. Todos")
        print("5. Salir")
        choice = input("\033[1;32mIngrese su elección: \033[0m")
        
        if choice == '5':
            break
        
        # Determinar las clases en las que operar según la elección del usuario
        classes = []
        if choice == '1':
            classes = ['Warlock']
        elif choice == '2':
            classes = ['Hunter']
        elif choice == '3':
            classes = ['Titan']
        elif choice == '4':
            classes = ['Warlock', 'Hunter', 'Titan']
        
        for cls in classes:
            # Mostrar el menú para seleccionar la operación
            print(f"\033[1;34mSeleccione la operación para {cls}:\033[0m")
            print("1. Desequipar Armas")
            print("2. Desequipar Armaduras")
            print("3. Desequipar TODO")
            operation = input("\033[1;32mIngrese su elección: \033[0m")
            
            # Realizar la operación seleccionada
            if operation == '1':
                desequipar_items(character_ids[cls], 'weapons', membership_type)
            elif operation == '2':
                desequipar_items(character_ids[cls], 'armor', membership_type)
            elif operation == '3':
                desequipar_items(character_ids[cls], 'everything', membership_type)
        
        print("\033[1;32mOperación completada.\033[0m")

if __name__ == "__main__":
    # ID de membresía del usuario
    membership_id = 'your_membership_id_here'
    # Tipo de membresía (14 para Epic Games, 3 para Steam, 2 para Xbox, 1 para PSN)
    membership_type = 14  # Epic Games
    # Ejemplo de hashes de cubos para armas
    weapon_buckets = [1498876634, 2465295065, 953998645]
    # Ejemplo de hashes de cubos para armaduras
    armor_buckets = [3448274439, 14239492, 20886954, 1585787867, 14239492]
    main()
