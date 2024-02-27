import requests

from transpose import api_key
from transpose.src.util.client import build_headers, handle_response, get_api_request, post_api_request


def test_build_headers():
    assert build_headers('api_key') == {
        'x-api-key': 'api_key',
        'x-request-source': 'python-sdk',
        'Accept': 'application/json',
    }


def test_handle_response():
    response = requests.Response()
    response.status_code = 200
    response._content = b'{"results": [{"a": 1, "b": 2}]}'
    assert handle_response(response) == {'results': [{'a': 1, 'b': 2}]}

    response.status_code = 400
    response._content = b'{"message": "Bad Request"}'
    try:
        handle_response(response)
        assert False
    except Exception:
        assert True


def test_get_api_request():

    url = "https://api.transpose.io/get-schema"
    response = get_api_request(
        url=url,
        api_key=api_key,
    )

    assert isinstance(response, dict)
    assert 'ethereum' in response['schema']
    assert 'settlement_layer' in response['schema']['ethereum']


def test_post_api_request():

    url = "https://api.transpose.io/sql/analytical"
    response = post_api_request(
        url=url,
        api_key=api_key,
        body={
            'sql': "SELECT * FROM cross_chain.transaction_flows LIMIT 1;",
            'parameters': {}
        }
    )
    assert response['stats']['count'] == 1
    assert len(response['results']) == 1
