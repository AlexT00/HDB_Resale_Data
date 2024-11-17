import requests
import pandas
import json
# Load user data

class HDB_PC_Parser:
    def __init__(self, data_file_name):
        with open("./Config/config.json", "r") as config_file:
            config = json.load(config_file)
            self.onemap_username = config["onemapusername"]
            self.onemap_password = config["onemappassword"] 
        self.data_file_name = data_file_name
    def query_onemap(self, address):
        url = "https://www.onemap.gov.sg/api/common/elastic/search"
        params = {
            "searchVal": address,
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
    def read_postal_code(self, response):
        if response["found"] == 0:
            return None
        else:
            return response["results"][0]["POSTAL"]
    def apply_df(self, file_name):
        '''
        Using iterrows to only call the API once per address
        Function is tweaked to obtain unique block and addresses from the df to prevent multiple calls to the API
        '''
        data = pandas.read_csv(file_name)
        data["LATITUDE"] = None
        data["LONGITUDE"] = None
        data["POSTAL"] = None
        ## Unique concat block and street name
        unique_address = data["blk_no"] + " " + data["street"]
        unique_address = unique_address.unique()
        for address in unique_address:
            print(address)
            response = self.query_onemap(address)
            lat_lo = self.read_lat_lo(response)
            postal_code = self.read_postal_code(response)
            data.loc[(data["blk_no"] + " " + data["street"]) == address, "LATITUDE"] = lat_lo[0]
            data.loc[(data["blk_no"] + " " + data["street"]) == address, "LONGITUDE"] = lat_lo[1]
            data.loc[(data["blk_no"] + " " + data["street"]) == address, "POSTAL"] = postal_code
        return data
    

def run():
    '''
    Run the parser and return the CSV
    '''
    parser = HDB_PC_Parser("./Input/HDBPropertyInformation.csv")
    data = parser.apply_df(parser.data_file_name)
    data.to_csv("./Output/output.csv", index=False)
    return data