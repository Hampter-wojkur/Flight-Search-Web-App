import json

# Otwórz plik JSON w trybie odczytu

iata_city_codes = {}
i = 0
with open('airports.json', 'r') as file:
    data = json.load(file)
    for airport_code, airport_info in data.items():
        if airport_info["iata"] != "":
            iata_code = airport_info["iata"]
            city = airport_info["city"]
            iata_city_codes[city] = iata_code

print(iata_city_codes)
print(len(iata_city_codes))

file_name = "iata_city_codes.json"

# Zapisywanie danych do pliku JSON
with open(file_name, 'w') as file:
    json.dump(iata_city_codes, file, indent=4)
