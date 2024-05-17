import pytest
import data.forecast_API.test_data_1_day as test_data_1_day
from make_requests import make_request


@pytest.mark.parametrize("positive_tests", test_data_1_day.test_successfull_default,
                         ids=lambda test: test['description'])
def test_get_simple_response_for_1_day_success(positive_tests: dict):
    input_data = positive_tests["input_data"]
    output_data = positive_tests["output_data"]
    # Act:
    response = make_request(input_data["id_town"], input_data["api_key"], input_data["parameters"])
    data = response.json()

    # Assertion:
    assert response.status_code == output_data["code"]
    assert len(data) == output_data["length"]
    assert list(data.keys()) == output_data["keys"]
    assert list(data["Headline"].keys()) == output_data["headline_keys"]
    assert list(list(data['DailyForecasts'][0].keys())) == output_data["forecasts_keys"]


@pytest.mark.parametrize("incorrect_parameters_tests", test_data_1_day.test_with_incorrect_parameters,
                         ids=lambda test: test['description'])
def test_get_response_for_1_day_with_incorrect_parameters(incorrect_parameters_tests: dict):
    input_data = incorrect_parameters_tests["input_data"]
    output_data = incorrect_parameters_tests["output_data"]
    # Act:
    response = make_request(input_data["id_town"], input_data["api_key"], input_data["parameters"])
    data = response.json()
    # Assertion:
    assert response.status_code == output_data["code"]  # Validation of status code
    assert len(data) == output_data["length"]
    assert data["Code"] == output_data["code_description"]
    assert data["Message"] == output_data["message"]
    assert data["Reference"] == output_data["length"]


@pytest.mark.xfail(reason="#2-3 - need to clarify status code")
@pytest.mark.parametrize("test_without_api_key", test_data_1_day.test_without_api_key,
                         ids=lambda test: test['description'])
def test_get_full_response_for_1_day_without_apikey(test_without_api_key: dict):
    input_data = test_without_api_key["input_data"]
    output_data = test_without_api_key["output_data"]
    # Act:
    response = make_request(input_data["id_town"], input_data["api_key"], input_data["parameters"])
    data = response.json()
    # Assertion:
    assert response.status_code == output_data["code"]  # Validation of status code
    assert data['fault']['faultstring'] == output_data["faultstring"]
    assert data['fault']['detail']['errorcode'] == output_data["errorcode"]
