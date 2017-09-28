# Author: Andrew Nell 2017/09/27 
# HW2-Assignment 2

###############################################################################

# Code developed to pull information for a specific bus line from the MTA Bus
# API and output all current vehicles coordinates and next stops and status

###############################################################################

# Imports to run code
from __future__ import print_function
import sys
import json

try: 
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib                    # F. Bianco Reference 1

###############################################################################
# Import data from API 

# Ensure correct number of arguments entered 
if not len(sys.argv) == 4:
    print ("Invalid number of arguments. Run as: python get_bus_info_adn"
           "323.py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv")
    sys.exit()                                         # F. Bianco Reference 2

# Define arguments
key, bus_line, outputfile = sys.argv[1], sys.argv[2], sys.argv[3]

# Pull data from API using Key and Bus Line
try:
    url = ("http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="
           "%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(key, bus_line))
    response = urllib.urlopen(url)
    data = response.read().decode("utf-8")
    data = json.loads(data)
except urllib.HTTPError:
    print("Invalid key and url. Please try again. Run as: python " 
          "get_bus_info_adn323.py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv")
    sys.exit()

###############################################################################
# Define variables for output including Total Vehicles, Latitudes, longitudes 
# next stops and status for each vehicle and then print variables out and  
# create .csv file and start printing output into .csv

# Define Number of vehicles
try:
    NoOfVehicles = (len(data['Siri']['ServiceDelivery']
                        ['VehicleMonitoringDelivery'][0]['VehicleActivity']))
except KeyError:
    print("Bus line does not exist or input invalid. Run as: " 
          "python get_bus_info_adn323.py <MTA_KEY> <BUS_LINE> <BUS_LINE.csv>")
    sys.exit()

# create.csv    
fout = open(sys.argv[3], "w")
fout.write("Latitude,Longitude,Stop Name,Stop Status\n")

# Define latitude, longitutde, Next stop and statu of each bus and print 
# out in .CSV
for i in range(NoOfVehicles):
    
    # Define latitutde and Longitude
    
    latitude = (data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery']
                [0]['VehicleActivity'][i]['MonitoredVehicleJourney']
                ['VehicleLocation']['Latitude'])
   
    longitude = (data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery']
                 [0]['VehicleActivity'][i]['MonitoredVehicleJourney']
                 ['VehicleLocation']['Longitude']) 
    
    # Define Next stop and account for errors
    try:

        stopname = (data['Siri']['ServiceDelivery']
                    ['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]
                    ['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]
                    ['StopPointName'])
    except KeyError:
        stopname = "N/A"
    
    # Define status and account for errors 
    try:

        stopstatus = (data['Siri']['ServiceDelivery']
                      ['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]
                      ['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall']
                      [0]['Extensions']['Distances']['PresentableDistance'])
    except KeyError:
        stopstatus = "N/A"
    
    # Print outputs in desired format into .csv
    fout.write(str(latitude) + "," + str(longitude) + "," + str(stopname) + 
               "," + str(stopstatus) + "\n")



###############################################################################

# References 

# 1
# F. Bianco, APIreadingJson.py.ipynb, access at:  
# https://github.com/fedhere/PUI2017_fb55/blob/master/Lab2_fb55/APIreadingJso
# n.py.ipynb on 2017/09/27

# 2 
# F. Bianco, aSimplePythonThatWritesToCSV.py, access at:  
# https://github.com/fedhere/PUI2017_fb55/blob/master/Lab2_fb55/aSimplePython
# ThatWritesToCSV.py on 2017/09/27   