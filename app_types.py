from pydantic import BaseModel
from typing import List

class ImageSimilarityRequest(BaseModel):
    id:str
    imageUrl:str

class ImageSimilarityResponse(BaseModel):
    similarAlbumIds:List[str] = []