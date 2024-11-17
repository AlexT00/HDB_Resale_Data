import sys
import school_loc

def main():
    # target_file = sys.argv[1]
    # output_file = sys.argv[2]
    scraper = school_loc.schoolScraper("./Input/Generalinformationofschools.csv", "./Output/school_loc.csv")
    scraper.run()
    return None

if __name__ == "__main__":
    main()