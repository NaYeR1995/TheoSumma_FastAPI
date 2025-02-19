from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get('/')
async def run():
    return {"message"}



from elasticsearch import AsyncElasticsearch

# Initialize Elasticsearch Client
es = AsyncElasticsearch("http://localhost:9200")  # Update with your ES server URL

@app.on_event("startup")
async def startup_event():
    if not await es.ping():
        raise HTTPException(status_code=500, detail="Elasticsearch is unavailable")

@app.on_event("shutdown")
async def shutdown_event():
    await es.close()

# Index a document
@app.post("/index/")
async def index_document(index: str, doc_id: str, document: dict):
    await es.index(index=index, id=doc_id, document=document)
    return {"message": "Document indexed"}

# Search documents
@app.get("/search/")
async def search(index: str, query: str):
    response = await es.search(
        index=index,
        query={"match": {"content": query}}
    )
    return response["hits"]["hits"]
