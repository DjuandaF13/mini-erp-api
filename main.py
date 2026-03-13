from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
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
