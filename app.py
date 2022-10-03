from fastapi import FastAPI,Body
app = FastAPI()



@app.get("/",status_code=200)
async def base():
    return None


# Dummy route to test callbacks
@app.post("/dump")
async def dump(dump = Body()):
    print(dump)
    return dump

