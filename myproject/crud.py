from fastapi import HTTPException
from sqlalchemy.orm import Session
import models, schemas

def get_cd(db: Session, cd_id: int):
    return db.query(models.CD).filter(models.CD.id == cd_id).first()

def get_cds(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CD).offset(skip).limit(limit).all()

def get_artist(db: Session, artist_id: int):
    return db.query(models.Artist).filter(models.Artist.id == artist_id).first()

def get_artists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Artist).offset(skip).limit(limit).all()

def create_artist(db: Session, artist: schemas.ArtistBase):
    db_artist = models.Artist(**artist.dict())
    db.add(db_artist)
    db.commit()
    db.refresh(db_artist)
    return db_artist

def get_reviews_by_cd(db: Session, cd_id: int):
    return db.query(models.Review).filter(models.Review.cd_id == cd_id).all()

def create_review(db: Session, review: schemas.ReviewCreate):
    db_review = models.Review(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def create_cd(db: Session, cd: schemas.CDCreate):
    artist = db.query(models.Artist).filter(models.Artist.name == cd.artist_name).first()
    if not artist:
        raise HTTPException(status_code=404, detail=f"Artist with name {cd.artist_name} not found")
    db_cd = models.CD(title=cd.title, artist_id=artist.id)
    db.add(db_cd)
    db.commit()
    db.refresh(db_cd)
    return db_cd

def delete_cd(db: Session, cd_id: int):
    db_cd = db.query(models.CD).filter(models.CD.id == cd_id).first()
    if db_cd:
        db.delete(db_cd)
        db.commit()
        return True
    return False

def delete_artist(db: Session, artist_id: int):
    db_artist = db.query(models.Artist).filter(models.Artist.id == artist_id).first()
    if db_artist:
        db.delete(db_artist)
        db.commit()
        return db_artist
    return None

