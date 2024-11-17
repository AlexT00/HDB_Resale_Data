import geojson_to_csv

if __name__ == "__main__":
    mrt = geojson_to_csv.MRTtoCSV("./Input/LTAMRTStationExitGEOJSON.geojson", "./Output/mrt.csv")
    mrt.parse()