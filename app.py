from sqlmodel import SQLModel, create_engine, Session, select
from fastapi import FastAPI,Body,HTTPException
from dotenv import load_dotenv
from time import tzset
from datetime import datetime
from pytz import timezone
from os import getenv
from models import *

load_dotenv()
tzset()
engine = create_engine(getenv('db_url'),echo=True)
app = FastAPI(on_startup=SQLModel.metadata.create_all(engine))


@app.get("/",status_code=200)
async def base():
    return None


# Dummy route to test callbacks
@app.post("/dump",
response_model=SensorDataRead)
async def dump(dump : SensorDataBase = Body()):
    print(dump)
    with Session(engine) as session:
        newSensorData = SensorData.from_orm(
            SensorDataWrite(
                Temperature = dump.Temperature,
                RelativeTurbidity = dump.RelativeTurbidity,
                TotalDissolvedSolids = dump.TotalDissolvedSolids,
                PH = dump.PH,
                time = datetime.now(timezone('Africa/Nairobi'))
                ))
        session.add(newSensorData)
        session.commit()
        session.refresh(newSensorData)
        return newSensorData

