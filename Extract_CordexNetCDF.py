#Created by Nirman Shrestha
#With help of tutorial from this YouTube Tutorial: https://www.youtube.com/watch?v=ue55Mxe4yVQ&list=PLLxyyob7YmEE8S3QDs1PZQkiBxA4zn_Gx

import glob
from netCDF4 import Dataset
import numpy as np
import pandas as pd
from datetime import datetime
from art import *

#Start program
tprint("Game Start!", font="rnd-small")

#Record all the start and end years of netCDF files into a Python list
all_years = []

for file in glob.glob('*.nc'):
    data = Dataset(file,'r')
    year_s = file[-20:-16]
    year_e = file[-11:-7]
    all_years.append(year_s)
    all_years.append(year_e)

#Counting letters in filename to read file later
len_file = len(file)
    
#Creating variable name
vals_name = str(file.split('_')[0]) 
model = str(file.split('_')[2])
model_name = str(file.split('_')[2]) + '_' + str(file.split('_')[3])     

#Creating an empty Panda DataFrame covering the whole range of Data
year_start = min(all_years)
year_end = max(all_years)
start_date = str(year_start) + '-01-01'
end_date = str(year_end) +'-12-31'
start_date = datetime.strptime(start_date, '%Y-%m-%d')
end_date = datetime.strptime(end_date, '%Y-%m-%d')
date_range = pd.date_range(start = start_date, 
                           end = end_date, 
                           freq = 'D', name = 'Date')
df = pd.DataFrame(np.nan, columns = [vals_name],index = date_range)

#Sort the all_years list
all_years.sort()
#Creating lenght of loop for reading NetCDF filenames
len_loop = len(all_years)

#Defining the location ,lati,long based on the csv file
Stations = pd.read_csv('Stations.csv')

for index,row in Stations.iterrows():
    location = row['Stations']
    rlati = row['rlati']
    rlong = row['rlong']
    tprint("Player " + location + " Ready!", font = "amc3line")
    aprint("random")
    for n in range(0,len_loop,2):
    #Reading the data
        data = Dataset(str(file[0:(len_file - 20)] + all_years[n] + file[(len_file - 16):(len_file - 11)] + all_years[n+1] + file[(len_file - 7):]), 'r')
            
        #Storing the lat and lon data into the variables
        lat = data.variables['rlat'][:]
        lon = data.variables['rlon'][:]              
            
        #Squared difference of lat and lon
        sq_diff_lat = (lat - rlati)**2
        sq_diff_lon = (lon - rlong)**2
            
        #Identifying the index of the minimum difference in value for lat and lon
        min_index_lat = sq_diff_lat.argmin()
        min_index_lon = sq_diff_lon.argmin()
    
        #Accessing the required extract values       
        vals = data.variables[vals_name]
            
        #Creating the date range for each 5 years during each iteration
        start =str(all_years[n]) + '-01-01'
        end = str(all_years[n+1]) +'-12-31'
        start = datetime.strptime(start, '%Y-%m-%d')
        end = datetime.strptime(end, '%Y-%m-%d')
        d_range = pd.date_range(start = start, 
                               end = end, 
                               freq = 'D', name = 'Date')
        dfr = pd.DataFrame(index = d_range)
        #Inserting index as date column to remove leap year day i.e. 02/29
        dfr['Date'] = dfr.index 
        #Remove leap years day i.e. 02/29 from dataframe
        dfr = dfr[~((dfr.Date.dt.month == 2) & (dfr.Date.dt.day == 29))]
                          
        for t_index in np.arange(0,len(dfr)):
            #print('Recording values for '+ location + ':' + str(dfr['Date'][t_index]))
            df.loc[dfr['Date'][t_index]][vals_name] = vals[t_index, min_index_lat, min_index_lon]
    #Fill missing leap year values with interpolation between two cells
    df = df.interpolate()
    #Path to save csv file to 
    csv_name = location + '_' + vals_name + '_' + model_name + '_' + year_start + '_'+ year_end + '.csv'
    df.to_csv(csv_name )    
    tprint("Player " + location + " Down!", font = "amc3line")
#Print end of program
tprint("GAME OVER!", font="rnd-small")             
