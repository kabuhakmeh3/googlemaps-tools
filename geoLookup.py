import time, argparse
import googlemaps as gmaps
import numpy as np
import pandas as pd

def get_apikey(apifile):
    '''Load Google API Key

    Key should be restricted by:
    + API/service type
    + IP Address
    '''
    with open(apifile,'r') as file:
        apikey = file.read().strip()
        return apikey

def get_lat_lng(address, delay=0.05):
    ''' 
    Return coordinates of a street address

    Limits to keep in mind:

    2500 free requests/day - now $200 credit/month 
    50 requests/second maxiumum
    '''
    try:
        geoad = geolookup.geocode(address)
        lat = geoad[0]['geometry']['location']['lat']
        lng = geoad[0]['geometry']['location']['lng']
    except:
        lat = np.NaN
        lng = np.NaN
    print(lat,lng)
    time.sleep(delay)
    return lat, lng

# get api key and instantiate gmaps client
pathToApiKey = '/home/ubuntu/.gmaps_api/googlemaps.txt'
geoapikey = get_apikey(pathToApiKey)
geolookup = gmaps.Client(key=geoapikey)

def main():
    # get input from user 
    parser = argparse.ArgumentParser(description='Geocoding Lookup')
    
    parser.add_argument('-r', '--pathToRead', 
            type=str, help='File containing addresses to lookup')
    
    parser.add_argument('-w', '--pathToWrite', 
            type=str, default='./geocodedAddresses.csv', 
            help='Where to write results')
    
    parser.add_argument('-a', '--addressColumn', 
            type=str, default='Full Address', 
            help='Where to write results')
    
    args = parser.parse_args()

    fileToRead = args.pathToRead
    fileToWrite = args.pathToWrite
    address_col = args.addressColumn

    addresses = pd.read_csv(fileToRead, index_col=0)
    addresses['GeoLoc'] = addresses[address_col].apply(get_lat_lng)
    addresses.to_csv(fileToWrite, header=['Full Address','GeoLoc'])
    
if __name__ == '__main__':
    main()
