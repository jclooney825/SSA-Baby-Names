from dataclasses import dataclass

# Record dataclass 

@dataclass(frozen=True)
class Record(object):
    
    # Input values
    name: str
    sex: str
    num: int
    year: int




