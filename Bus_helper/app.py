import get_all_busstops
import sys
def run():
    '''
    Run the parser and return the CSV
    '''
    parser = get_all_busstops.BusStop("./Output/busstops.csv") ## Change the file name to the desired output file name if required.
    parser.main()
    return "Completed"


if __name__ == "__main__":
    run()