import pandas as pd
import geojson
from bs4 import BeautifulSoup

class geojson_helper:
    def __init__(self, file_name, output_file):
        self.file_name = file_name
        self.output_file = output_file
        with open (self.file_name, "r") as f:
            self.data = geojson.load(f)
    def geojson_polygon_point(self, feature):
        '''
        This function calculates the centroid of a polygon or multipolygon
        and returns it in lat and long
        '''
        if feature["geometry"]["type"] == "Polygon":
            coordinates = feature["geometry"]["coordinates"][0]
            x = [c[0] for c in coordinates]
            y = [c[1] for c in coordinates]
            centroid_x = sum(x) / len(x)
            centroid_y = sum(y) / len(y)
            return centroid_x, centroid_y
        elif feature["geometry"]["type"] == "MultiPolygon":
            coordinates = feature["geometry"]["coordinates"]
            x = []
            y = []
            for polygon in coordinates:
                x.append(sum([c[0] for c in polygon[0]]) / len(polygon[0]))
                y.append(sum([c[1] for c in polygon[0]]) / len(polygon[0]))
            centroid_x = sum(x) / len(x)
            centroid_y = sum(y) / len(y)
            return centroid_x, centroid_y
        elif feature["geometry"]["type"] == "Point":
            return feature["geometry"]["coordinates"][0], feature["geometry"]["coordinates"][1]
    @staticmethod
    def name_parser(estate_string):
        # Parse the HTML content
        soup = BeautifulSoup(estate_string, 'html.parser')

        # Find the <td> tag that follows the <th> tag with text "STATION_NA"
        estate_string = soup.find('th', text='ESTATE_NAME').find_next_sibling('td').text
        return estate_string
    def parse(self):
        df = pd.DataFrame(columns=["Estate Name", "Latitude", "Longitude"])
        for feature in self.data["features"]:
            estate_name = self.name_parser(feature["properties"]["Description"])
            latitude, longitude = self.geojson_polygon_point(feature)
            df_res = pd.DataFrame([[estate_name, latitude, longitude]], columns=["Estate Name", "Latitude", "Longitude"])
            df = pd.concat([df, df_res])
        df.to_csv(self.output_file, index=False)