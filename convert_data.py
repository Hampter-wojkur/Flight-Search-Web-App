from datetime import datetime

def convert_data_format(dict):
    # Data format conversion
    # dict["date_from"] = dict["date_from"].replace("-", "/")
    date_object = datetime.strptime(dict["date_from"], "%Y-%m-%d")
    dict["date_from"] = date_object.strftime("%d/%m/%Y")
    # dict["date_to"] = dict["date_to"].replace("-", "/")
    date_object = datetime.strptime(dict["date_to"], "%Y-%m-%d")
    dict["date_to"] = date_object.strftime("%d/%m/%Y")

    dict["max_days_at_destination"] = int(dict["max_days_at_destination"])
    
    dict["city_from"] = ','.join(dict["city_from"])
    
    # Temporary added, it will be converted to list on frontend by default later 
    dict["max_flight_prices"] = str(dict["max_flight_prices"]).split(",") 
    dict["max_flight_prices"] = list(map(int, dict["max_flight_prices"]))
    if dict["accept_stopovers"] == "true":
        dict["accept_stopovers"] = True
    else:
        dict["accept_stopovers"] = False

    return dict
    