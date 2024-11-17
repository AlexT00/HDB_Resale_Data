import sys
import jtcestate_geojson_helper

def main():
    # input_file = sys.argv[1]
    # output_file = sys.argv[2]
    helper = jtcestate_geojson_helper.geojson_helper("./Input/JTCEstateNameBoundaryGEOJSON.geojson", "./Output/JTCEstateNameBoundaryGEOJSON.csv")
    helper.parse()
    return None

if __name__ == "__main__":
    main()