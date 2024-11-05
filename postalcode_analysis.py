import pandas as pd

'''
This script is used to analyse the postal codes of the HDB flats in Singapore.
The unique first 2 digits of the postal codes are extracted by town.
They are formatted into a CSV.'''

def postal_code_analysis(data_file_name):
    data = pd.read_csv(data_file_name)
    data["POSTAL"] = data["POSTAL"].astype(str)
    data["POSTAL"] = data["POSTAL"].str[:2]
    data = data.groupby(["town", "POSTAL"]).size().reset_index(name="count")
    data.to_csv("HDB_Postal_Code_Analysis.csv", index=False)
    return data

postal_code_analysis("HDB_Postal_Code_Edit.csv")