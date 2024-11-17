import supermarket_parser

if __name__ == "__main__":
    supermarkets = supermarket_parser.supermarkettoCSV("./Input/SupermarketsGEOJSON.geojson", "./Output/supermarketloc.csv")
    supermarkets.parse()