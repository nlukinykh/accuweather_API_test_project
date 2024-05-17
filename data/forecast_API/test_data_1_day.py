from data.input_data import *
from data.expected_data import *

test_successfull_default = [
    {
        "description": "Existed town with apikey with blank parameters",
        "input_data": {
            "id_town": TOWN1_LOCATION_KEY,
            "api_key": API_KEY,
            "parameters": PARAMETERS_BLANK
            },
        "output_data": {
            "code": 200,
            "length": 2,
            "keys": DAILY_KEYS,
            "headline_keys": DAILY_HEADLINE_KEYS,
            "forecasts_keys": DAILY_FORECASTS_KEYS
        }
    },
    {
        "description": "Existed town with apikey with detailed result",
        "input_data": {
            "id_town": TOWN1_LOCATION_KEY,
            "api_key": API_KEY,
            "parameters": PARAMETERS_TRUE
            },
        "output_data": {
            "code": 200,
            "length": 2,
            "keys": DAILY_KEYS,
            "headline_keys": DAILY_HEADLINE_KEYS,
            "forecasts_keys": DAILY_FORECASTS_KEYS_FULL
        }
    },
    {
        "description": "Existed town with apikey with parameters but with standard result",
        "input_data": {
            "id_town": TOWN1_LOCATION_KEY,
            "api_key": API_KEY,
            "parameters": PARAMETERS_TRUE
            },
        "output_data": {
            "code": 200,
            "length": 2,
            "keys": DAILY_KEYS,
            "headline_keys": DAILY_HEADLINE_KEYS,
            "forecasts_keys": DAILY_FORECASTS_KEYS
        }
    }
]

test_with_incorrect_parameters = [
    {
        "description": "Request with incorrect random key",
        "input_data": {
            "id_town": TOWN1_LOCATION_KEY,
            "api_key": "random",
            "parameters": PARAMETERS_BLANK
            },
        "output_data": {
            "code": 401,
            "code_description": "Unauthorized",
            "message": "Api Authorization failed",
            "reference": "/forecasts/v1/daily/1day/289162?apikey=random"
        }
    },
    {
        "description": "Request with incorrect town id",
        "input_data": {
            "id_town": "random_town",
            "api_key": API_KEY,
            "parameters": PARAMETERS_BLANK
            },
        "output_data": {
            "code": 400,
            "code_description": "Unauthorized",
            "message": "Api Authorization failed",
            "reference": "/forecasts/v1/daily/1day/random_town"
        }
    },
    {
        "description": "Request with blank location id",
        "input_data": {
            "id_town": "",
            "api_key": API_KEY,
            "parameters": PARAMETERS_BLANK
        },
        "output_data": {
            "code": 400,
            "code_description": "Bad Request",
            "message": "Api Authorization failed",
            "reference": "/forecasts/v1/daily/1day/"
        }
    }
]

test_without_api_key = [
    {
        "description": "Request with incorrect random key",
        "input_data": {
            "id_town": TOWN1_LOCATION_KEY,
            "api_key": "",
            "parameters": PARAMETERS_BLANK
            },
        "output_data": {
            "code": 401,
            "faultstring": "Failed to resolve API Key variable request.queryparam.apikey",
            "errorcode": "steps.oauth.v2.FailedToResolveAPIKey"
        }
    }
]

