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
        return '<{}{}>'.format(self.model_name, "".join(" {}=\"{}\"".format(key, value) for key, value in self.data.items()))


class TransposeAPIResponse:
    def __init__(self, name: str, data: List[object]) -> None:
        self.data_model_name = name
        self.data = [TransposeModel(name, d) for d in data]
        
        if len(self.data) == 1:
            for key, value in data[0].items():
                setattr(self, key, value)
    
    # representation as a TransposeAPIResponse object
    def __repr__(self) -> str:
        
        # if there's only one item in the list, return the representation of the TransposeModel object
        if len(self.data) == 1:
            return self.data[0].__repr__()
        
        return '<TransposeAPIResponse type="{}" size="{}" id="{}">'.format(self.data_model_name, len(self.data), id(self))
    
    def __getitem__(self, key: Any) -> Any:
        return self.data[key]
    
    # Get the length of the TransposeModel data list
    def __len__(self) -> int:
        return len(self.data)
    
    def __dict__(self) -> dict:
        return [d.__dict__() for d in self.data]