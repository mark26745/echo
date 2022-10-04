from typing import Optional
from sqlmodel import Field,SQLModel
from datetime import datetime
from pytz import timezone

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
    time: datetime = datetime.now(timezone('Africa/Nairobi'))

class SensorDataRead(SensorDataBase):
    Temperature: float
    RelativeTurbidity: float 
    TotalDissolvedSolids: float 
    PH: float
    time: datetime