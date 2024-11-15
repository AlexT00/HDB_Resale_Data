import pandas
from bs4 import BeautifulSoup
import geojson

class MRTtoCSV:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        with open(self.input_file, "r") as f:
            self.data = geojson.load(f)
        self.df = pandas.DataFrame(columns=["Name", "Latitude", "Longitude"])
    @staticmethod
    def name_parser(station_string):
        # Parse the HTML content
        soup = BeautifulSoup(station_string, 'html.parser')

        # Find the <td> tag that follows the <th> tag with text "STATION_NA"
        station_name = soup.find('th', text='STATION_NA').find_next_sibling('td').text
        return station_name
    def parse(self):
        for feature in self.data["features"]:
            name = self.name_parser(feature["properties"]["Description"])
            latitude = feature["geometry"]["coordinates"][1]
            longitude = feature["geometry"]["coordinates"][0]
            self.df = self.df.append({"Name": name, "Latitude": latitude, "Longitude": longitude}, ignore_index=True)
            print(feature)
        self.df.to_csv(self.output_file, index=False)