from fastapi import FastAPI,Body
app = FastAPI()


# Dummy route to test callbacks
@app.post("/dump")
async def dump(dump = Body()):
    print(dump)
    return dump

