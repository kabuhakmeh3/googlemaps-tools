# googlemaps-tools

This repository contains tools to access googlemaps

Currently only geocoding is supported

More functionality may be added later

To run the geolookup, enter the following at the command line:

```
python geoLookup.py 
```

You have the option to specify several inputs:

+ path to a file containing address
+ path to an output file
+ name of a column containing addresses (for pandas dataframes)

A sample call might look like:

```
python geoLookup.py -r ./input/customers.csv -w ./results/coded_customers.csv
-a "Street Address"
```

To see full options:

```
python geoLookup.py --help
```
