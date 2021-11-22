from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/dataKeuangan/pemasukan", response_model=schemas.Pembayaran)
def post_data_pemasukan(pembayaran: schemas.Pembayaran, db: Session = Depends(get_db)):
    return crud.post_data_pemasukan(db=db, pembayaran=pembayaran)

@app.post("/dataKeuangan/pengeluaran", response_model=schemas.Pengeluaran)
def post_data_pengeluaran(pengeluaran: schemas.Pengeluaran, db: Session=Depends(get_db)):
    return crud.post_data_pengeluaran(db=db, pengeluaran=pengeluaran)

@app.post("/dataKeuangan/supplyBahanDasar", response_model=schemas.SupplyBahanDasar)
def post_data_supply_bahan(supplyBahanDasar: schemas.SupplyBahanDasar, db: Session=Depends(get_db)):
    return crud.post_supply_bahan_dasar(db=db, supplyBahanDasar=supplyBahanDasar)