# HDB Resale Data Mining
## Introduction
This repository is created for the group project in DSA3361 - Inferential Data Analytics. The final project is to predict the HDB Resale Price.

## Methodology
Data augmentation is done by crawling open source datasets across the internet. Majority of the dataset are clean and do not require cleaning, however, several of the dataset includes outdated data which requires the user to manually verify and clean the data. In this Github, I have included the code to derive the following features
- All of the bus stops and their coordinates in Singapore
- Coordinates of the licensed hawker centres in Singapore
- Coordinates of the HDB Locations in Singapore
- Coordinates of the industrial districts in Singapore
- Code used for prediction of housing price index
- Coordinates of all of the schools in Singapore
- Coordinates of all of the supermarket in Singapore
- Coordinates of all MRT and LRT stations in Singapore
- Time taken to travel to Raffles Place MRT from each HDB Block

## Usage
There should be a Config folder consisting of two files:
config.json - Containing the username and password for OneMap API with the following json fields: onemapusername, onemappassword.
lta_config.json - Containing the API key for LTA DataMall with the following json field: lta_datamall_key

After that, you should include the files in the Input folders before going to each folder and running the relevant codes.
Files will be included in the output folder.

Include all of the output files in HDB_Price_Prediction_In_Python\Feature Engineering - Alex and run Feature_Engineering.ipynb.
After that, run XGB_1.ipynb to train and obtain the model.

## Results
We achieved an RMSE of 25914 and an R^2 of 0.9783237530633263. This is an improvement over the existing models which doesn't exactly consider the timeseries movement of the prices. This is done by calculating median price and predicting the price movement. We recognize that this result might be different if there is a large deviation of the median prices in the prediction months. However, from historical observations, prices are generally stable and will follow a general trend.

Data Mining is done using LTA DataMall, OneMap and Data.gov.sg. 

The data and content accessed via OneMap, LTA DataMall, and Data.gov.sg are provided by the respective agencies (the Land Transport Authority (LTA) of Singapore, Singapore Land Authority (SLA), and the Singapore Government) for public use and are intended for informational, educational, and non-commercial purposes. All data is made available under the terms and conditions outlined by these platforms and the respective licensing arrangements.

By using data from OneMap, LTA DataMall, and Data.gov.sg, you agree to comply with all applicable laws, regulations, and restrictions, and to use the data responsibly and in accordance with their intended purposes. Any use of the data for commercial purposes, redistribution, or modification without prior approval may be subject to additional terms and conditions or may require explicit permission from the respective data providers.
