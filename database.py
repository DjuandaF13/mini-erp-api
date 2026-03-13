from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Kita menggunakan SQLite karena ringan dan tidak perlu server tambahan
SQLALCHEMY_DATABASE_URL = "sqlite:///./minierp.db"

# Engine adalah mesin utama yang menghubungkan Python ke file SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal adalah sesi kita setiap kali ingin menyimpan/mengambil data
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base adalah pondasi untuk membuat tabel-tabel kita nanti
Base = declarative_base()
