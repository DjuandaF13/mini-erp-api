from sqlalchemy import Column, Integer, String, Float
from database import Base


# Ini adalah representasi dari tabel "produk" dalam database
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    stock = Column(Integer, default=0)
