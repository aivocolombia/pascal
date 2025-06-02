from pydantic import BaseModel
from typing import Optional, List

class SearchParams(BaseModel):
    realEstateTypeList: str
    realEstateBusinessList: str
    city: str
    roomList: Optional[str] = None
    bathroomList: Optional[str] = None
    max_results: Optional[int] = 50
    page: Optional[int] = 1
    areaRange: Optional[int] = None
    areaRangeMin: Optional[int] = None