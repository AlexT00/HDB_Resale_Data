import requests
import json
import pandas as pd

class HDBDistCBD:
    def __init__(self, file_name):
        ## Set OneMap username and OneMap password
        with open("config.json", "r") as f:
            config = json.load(f)
            self.onemapusername = config["onemapusername"]
            self.onemappassword = config["onemappassword"]
        self.file_name = file_name
        self.df = pd.read_csv(file_name)
        ## ONEMAP Authentication in json
        url = "https://www.onemap.gov.sg/api/auth/post/getToken"
        payload = {
            "email": self.onemapusername,
            "password": self.onemappassword
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url, headers=headers, json=payload)
        self.token = response.json()["access_token"]
        print(self.token)
    
    def onemapquery(self, query):
        url = "https://www.onemap.gov.sg/api/common/elastic/search"
        params = {
            "searchVal": query,
            "returnGeom": "Y",
            "getAddrDetails": "Y",
            "pageNum": 1
        }
        response = requests.get(url, params=params)
        return response.json()
    def onemapdist(self, hdb_lat, hdb_long, cbd_lat, cbd_long):
        url = "https://www.onemap.gov.sg/api/public/routingsvc/route"
        params = {
            "start": f"{hdb_lat},{hdb_long}",
            "end": f"{cbd_lat},{cbd_long}",
            "routeType": "pt",
            "date": "05-11-2024",
            "time": "08:00:00",
            "mode": "TRANSIT",
            "numItineraries": 1
        }
        headers = {
            "Authorization": f"{self.token}"
        }
        response = requests.get(url, params=params, headers=headers)
        return response.json()
    def get_dist_cbd(self):
        '''
        Get the distance to the CBD for each HDB block
        '''
        self.df["time_cbd"] = None
        # Coordinates of raffles place mrt
        rf_onemap_query = self.onemapquery("Raffles Place MRT")
        rf_lat = rf_onemap_query["results"][0]["LATITUDE"]
        rf_long = rf_onemap_query["results"][0]["LONGITUDE"]
        for index, row in self.df.iterrows():
            hdb_lat = row["LATITUDE"]
            hdb_long = row["LONGITUDE"]
            try:
                response = self.onemapdist(hdb_lat, hdb_long, rf_lat, rf_long)
                self.df.loc[index, "time_cbd"] = response["plan"]["itineraries"][0]["duration"]
                print (f"Block {row['blk_no']} {row['street']} to CBD: {response['plan']['itineraries'][0]['duration']}")
            except Exception as e:
                print(f"Error: {e}")
                continue
        ## Create df to export
        self.df.to_csv("HDB_Distance_To_CBD.csv", index=False)

def run(file_name):
    '''
    Run the parser and return the CSV
    '''
    parser = HDBDistCBD(file_name)
    parser.get_dist_cbd()

run("HDB_Postal_Code_Edit.csv")