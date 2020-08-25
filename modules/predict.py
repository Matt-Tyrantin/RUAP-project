import urllib2
# If you are using Python 3+, import urllib instead of urllib2

import json 


data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": ["App", "Category", "Rating", "Reviews", "Size", "Installs", "Type", "Price", "Content Rating", "Genres", "Last Updated", "Current Ver", "Android Ver"],
                    "Values": [ [ "value", "ART_AND_DESIGN", "0", "0", "value", "0", "value", "0", "Adults only 18+", "value", "", "value", "value" ], [ "value", "ART_AND_DESIGN", "0", "0", "value", "0", "value", "0", "Adults only 18+", "value", "", "value", "value" ], ]
                },        },
            "GlobalParameters": {
}
    }

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/92518c6337964d95af1c417d83471dec/services/535fd871d310474ea32a096456a43822/execute?api-version=2.0&details=true'
api_key = 'OkBFV/GW3n/rfqOXChEb+/yp3oe/s7pPa0UzKm0tW6dJAau16MWuou28WKI+KSZxpUGfD6tgwHhxlWRl4WeCoA==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib2.Request(url, body, headers) 

try:
    response = urllib2.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers) 
    # response = urllib.request.urlopen(req)

    result = response.read()
    print(result) 
except urllib2.HTTPError, error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))    
