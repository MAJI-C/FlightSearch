from configure import configure
import os
import requests

configure()

sheety_endpoint = os.getenv("SHT_ENDPOINT")
myToken = os.getenv("SHT_TOKEN")
bearer_headers = {
"Authorization": myToken,
}

class DataManager:
    def __init__(self):
        response = requests.get(url = sheety_endpoint, headers=bearer_headers)
        print(response.status_code)
        self.data = response.json()['iata']
    
    def edit_cell(self, id, **kwargs):
        for var_name, var_value in kwargs.items():
            json_data = {
                "iata": {
                var_name: var_value,
                }
            }
            endpoint = f"{sheety_endpoint}/{id}"
            response = requests.put(url=endpoint, json=json_data,headers=bearer_headers)
            print(response.status_code)



