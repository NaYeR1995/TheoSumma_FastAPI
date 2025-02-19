

from fastapi import FastAPI, HTTPException
from elasticsearch import AsyncElasticsearch
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    es = AsyncElasticsearch("http://localhost:9200")
    app.state.es = es
    try:
        yield
    finally:
        await es.close()

app = FastAPI(lifespan=lifespan)

@app.get('/')
async def run():
    return {"message"}

# Ensure the index exists before indexing
@app.post("/index/")
async def index_document(index: str, doc_id: str, document: dict):
    es: AsyncElasticsearch = app.state.es
    
    # Create index if it does not exist
    exists = await es.indices.exists(index=index)
    if not exists:
        await es.indices.create(index=index)
    
    await es.index(index=index, id=doc_id, document=document)
    return {"message": "Document indexed"}

# Ensure the index exists before searching
@app.get("/search/")
async def search(index: str, query: str):
    es: AsyncElasticsearch = app.state.es
    
    # Check if index exists before searching
    exists = await es.indices.exists(index=index)
    if not exists:
        raise HTTPException(status_code=404, detail=f"Index '{index}' not found")

    response = await es.search(index=index, query={"match": {"content": query}})
    return response["hits"]["hits"]
