import hawkercentre_parser

if __name__ == "__main__":
    hawkercentre = hawkercentre_parser.hawkercentreToCSV("./Input/HawkerCentresGEOJSON.geojson", "./Output/hawkercentreloc.csv")
    hawkercentre.parse()