import json
import sys
import urllib2



if __name__=='__main__':
    #mtakey = 'b7450ea1-8298-44f8-85cc-e93711acf643'
    #busnumber = 'M1'
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2].upper())
    request = urllib2.urlopen(url)
    metdata = json.loads(request.read())
    bus = metdata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    
    print "Bus Line : %s" % (sys.argv[2].upper())
    
    count = 0
    for i in bus:
        latitude  = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        longitude = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        print "Bus %s latitude is at %s and longitude is at %s" %(count,latitude,longitude)
        count += 1
    
    
    print "Number of Active Buses : %s" % len(bus)


