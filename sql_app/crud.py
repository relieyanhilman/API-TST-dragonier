from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime, date

def post_data_pemasukan(db: Session, pembayaran: schemas.Pembayaran):
    rowsPembayaran = db.query(models.Pembayaran).count()
    newRowPembayaran = rowsPembayaran + 1
    rowsDataKeuangan = db.query(models.DataKeuangan).count()
    newRowDataKeuangan = rowsDataKeuangan + 1
    db_data_bayar = models.Pembayaran(idBayar=newRowPembayaran, tanggal=pembayaran.tanggal, metodePembayaran=pembayaran.metodePembayaran, totalHarga=pembayaran.totalHarga, idPesanan=pembayaran.idPesanan)
    db_data_masuk = models.DataKeuangan(idDataKeuangan=newRowDataKeuangan, idDataPemasukan=newRowPembayaran, tanggal=pembayaran.tanggal)
    db.add(db_data_bayar)
    db.add(db_data_masuk)
    db.commit()
    db.refresh(db_data_bayar)
    db.refresh(db_data_masuk)
    return db_data_bayar

def post_data_pengeluaran(db: Session, pengeluaran: schemas.Pengeluaran):
    rowsPengeluaran = db.query(models.Pengeluaran).count()
    newRowPengeluaran = rowsPengeluaran + 1
    rowsDataKeuangan = db.query(models.DataKeuangan).count()
    newRowDataKeuangan = rowsDataKeuangan + 1
    db_data_keluar = models.Pengeluaran(idPengeluaran=newRowPengeluaran, deskripsi=pengeluaran.deskripsi, jenis=pengeluaran.jenis, total=pengeluaran.total)
    db_data_keuangan_keluar = models.DataKeuangan(idDataKeuangan=newRowDataKeuangan, idDataPengeluaran= newRowPengeluaran, tanggal=date.today().strftime("%Y-%m-%d"))
    db.add(db_data_keluar)
    db.commit()
    db.refresh(db_data_keluar)
    db.add(db_data_keuangan_keluar)
    db.commit()
    db.refresh(db_data_keuangan_keluar)
    return db_data_keluar

def post_supply_bahan_dasar(db: Session, supplyBahanDasar: schemas.SupplyBahanDasar):
    rowsBahanDasar = db.query(models.SupplyBahanDasar).count()
    newRowBahanDasar= rowsBahanDasar + 1
    rowsPengeluaran = db.query(models.Pengeluaran).count()
    newRowPengeluaran = rowsPengeluaran + 1
    rowsDataKeuangan = db.query(models.DataKeuangan).count()
    newRowDataKeuangan = rowsDataKeuangan + 1
    db_data_bahan = models.SupplyBahanDasar(idPengeluaran=newRowPengeluaran, idBahan=supplyBahanDasar.idBahan, harga=supplyBahanDasar.harga, kuantitas=supplyBahanDasar.kuantitas, idSupplier= supplyBahanDasar.idSupplier, totalHarga=(supplyBahanDasar.kuantitas)*(supplyBahanDasar.harga), tanggal=supplyBahanDasar.tanggal, satuan=supplyBahanDasar.satuan)
    db_data_keluar = models.Pengeluaran(idPengeluaran=newRowPengeluaran, deskripsi="Supply Bahan Dasar", jenis="Supply", total=(supplyBahanDasar.kuantitas)*(supplyBahanDasar.harga))
    db_data_keuangan_keluar = models.DataKeuangan(idDataKeuangan=newRowDataKeuangan, idDataPengeluaran= newRowPengeluaran, tanggal=supplyBahanDasar.tanggal)
    db.add(db_data_keluar)
    db.commit()
    db.refresh(db_data_keluar)
    db.add(db_data_bahan)
    db.add(db_data_keuangan_keluar)
    db.commit()
    db.refresh(db_data_bahan)
    db.refresh(db_data_keuangan_keluar)
    return db_data_bahan
