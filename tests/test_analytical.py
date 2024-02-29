from transpose import Transpose, api_key
from transpose.src.base import TransposeBadRequest
import pandas as pd
from pandas import DataFrame


def test_basic():
    try:
        api = Transpose(api_key)

        response = api.analytical.query("SELECT * FROM cross_chain.transaction_flows LIMIT 1;")

        assert response['stats']['count'] == 1
        assert len(response['results']) == 1

    except Exception:
        assert False


def test_batch():
    try:
        api = Transpose(api_key)

        response = api.analytical.query("SELECT * FROM cross_chain.transaction_flows LIMIT 10;")

        assert response['stats']['count'] == 10
        assert len(response['results']) == 10

    except Exception:
        assert False


def test_invalid_query():
    try:
        api = Transpose(api_key)

        response = api.analytical.query("SELECT * FROM cross_chan.transaction_flows LIMIT 1;")

        # assert throws
        assert False

    except TransposeBadRequest:
        assert True

    except Exception:
        assert False


def test_query_parameters():
    try:
        api = Transpose(api_key)

        query = "SELECT * FROM cross_chain.transaction_flows WHERE transaction_hash = '{{transaction_hash}}';"
        parameters = {'transaction_hash': '0xeda18199abfc878196798af337c15beba1966b520cc6f68f1014406dfeb23552'}
        response = api.analytical.query(sql_query=query, parameters=parameters)

        assert response['stats']['count'] == 1
        assert len(response['results']) == 1

    except Exception:
        assert False


def test_query_df():

    # if pandas is not installed, skip this test
    if not pd:
        assert True
        return

    try:
        api = Transpose(api_key)
        query = "SELECT * FROM cross_chain.transaction_flows LIMIT 10;"
        response = api.analytical.query(
            query
        ).toPandas()

        assert len(response) == 10
        assert isinstance(response, DataFrame)

    except Exception:
        assert False
