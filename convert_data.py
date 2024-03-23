def convert_data_format(dict):
    dict["date_from"] = dict["date_from"].replace("-", "/")
    dict["date_to"] = dict["date_to"].replace("-", "/")
    dict["max_flight_prices"] = float(dict["max_flight_prices"])
    dict["max_days_at_destination"] = int(dict["max_days_at_destination"])
    
    dict["city_from"] = ','.join(dict["city_from"])
    
    # Temporary added, it will be converted to list on frontend by default later 
    dict["max_flight_prices"] = str(dict["max_flight_prices"]).split(",") 

    if dict["accept_stopovers"] == "true":
        dict["accept_stopovers"] = True
    else:
        dict["accept_stopovers"] = False

    return dict
    