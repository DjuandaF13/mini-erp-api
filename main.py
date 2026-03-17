from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import engine, SessionLocal

# 1. Membuat tabel di database
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mini ERP Asset Tracker API",
    description="API untuk manajemen stok barang dengan konversi mata uang real-time.",
)


# 2. DEFINISIKAN FUNGSI GET_DB DI SINI (Di atas endpoint)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 3. ENDPOINT API BAWAHNYA
@app.get("/")
def read_root():
    return {"message": "Selamat datang di Sistem Mini ERP!"}


@app.post("/products/", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(
        name=product.name, price=product.price, stock=product.stock
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@app.get("/products/", response_model=List[schemas.ProductResponse])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Perintah ke database: "Ambilkan data dari tabel Product, maksimal 100 barang"
    products = db.query(models.Product).offset(skip).limit(limit).all()
    return products


# --- ENDPOINT UNTUK MENGUBAH DATA BARANG (UPDATE) ---
@app.put("/products/{product_id}", response_model=schemas.ProductResponse)
def update_product(
    product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)
):
    # 1. Cari barangnya di gudang berdasarkan ID
    db_product = (
        db.query(models.Product).filter(models.Product.id == product_id).first()
    )

    # 2. Kalau barang tidak ditemukan, tolak permintaannya
    if db_product is None:
        raise HTTPException(status_code=404, detail="Barang tidak ditemukan di gudang")

    # 3. Kalau ketemu, perbarui datanya dengan data yang baru
    db_product.name = product.name
    db_product.price = product.price
    db_product.stock = product.stock

    # 4. Simpan perubahan ke database
    db.commit()
    db.refresh(db_product)
    return db_product


# --- ENDPOINT UNTUK MENGHAPUS BARANG (DELETE) ---
@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    # 1. Cari barangnya dulu
    db_product = (
        db.query(models.Product).filter(models.Product.id == product_id).first()
    )

    if db_product is None:
        raise HTTPException(status_code=404, detail="Barang tidak ditemukan di gudang")

    # 2. Hapus barang dari database
    db.delete(db_product)
    db.commit()
    return {"message": f"Barang dengan ID {product_id} berhasil dihapus dari sistem"}
