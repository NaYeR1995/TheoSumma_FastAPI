from fastapi import FastAPI, HTTPException
app = FastAPI()

@app.get('/')
async def run():
    return {"message"}
