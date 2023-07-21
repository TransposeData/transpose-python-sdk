from transpose import Transpose, api_key


def test_default():
    try:
        api = Transpose(api_key)

        transactions = api.block.transactions_by_block()

        assert len(transactions) >= 1

    except Exception:
        assert False


def test_basic():
    try:
        api = Transpose(api_key)

        transactions = api.block.transactions_by_block(block_number_above=1)

        assert len(transactions) >= 1

    except Exception:
        assert False


def test_cursor():
    try:
        api = Transpose(api_key)

        transactions = api.block.transactions_by_block(block_number_above=1)

        assert len(transactions) >= 1
        assert api._next != None

        transactions = api.block.next()

        assert len(transactions) >= 1

    except Exception:
        assert False


def test_blockrange():
    try:
        api = Transpose(api_key)

        transactions = api.block.transactions_by_block(
            block_number_above=1, block_number_below=100000
        )

        assert len(transactions) >= 1
        assert all(transaction.block_number <= 100000 for transaction in transactions)

    except Exception:
        assert False
