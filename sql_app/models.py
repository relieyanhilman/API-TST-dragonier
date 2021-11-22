from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Float
from .database import Base


class DataKeuangan(Base):
    __tablename__ = "dataKeuangan"


    idDataKeuangan = Column(Integer, primary_key=True, index=True)
    idDataPemasukan = Column(Integer)
    idDataPengeluaran = Column(Integer)
    idDataBeban = Column(Integer)
    tanggal= Column(Date, index=True)

    # email = Column(String, unique=True, index=True)
    # hashed_password = Column(String)
    # is_active = Column(Boolean, default=True)
    # items = relationship("Item", back_populates="owner")


class Pembayaran(Base):
    __tablename__ = "pembayaran"


    idBayar = Column(Integer, primary_key=True, index=True)
    tanggal = Column(Date, index=True)
    metodePembayaran = Column(String, index=True)
    totalHarga = Column(Float)
    idPesanan = Column(Integer)


    # title = Column(String, index=True)
    # description = Column(String, index=True)
    # owner_id = Column(Integer, ForeignKey("users.id"))
    # owner = relationship("User", back_populates="items")

class Pengeluaran(Base):
    __tablename__ = "pengeluaran"

    idPengeluaran = Column(Integer, primary_key=True, index=True)
    deskripsi = Column(String)
    jenis = Column(String)
    total = Column(Integer)


class SupplyBahanDasar(Base):
    __tablename__ = "supplyBahanDasar"

    idPengeluaran= Column(Integer, primary_key=True, index=True)
    idBahan = Column(Integer)
    harga = Column(Integer)
    kuantitas = Column(Integer)
    idSupplier = Column(Integer)
    totalHarga = Column(Float)
    tanggal = Column(Date)
    satuan = Column(String)

