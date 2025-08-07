import os
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from agents import Runner
from .setup import AppContext, config, triage_agent
import uvicorn


load_dotenv()

app = FastAPI()

cors_origins = os.getenv("CORS_ORIGIN", "")
allowed_origins = [origin.strip() for origin in cors_origins.split(",") if origin.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins or ["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AgentRequest(BaseModel):
    input: str

context = AppContext()

@app.post("/agent")
async def run_agent(request: AgentRequest):
    result = await Runner.run(
        triage_agent,
        request.input,
        run_config=config,
        context=context,
    )
    return {"response": result.final_output}



# ✅ Run directly if script is called via `python main.py`
if __name__ == "__main__":
    uvicorn.run("src.agent.main:app", host="127.0.0.1", port=8000, reload=True)
