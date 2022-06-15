import time
from typing import List
from transpose.extras import CDNResponse
import multiprocessing.pool as multiprocessing


class CDN():
    def __init__(self, base_class) -> None:
        self.super  = base_class


    def query(self, endpoint: str) -> CDNResponse:
        '''
        Queries the CDN for an endpoints.
        
        :param endpoint: The endpoint to query.
        '''
        return self.super.perform_authorized_request(CDNResponse, endpoint)
    
    
    def save(self, endpoint: str, path: str=None) -> None:
        '''
        Saves a file from the CDN to the local disk.
        
        :param endpoint: The endpoint to save the file from.
        :param file: OPTIONAL. The path to save the file to. If not specified, the file will be saved to the current directory.
        '''
        response = self.super.perform_authorized_request(CDNResponse, endpoint)
        
        # if there was no path specified, infer the path from the endpoint
        if path is None:
            path = "-".join(endpoint.split('/')[-2:])
            
        response.save(path)
    
    
    def bulk_query(self, endpoints: List[str], requests_per_second: int=999999999) -> List[object]:
        '''
        Queries the CDN for a list of endpoints.
        
        :param endpoints: The endpoints to query.
        :param requests_per_second: OPTIONAL. The number of requests to make per second.
        '''
        
        # throw if requests_per_second is <= 0
        if requests_per_second <= 0:
            raise Exception("requests_per_second must be > 0")
        
        # set the sleep time
        cooldown = 1.01 / requests_per_second
        
        # ensure requests_per_seconds <= len(endpoints)
        if requests_per_second > len(endpoints):
            requests_per_second = len(endpoints)
            cooldown = 0.001
            
        with multiprocessing.Pool(requests_per_second) as pool:
            return pool.starmap(self._limited_query, [(endpoint, cooldown) for endpoint in endpoints])
        
        
    def bulk_save(self, endpoints: List[str], requests_per_second: int=50, dir: str=None) -> None:
        '''
        Saves a list of files from the CDN to the local disk.
        
        :param endpoints: The endpoints to save the files from.
        :param dir: OPTIONAL. The directory to save the files to. If not specified, the files will be saved to the current directory.
        :param requests_per_second: OPTIONAL. The number of requests to make per second.
        '''
        
        # throw if requests_per_second is <= 0
        if requests_per_second <= 0:
            raise Exception("requests_per_second must be > 0")
        
        # set the sleep time
        cooldown = 1.01 / requests_per_second
        
        # ensure requests_per_seconds <= len(endpoints)
        if requests_per_second > len(endpoints):
            requests_per_second = len(endpoints)
            cooldown = 0.001
            
        if requests_per_second >= 50: requests_per_second = 50
            
        with multiprocessing.Pool(requests_per_second) as pool:
            return pool.starmap(self._limited_save, [(endpoint, cooldown, dir) for endpoint in endpoints])
        

    def _limited_query(self, endpoint: str, sleep_time: int=0) -> CDNResponse:
        try:
            response = self.super.perform_authorized_request(CDNResponse, endpoint)
            
            time.sleep(sleep_time)
            return response.to_dict()
        except:
            return None
    
    
    def _limited_save(self, endpoint: str, sleep_time: int=0, dir: str=None) -> CDNResponse:
        try:
            response = self.super.perform_authorized_request(CDNResponse, endpoint)
            
            path = "-".join(endpoint.split('/')[-2:])
            if dir is not None: path = dir + "/" + path
            
            response.save(path)
            time.sleep(sleep_time)
        except:
            pass
        return None