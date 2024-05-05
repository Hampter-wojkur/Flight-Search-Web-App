import json

# Otwórz plik JSON w trybie odczytu

iata_city_codes = {}
i = 0
with open('iata_city_codes_raw.json', 'r') as file:
    data = json.load(file)
    for element in data:
        city = element["name_translations"]["en"]
        iata_code = element["code"]
        iata_city_codes[city] = iata_code

print(iata_city_codes)
print(len(iata_city_codes))

file_name = "iata_city_codes.json"

# Zapisywanie danych do pliku JSON
with open(file_name, 'w') as file:
    json.dump(iata_city_codes, file, indent=4)
