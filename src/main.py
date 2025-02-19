from fastapi import FastAPI;

app = FastAPI()


@app.get('/')
async def run():
    return {"message"}