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
        price = flight_search.find_flight(code)
        upd_values.append([city, code, price])
    print(upd_values)
    data_manager.update_cells(upd_range = "iata!A2", upd_values = upd_values)
