from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from dotenv import load_dotenv
import os
import requests
load_dotenv()  
app = FastAPI()

INTERNAL_API_KEY = os.getenv("api_key_internal")
API_KEY_METRO_CUADRADO = os.getenv("api_key_metro_cuadrado")


class SearchParams(BaseModel):
    realEstateTypeList: str
    realEstateBusinessList: str
    city: str
    roomList: Optional[str] = None
    bathroomList: Optional[str] = None
    max_results: Optional[int] = 50
    page: Optional[int] = 1

@app.post("/buscar")
def buscar_inmuebles(params: SearchParams, x_api_key: str = Header(...)):

    if x_api_key != INTERNAL_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    url = "https://www.metrocuadrado.com/rest-search/search"

    headers = {
        "accept": "*/*",
        "content-type": "application/json",
        "referer": "https://www.metrocuadrado.com/apartamento/venta/bogota/?search=form",
        "x-api-key": API_KEY_METRO_CUADRADO,
        "user-agent": "Mozilla/5.0"
    }

    query_params = {
        "size": str(params.max_results),
        "from": "0",
        "realEstateTypeList": params.realEstateTypeList,
        "realEstateBusinessList": params.realEstateBusinessList,
        "city": params.city
    }

    if params.roomList:
        query_params["roomList"] = params.roomList
    if params.bathroomList:
        query_params["bathroomList"] = params.bathroomList

    response = requests.get(url, headers=headers, params=query_params)

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Error al consultar Metrocuadrado")

    data = response.json()
    results = data.get("results", [])

    filtered_results = [r for r in results if r.get("areaPrivada") is not None]

    results_per_page = 5
    start = (params.page - 1) * results_per_page
    end = start + results_per_page
    paged_results = filtered_results[start:end]

    base_url = "https://www.metrocuadrado.com"
    final_output = []

    for r in paged_results:
        final_output.append({
            "titulo": r.get("title"),
            "tipo_inmueble": r.get("mtipoinmueble", {}).get("nombre"),
            "cuartos": r.get("mnrocuartos"),
            "baños": r.get("mnrobanos"),
            "garajes": r.get("mnrogarajes"),
            "area_privada": r.get("areaPrivada"),
            "url": base_url + r.get("link", "")
        })

    return {"resultados": final_output}
