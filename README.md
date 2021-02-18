# ExtractCordexNetCDF
Simple Python code to extract data for selected locations from multiple NetCDF files downloaded from Cordex (https://cordex.org/) website

Required Packages:
1) glob2
2) netCDF4
3) numpy
4) pandas
5) DateTime
6) art

How to run the code:
1) Put the Stations.csv, downloaded Cordex NetCDF files for which data should be extracted and extract_CordexNetCDF.py files in same folder.
2) Make sure that the multiple Cordex NetCDF files are for same model name (i.e. NOAA-GFDL-GFDL-ESM2M or CCCma-CanESM2), same rcp (i.e. historical or rcp45 or rcp85), and continuous years (i.e. 20210101-20251231, 20260101-20301231 and so on)  as this code reads the model name, rcp name, years from Cordex NetCDF file names (for eg: tasmin_WAS-44_NOAA-GFDL-GFDL-ESM2M_rcp85_r1i1p1_SMHI-RCA4_v2_day_20210101-20251231.nc) and determine the data entry for dates based on those years it has read. 
3) Check the NetCDF files to see if the co-ordinates are rotated or regular and enter stations name, and input the station names and their co-ordinates in the csv file removing the all data that are already in there. 
4) The code will extract the data in Station-Name_Parameter_Model_Years.csv format in same folder the code is in.
5) Enjoy!
