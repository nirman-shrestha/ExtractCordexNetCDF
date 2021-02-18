# ExtractCordexNetCDF
Simple Python code to extract data for selected locations from multiple NetCDF files downloaded from Cordex (https://cordex.org/) website

Required Packages:
glob2
netCDF4
numpy
pandas
DateTime
art

How to run the code:
1) Put the Stations.csv, downloaded Cordex NetCDF files for which data should be extracted and extract_CordexNetCDF.py files in same folder.
2) Check the NetCDF files to see if the co-ordinates are rotated or regular and enter stations name, and input the station names and their co-ordinates in the csv file removing the all data that are already in there. 
3) The code will extract the data in Station-Name_Parameter_Model_Years.csv format in same folder the code is in.
4) Enjoy!
