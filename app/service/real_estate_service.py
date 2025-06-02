import requests
from fastapi import HTTPException

from app.config import API_KEY_METRO_CUADRADO
from app.models.request import SearchParams

def buscar_inmuebles_service(params:SearchParams, max_results=50, page=1):
    url = "https://www.metrocuadrado.com/rest-search/search"

    headers = {
        "accept": "*/*",
        "content-type": "application/json",
        "referer": "https://www.metrocuadrado.com/apartamento/venta/bogota/?search=form",
        "x-api-key": API_KEY_METRO_CUADRADO,
        "user-agent": "Mozilla/5.0"
    }
    print(f"Headers: {headers}")
    query_params = {
        "size": str(max_results),
        "from": "0",
        "realEstateTypeList": params.realEstateTypeList,
        "realEstateBusinessList": params.realEstateBusinessList,
        "city": params.city
    }

    if params.roomList:
        query_params["roomList"] = params.roomList
    if params.bathroomList:
        query_params["bathroomList"] = params.bathroomList
    print(f"Query Params: {query_params}")
    print
    response = requests.get(url, headers=headers, params=query_params)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Error al consultar Metrocuadrado")

    data = response.json()
    results = data.get("results", [])

    filtered_results = [r for r in results if r.get("areaPrivada") is not None]

    results_per_page = 5
    start = (page - 1) * results_per_page
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

    return final_output
