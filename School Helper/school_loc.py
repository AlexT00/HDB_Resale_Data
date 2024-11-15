import requests
import json
import pandas as pd

class schoolScraper:
    def __init__(self, target_file, output_file):
        self.target_file = target_file
        self.output_file = output_file
    def query_onemap(self, postal_code):
        url = "https://www.onemap.gov.sg/api/common/elastic/search"
        params = {
            "searchVal": postal_code,
            "returnGeom": "Y",
            "getAddrDetails": "Y",
            "pageNum": 1
        }
        response = requests.get(url, params=params)
        return response.json()
    def read_lat_lo(self, response):
        if response["found"] == 0:
            return None
        else:
            return response["results"][0]["LATITUDE"], response["results"][0]["LONGITUDE"]
        
    def apply_df(self):
        '''
        '''
        data = pd.read_csv(self.target_file)
        data["LATITUDE"] = None
        data["LONGITUDE"] = None
        for index, row in data.iterrows():
            response = self.query_onemap(row["postal_code"])
            print(response)
            lat_lo = self.read_lat_lo(response)
            data.loc[data["postal_code"] == row["postal_code"], "LATITUDE"] = lat_lo[0]
            data.loc[data["postal_code"] == row["postal_code"], "LONGITUDE"] = lat_lo[1]
        data.to_csv(self.output_file, index=False)
        return None
    def run(self):
        self.apply_df()
        return None