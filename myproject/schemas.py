from pydantic import BaseModel
from typing import List

class ArtistBase(BaseModel):
    name: str

class Artist(ArtistBase):
    id: int
    class Config:
        orm_mode = True

class CDCreate(BaseModel):
    title: str
    artist_id: int

class CD(CDCreate):
    id: int
    class Config:
        orm_mode = True

class ReviewBase(BaseModel):
    rating: float
    comment: str

class ReviewCreate(ReviewBase):
    cd_id: int

class Review(ReviewBase):
    id: int
    class Config:
        orm_mode = True
