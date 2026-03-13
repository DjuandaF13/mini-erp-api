# 📦 Mini ERP Backend: Inventory & Asset Tracker API

Sebuah RESTful API yang disimulasikan sebagai *backend* sistem Enterprise Resource Planning (ERP) skala kecil untuk mengelola stok barang (Inventory). Proyek ini dibangun untuk mendemonstrasikan pemahaman mengenai arsitektur *backend*, validasi data, manipulasi *database* dengan ORM, serta integrasi API.

## 🛠️ Tech Stack
- **Bahasa Pemrograman:** Python 3.x
- **Framework:** FastAPI
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Data Validation:** Pydantic
- **Server:** Uvicorn

## ✨ Fitur (Roadmap)
- [x] **Create Product:** Menambahkan barang baru ke dalam gudang beserta detail harga dan jumlah stok.
- [ ] **Read Product:** Melihat daftar seluruh barang yang ada di sistem (Segera hadir).
- [ ] **Update Product:** Mengubah data barang seperti penyesuaian harga atau stok (Segera hadir).
- [ ] **Delete Product:** Menghapus barang dari sistem (Segera hadir).
- [ ] **Live Currency Integration:** Mengonversi total nilai aset ke USD menggunakan *Public API* pihak ketiga secara *real-time* (Segera hadir).

## 🚀 Cara Instalasi & Menjalankan Proyek

Pastikan Python sudah terinstal di komputer Anda. Ikuti langkah-langkah berikut untuk menjalankan API ini di sistem lokal Anda:

**1. Clone Repositori**
```bash
git clone [https://github.com/DjuandaF13/mini-erp-api.git](https://github.com/DjuandaF13/mini-erp-api.git)
cd mini-erp-api