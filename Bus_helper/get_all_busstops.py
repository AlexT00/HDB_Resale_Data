import requests
import json
import pandas

'''
This function utilizes LTADataMall to retrieve all of the bus stop coordinates in Singapore
'''
class BusStop:
    def __init__(self, file_name):
        self.file_name = file_name
        with open ("lta_config.json", "r") as f:
            self.config = json.load(f)
            self.apikey = self.config["lta_datamall_key"]
            self.res_df = pandas.DataFrame()
            print(self.apikey)
        self.index = 0
    def get_all_bus_stops(self):
        url = f"http://datamall2.mytransport.sg/ltaodataservice/BusStops?$skip={self.index}"
        headers = {
            'AccountKey': self.apikey,
            'accept': "application/json"
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        print(data)
        bus_stops = data["value"]
        bus_stops_df = pandas.DataFrame(bus_stops)
        self.res_df = self.res_df.append(bus_stops_df)
        return bus_stops_df
    def main(self):
        bus_stops_df = self.get_all_bus_stops()
        while len(bus_stops_df) > 0:
            self.index += 500
            bus_stops_df = self.get_all_bus_stops()
        self.res_df.to_csv(self.file_name, index=False)
        return bus_stops_df