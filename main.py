from configure import configure
from flight_search import FlightSearch
from data_manager import DataManager

# Set up the template: update city codes and minimum price
data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.data
if sheet_data[0]["code"]=="":
    for item in data_manager.data:
        id = item["id"]
        city = item["city"]
        code = flight_search.get_city_code(city)
        price = flight_search.find_flight(code)
        data_manager.edit_cell(id, code = code, price = price)
