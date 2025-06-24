from fastapi import FastAPI
from agent_runner import run_agent

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Prince!"}

@app.get("/query")
async def query_func(query:str):
    return run_agent(query)
