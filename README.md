# 📦 Mini ERP Backend: Inventory & Asset Tracker API

Sebuah RESTful API yang disimulasikan sebagai *backend* sistem Enterprise Resource Planning (ERP) skala kecil untuk mengelola stok barang (Inventory). Proyek ini dibangun untuk mendemonstrasikan pemahaman mengenai arsitektur *backend*, validasi data, manipulasi *database* dengan ORM, serta integrasi API eksternal.

## 🛠️ Tech Stack & Architecture
- **Python 3.x:** Bahasa pemrograman dasar yang menopang seluruh logika bisnis (*backend*).
- **FastAPI:** *Framework* modern dan cepat untuk membangun RESTful API. Dipilih karena kemampuannya menghasilkan dokumentasi interaktif (Swagger UI) secara otomatis.
- **SQLite:** *Database* relasional yang terintegrasi untuk menyimpan data stok barang secara persisten.
- **SQLAlchemy (ORM):** *Object-Relational Mapping* yang bertugas menjembatani interaksi antara kode Python dan *database* tanpa perlu menulis kueri SQL mentah.
- **Pydantic:** Digunakan sebagai "penjaga gerbang" untuk memvalidasi struktur data (*schema*) yang masuk (seperti memastikan harga berupa angka) dan keluar dari API.
- **Uvicorn:** ASGI *server* berkinerja tinggi yang digunakan untuk menjalankan aplikasi FastAPI di lingkungan lokal.
- **Requests:** *Library* Python yang bertugas sebagai HTTP *client* untuk mengambil data kurs mata uang (USD) secara *real-time* dari *Public API* eksternal.
- **Git & GitHub:** Sistem *version control* yang digunakan untuk manajemen kode sumber, pelacakan riwayat perubahan, dan dokumentasi portofolio.

## ✨ Fitur (Roadmap)
- [x] **Create Product:** Menambahkan barang baru ke dalam gudang beserta detail harga dan jumlah stok.
- [x] **Read Product:** Melihat daftar seluruh barang yang ada di sistem.
- [x] **Update Product:** Mengubah data barang seperti penyesuaian harga atau stok.
- [x] **Delete Product:** Menghapus barang dari sistem.
- [x] **Live Currency Integration:** Mengonversi total nilai aset ke USD menggunakan *Public API* pihak ketiga secara *real-time*.