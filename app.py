from fastapi import FastAPI,Body,HTTPException
app = FastAPI()


# Dummy route to test callbacks
@app.post("/dump",
response_model=SensorDataRead)
async def dump(dump = Body()):
    print(dump)
    return dump

