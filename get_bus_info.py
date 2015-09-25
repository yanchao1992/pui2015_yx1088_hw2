

import sys
import urllib2
import json
import csv

if __name__=='__main__':
    #key = 'b7450ea1-8298-44f8-85cc-e93711acf643'
    #bus = 'M1'
    mtakey = sys.argv[1]
    busnumber = sys.argv[2]
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (mtakey,busnumber) 
    request = urllib2.urlopen(url)
    metdata = json.loads(request.read())
    businfo = metdata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
    with open(sys.argv[3],'wb') as csvfile:
           buswriter = csv.writer(csvfile)
            
            
            for bus in businfo:
                latitude = bus["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
                longitude = bus["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
            if bus["MonitoredVehicleJourney"]["OnwardCalls"] == {}:
                stopname = "N/A"
                stopstatus = "N/A"
            else:
                stopname = bus["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["StopPointName"]
                stopstatus = bus["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["Extensions"]["Distances"]["PresentableDistance"]
            row = [latitude, longitude, stopname, stopstatus]
            buswriter.writerow(row)




