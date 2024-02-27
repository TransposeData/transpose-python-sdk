from transpose import Transpose, api_key


def test_basic():
    try:
        api = Transpose(api_key)

        records = api.ens.records_by_date(timestamp_after='2019-01-01T00:00:00Z',
                                          timestamp_before='2020-01-01T00:00:00Z')

        assert len(records) >= 10
        assert records[0].ens_name is not None
    except Exception:
        assert False


# def test_cursor():
#     try:
#         api = Transpose(api_key)
#
#         records = api.ens.records_by_date(timestamp_after='2019-01-01T00:00:00Z',
#                                           timestamp_before='2020-01-01T00:00:00Z')
#
#         assert len(records) >= 10
#         assert records[0].ens_name is not None
#         assert api._next is not None
#
#         records = api.ens.next()
#
#         assert len(records) >= 10
#         assert records[0].ens_name is not None
#         assert api._next is not None
#     except Exception:
#         assert False
