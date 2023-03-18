from configure import configure
from flight_search import FlightSearch
from data_manager import DataManager

# Set up the template: update city codes and minimum price
data_manager = DataManager()
flight_search = FlightSearch()
sheet_values = data_manager.call_spreadsheet_api()
if data_manager.get_cell_value("iata!B2") is None:
    upd_values = []
    for item in sheet_values[1:]:
        city = item[0]
        code = flight_search.get_city_code(city)
        price = flight_search.find_flight(code).price
        upd_values.append([city, code, price])
    print(upd_values)
    data_manager.update_cells(upd_range = "iata!A2", upd_values = upd_values)


for destination in sheet_values[1:]:
    code = destination[1]
    price = int(destination[2])
    flight = flight_search.find_flight(code)
    if flight is None:
        try:
            flight = flight_search.find_flight(code, max_stopovers = 2)

        except IndexError:
            print(f"There is no flights to {destination[0]}")
            continue

    if flight.price < price:
        msg = f"Low price alert! {flight.nights_in_dest} nights in {flight.destination_country}.Only €{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        
        if flight.stop_overs > 0:
            msg += f"\n\nFlight has {flight.stop_overs}, via {flight.via_city}."
        print(msg)
