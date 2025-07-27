from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel, HttpUrl
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class FeedComponent(BaseModel):
    id: str
    type: str  # "news" ou "ad"
    title: Optional[str] = None
    imageUrl: Optional[HttpUrl] = None
    description: Optional[str] = None
    fullDescription: Optional[str] = None
    destinationUrl: Optional[HttpUrl] = None
    adUnitId: Optional[str] = None

@app.get("/feed", response_model=List[FeedComponent])
def get_feed():
    json_path = os.path.join(os.path.dirname(__file__), "feed_data.json")
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="feed_data.json não encontrado.")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Erro ao decodificar o JSON.")
