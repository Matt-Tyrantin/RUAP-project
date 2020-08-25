import urllib2
import json 

API_KEY = 'OkBFV/GW3n/rfqOXChEb+/yp3oe/s7pPa0UzKm0tW6dJAau16MWuou28WKI+KSZxpUGfD6tgwHhxlWRl4WeCoA=='
URL = 'https://ussouthcentral.services.azureml.net/workspaces/92518c6337964d95af1c417d83471dec/services/535fd871d310474ea32a096456a43822/execute?api-version=2.0&details=true'

MAX_VALUE = 1000000000

def predict_single(form_data):
    app_category = form_data['app_category']
    app_rating = form_data['app_rating'] or 0
    app_ratings = form_data['app_ratings'] or 0
    app_installs = form_data['app_installs'] or 0
    app_price = form_data['app_price']
    app_content_rating = form_data['app_content_rating']

    data =  {
        "Inputs": {
            "input1":
            {
                "ColumnNames": ["Category", "Rating", "Reviews", "Installs", "Price", "Content Rating"],
                "Values": [[app_category, app_rating, app_ratings, app_installs, app_price, app_content_rating]]
            },        
        },
        "GlobalParameters": {}
    }

    body = str.encode(json.dumps(data))
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ API_KEY)}

    req = urllib2.Request(URL, body, headers) 

    try:
        response = urllib2.urlopen(req)
        result = response.read()

        raw_value = float(json.loads(result)['Results']['output1']['value']['Values'][0][0])

        result_value = max(0, int(raw_value * MAX_VALUE))

        return str(result_value)

    except urllib2.HTTPError, error:
        return str(error.code) + str(error.info()) + str(json.loads(error.read()))
