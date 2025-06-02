from fastapi import HTTPException
from app.service.real_estate_service import buscar_inmuebles_service
from app.models.request import SearchParams
import os

from app.config import INTERNAL_API_KEY
print(f"INTERNAL_API_KEY: {INTERNAL_API_KEY}")
def buscar_inmuebles_controller(params: SearchParams, x_api_key: str):
    if x_api_key != INTERNAL_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    resultados = buscar_inmuebles_service(params, max_results=params.max_results, page=params.page)
    return {"resultados": resultados}
