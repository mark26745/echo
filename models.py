from typing import Optional
from sqlmodel import Field,SQLModel
from datetime import datetime


# Base classes
class SensorDataBase(SQLModel):
    Temperature: float
    RelativeTurbidity: float 
    TotalDissolvedSolids: float 
    PH: float
    time: Optional[datetime] 

# Tables
class SensorData(SensorDataBase,table=True):
    streamID: Optional[int] = Field(default=None,primary_key=True) 

# IO
class SensorDataWrite(SensorDataBase):
    pass

class SensorDataRead(SensorDataBase):
    Temperature: float
    RelativeTurbidity: float 
    TotalDissolvedSolids: float 
    PH: float
    time: datetime