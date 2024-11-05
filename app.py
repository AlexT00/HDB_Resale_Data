import sys
import HDB_PC_Parser
if __name__ == "__main__":
    parser = HDB_PC_Parser.HDB_PC_Parser("HDBPropertyInformation.csv")
    data = parser.apply_df(parser.data_file_name)
    data.to_csv("HDB_Postal_Code_Edit.csv", index=False)
