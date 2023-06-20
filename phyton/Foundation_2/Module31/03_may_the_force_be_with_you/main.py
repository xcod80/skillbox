import json

import requests

millenium_ship = dict()

star_ships = requests.get('https://swapi.dev/api/starships/')

for ship in star_ships.json()['results']:
    if ship['name'] == 'Millennium Falcon':
        break
else:
    print('Корабя нет в базе!')
    exit(0)

millenium_ship['name'] = ship['name']
millenium_ship['max_atmosphering_speed'] = ship['max_atmosphering_speed']
millenium_ship['starship_class'] = ship['starship_class']
millenium_ship['pilots'] = list()

for pilot in ship['pilots']:
    pilot_data = requests.get(pilot).json()
    pilot_file = {
        'name': pilot_data['name'],
        'height' : pilot_data['height'],
        'mass' : pilot_data['mass'],
        'homeworld' : requests.get(pilot_data['homeworld']).json()['name'],
        'homeworld_link' : pilot_data['homeworld']
    }
    millenium_ship['pilots'].append(pilot_file)

with open('falcon.json', 'w') as file:
    json.dump(millenium_ship, file, indent=5)
print(json.dumps(millenium_ship, indent=5))