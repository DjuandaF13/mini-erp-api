from pydantic import BaseModel


# ini adalah bentuk dasar data barang yang kita harapkan dari user
class ProductBase(BaseModel):
    name: str
    price: float
    stock: int


# Schema khusus saat user membuat barang baru
class ProductCreate(ProductBase):
    pass


# Schema khusus saat API membalas/menampilkan data ke user (ada tambahan ID)
class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True
