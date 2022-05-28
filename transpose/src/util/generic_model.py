import json
from typing import Any, List

class TransposeModel:
    def __init__(self, name: str='TransposeDataModel', data: object={}) -> None:
        self.model_name = name
        self.data = data

        # convert the dict object into class attributes
        for key, value in data.items():
            setattr(self, key, value)
    
    # the data object should be returned when the object is converted to a dict
    def __dict__(self) -> dict:
        return self.data
    
    # generic class representation
    def __repr__(self) -> str:
        return '<{} id={}>'.format(self.model_name, id(self))


class TransposeAPIResponse:
    def __init__(self, name: str, data: List[object]) -> None:
        self.data_model_name = name
        self.data = [TransposeModel(name, d) for d in data]
    
    # representation as a TransposeAPIResponse object
    def __repr__(self) -> str:
        return '<TransposeAPIResponse type={} size={} id={}>'.format(self.data_model_name, len(self.data), id(self))