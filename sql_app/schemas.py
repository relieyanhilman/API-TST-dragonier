from datetime import date
from typing import List, Optional
from pydantic import BaseModel


class DataKeuangan(BaseModel):
    idDataKeuangan: int
    idDataPemasukan: int
    idDataPengeluaran: int
    idDataBeban: int
    tanggal: date

    class Config:
        orm_mode = True

class Pembayaran(BaseModel):
    idBayar: int
    tanggal: date
    metodePembayaran: str
    totalHarga: float
    idPesanan: int

    class Config:
        orm_mode = True

class Pengeluaran(BaseModel):
    idPengeluaran: int
    deskripsi: str
    jenis: str
    total: int

    class Config:
        orm_mode = True

class SupplyBahanDasar(BaseModel):
    idPengeluaran: int
    idBahan : int
    harga : int
    kuantitas : int
    idSupplier : int
    totalHarga : float
    tanggal : date
    satuan : str

    class Config:
        orm_mode = True

