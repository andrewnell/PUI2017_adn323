# Author: Andrew Nell 2017/09/27 
# HW2-Assignment 1

###############################################################################

# Code developed to pull information for a specific bus line from the MTA Bus
# API and convert the data for the specific line to the desired outputs

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
if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python show_bus_locations_adn"
           "323.py <MTA_KEY> <BUS_LINE>")
    sys.exit()                                         # F. Bianco Reference 2

# Define arguments
key, bus_line = sys.argv[1], sys.argv[2]

# Pull data from API using Key and Bus Line
try:
    url = ("http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="
           "%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(key, bus_line))
    response = urllib.urlopen(url)
    data = response.read().decode("utf-8")
    data = json.loads(data)
except urllib.HTTPError:
    print("Invalid key and url. Please try again. Run as: python " 
          "show_bus_locations_adn323.py <MTA_KEY> <BUS_LINE>")
    sys.exit()

###############################################################################
# Define variables for output including Bus Line, Total Vehicles and Latitudes
# and longitudes for each vehicle and then print variables out

# Define Bus line and Number of vehicles
try:
    Line_No = (data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]
               ['VehicleActivity'][1]['MonitoredVehicleJourney']
               ['PublishedLineName'])
    NoOfVehicles = (len(data['Siri']['ServiceDelivery']
                        ['VehicleMonitoringDelivery'][0]['VehicleActivity']))
except KeyError:
    print("Bus line does not exist or input invalid. Run as: " 
          "python show_bus_locations_adn323.py <MTA_KEY> <BUS_LINE>")
    sys.exit()
    
# Print Bus Line and Numbe rof vehicles in desired output
print ("\nBus Line : " + str(Line_No))
print ("Number of Active Buses : " + str(NoOfVehicles))

# Define latitude and longitutde of each bus and print out in desired output
for i in range(NoOfVehicles):
    
    # Define latitutde and Longitude
    latitude = (data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]
                ['VehicleActivity'][i]['MonitoredVehicleJourney']
                ['VehicleLocation']['Latitude'])
    longitude = (data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery']
                 [0]['VehicleActivity'][i]['MonitoredVehicleJourney']
                 ['VehicleLocation']['Longitude'])  
    
    # Print outputs in desired format
    print ("Bus " + str(i) + " is at latitude " + str(latitude) + 
           " and longitude " + str(longitude))
    
print ("\n")

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