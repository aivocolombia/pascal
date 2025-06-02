from fastapi import APIRouter
from app.controller.real_estate_controller import  buscar_inmuebles_controller
from app.models.request import SearchParams
from fastapi import Header

router = APIRouter()


@router.post("/buscar")
def buscar(params: SearchParams, x_api_key: str = Header(...)):
    return buscar_inmuebles_controller(params, x_api_key)
