if __name__ == '__main__': 
    from transpose import Transpose
    api = Transpose('Zh8OPJBdFF8uz5anWNv5v4vH8UMHzZ6S9Vjq6uRW')
    results = api.parallel_request(api.nft.nfts_by_owner, [{'owner_address': 'alexhimself.eth'}, {'owner_address': 'jbecker.eth'}], requests_per_second=10)