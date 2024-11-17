import pandas
from bs4 import BeautifulSoup
import geojson

class supermarkettoCSV:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        with open(self.input_file, "r") as f:
            self.data = geojson.load(f)
        self.df = pandas.DataFrame(columns=["Postal Code", "Latitude", "Longitude"])
    @staticmethod
    def name_parser(postal_string):
        # Parse the HTML content
        soup = BeautifulSoup(postal_string, 'html.parser')

        # Find the <td> tag that follows the <th> tag with text "STATION_NA"
        postal_code = soup.find('th', text='POSTCODE').find_next_sibling('td').text
        return postal_code
    def parse(self):
        for feature in self.data["features"]:
            PostalCode = self.name_parser(feature["properties"]["Description"])
            latitude = feature["geometry"]["coordinates"][1]
            longitude = feature["geometry"]["coordinates"][0]
            df_res = pandas.DataFrame([[PostalCode, latitude, longitude]], columns=["Postal Code", "Latitude", "Longitude"])
            self.df = pandas.concat([self.df, df_res])
        self.df.to_csv(self.output_file, index=False)