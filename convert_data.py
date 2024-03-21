def convert_data_format(dict):
    dict["date_from"] = dict["date_from"].replace("-", "/")
    # date_from.replace("-", "/")
    dict["date_to"] = dict["date_to"].replace("-", "/")
    # date_to.replace("-", "/")
    # flight_price = dict["max_flight_prices"]
    print(f"type of flight_price field: {type(dict["max_flight_prices"])}")
    dict["max_flight_prices"] = float(dict["max_flight_prices"])
    # stopovers = dict["accept_stopovers"]
    print(f"type of stopovers field: {type(dict["accept_stopovers"])}")
    
    if dict["accept_stopovers"] == "true":
        dict["accept_stopovers"] = True
    else:
        dict["accept_stopovers"] = False

    return dict
    