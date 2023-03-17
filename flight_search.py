from configure import configure
import os
import requests
import datetime
from flight_data import FlightData

configure()
tq_endpoint = "https://api.tequila.kiwi.com"
tq_kiwi_api_key = os.getenv("TQ_KIWI_API_KEY")
header = {
    "apikey":tq_kiwi_api_key,
        }
#https://tequila.kiwi.com/portal/docs/tequila_api/search_api
class FlightSearch:    
        
    def get_city_code(self, name):
        tq_url = f"{tq_endpoint}/locations/query"
        parameters = {
        "term": name,
        "location_types":"city",
        "location_types":"airport"}
        response = requests.get(url = tq_url, params = parameters, headers = header)
        code = response.json()['locations'][0]['city']['code']
        return code

    def find_flight(self, destination_airport_code, **kwargs):
        # get current and add 6 months to current date approximation
        current_date = datetime.datetime.now()
        six_months_from_now = current_date + datetime.timedelta(days=6*30)

        departure_airport_code = kwargs.get("departure_airport_code", "ZRH")
        date_from = kwargs.get("date_from", current_date.strftime("%d/%m/%Y"))
        date_to = kwargs.get("date_to", six_months_from_now.strftime("%d/%m/%Y"))
        nights_in_dst_from = kwargs.get("nights_in_dst_from", 2)
        nights_in_dst_to = kwargs.get("nights_in_dst_to", 21)
        flight_type = kwargs.get("flight_type", "round")
        max_stopovers = kwargs.get("max_stopovers", 0)

        tq_url = f"{tq_endpoint}/v2/search"

        parameters = {
            "fly_from": departure_airport_code,
            "fly_to": str(destination_airport_code),
            "dateFrom": date_from,
            "dateTo": date_to,
            "nights_in_dst_from": nights_in_dst_from,
            "nights_in_dst_to": nights_in_dst_to,
            "flight_type": flight_type,
            "max_stopovers": max_stopovers,
            }
        response = requests.get(url=tq_url, params = parameters, headers = header)

        try:
            flight = response.json()["data"][0]

        except IndexError:
            return None
        else:
            stops = int(len(flight["route"])/2)
            flight_data = FlightData(
                price=flight["price"],
                origin_city=flight["cityFrom"],
                origin_airport=flight["flyFrom"],
                destination_city=flight["cityTo"],
                destination_airport=flight["flyTo"],
                destination_country = flight["countryTo"]["name"],
                nights_in_dest = flight["nightsInDest"],
                out_date=flight["route"][0]["local_departure"].split("T")[0],
                return_date=flight["route"][stops]["local_departure"].split("T")[0],
                stop_overs = stops - 1,
                via_city = flight["route"][stops]["cityFrom"]
            )
            return flight_data
