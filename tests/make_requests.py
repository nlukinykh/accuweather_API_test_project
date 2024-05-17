import requests

BASE_URL = "http://dataservice.accuweather.com/forecasts/v1"
DAILY = "/daily"
DAYS_COUNTS = "/1day"

'''
location_key - code of town
apikey - key of developer to be able to connect to the accuweather
parameters - Dictionary - must have to include apikey, optional: 
    {language = "en-US", details = False, metric = False} 
'''
def make_request(location_key, apikey, parameters):
    base_url = f"{BASE_URL}{DAILY}{DAYS_COUNTS}/"

    apikey = f"apikey={apikey}" if apikey != "" else ""
    p_language = check_parameters(parameters, "language")
    p_details = check_parameters(parameters, "details")
    p_metrics = check_parameters(parameters, "metrics")

    response = requests.get(f'{base_url}{location_key}?{apikey}{p_language}{p_details}{p_metrics}')
    return response

def check_parameters(parameters, parameter):
    try:
        value = parameters[(parameter)]
        return f"&{parameter}={value}"
    except KeyError as e:
        return ""
