# 🛒 Superstore Data Analytics (End-to-End with Docker)

Proyek ini adalah simulasi Business Intelligence (BI) modern untuk menganalisis profitabilitas data retail "Superstore". 

Berbeda dengan analisis Excel biasa, proyek ini dibangun menggunakan **Full-Stack Data Pipeline** mulai dari database, ETL process, hingga visualisasi dashboard.

## 📊 Dashboard Preview
![Dashboard Metabase](Dashboard.jpg)

## 📄 Full Report
[Download Laporan Analisis Lengkap (PDF)](Superstore_Analysis_Report.pdf)

## 🛠️ Tech Stack
* **Infrastructure:** Docker & Docker Compose
* **Database:** MySQL 8.0
* **ETL (Data Processing):** Python (Pandas, SQLAlchemy)
* **Visualization/BI:** Metabase

## 📂 Project Structure
* `docker-compose.yml`: Konfigurasi container MySQL dan Metabase.
* `etl_script.py`: Script Python untuk membersihkan data CSV dan upload ke MySQL.
* `queries.sql`: Kumpulan query SQL yang digunakan untuk analisis bisnis.
* `SampleSuperstore.csv`: Dataset mentah.

## 🚀 How to Run

1.  **Clone Repository**
    ```bash
    git clone https://github.com/gnieerfd/superstore-data-analytics-docker.git
    cd superstore-data-analytics-docker
    ```

2.  **Jalankan Docker**
    Pastikan Docker Desktop sudah menyala, lalu run:
    ```bash
    docker-compose up -d
    ```

3.  **Jalankan ETL Process**
    Install library yang dibutuhkan dan jalankan script:
    ```bash
    pip install pandas sqlalchemy mysql-connector-python
    python etl_script.py
    ```
    *Tunggu hingga muncul pesan: "🎉 SUKSES! Data berhasil masuk ke MySQL"*

4.  **Akses Dashboard**
    * Buka browser: `http://localhost:3000`
    * Setup Metabase dan koneksikan ke Database MySQL (Host: `db`, User: `analyst`, Pass: `password123`).
    * Jalankan query SQL dan buat visualisasi.

## 💡 Key Insights
1.  **Produk:** Kategori 'Tables' menghasilkan kerugian terbesar meskipun penjualan tinggi.
2.  **Lokasi:** Texas dan Ohio adalah pasar dengan performa profit terburuk.
3.  **Strategi Diskon:** Pemberian diskon di atas **20%** terbukti menjadi penyebab utama kerugian (negative profit).

### 🔒 Security Note
Untuk tujuan demonstrasi, kredensial database (username/password) ditulis langsung (hardcoded) dalam script.
Dalam lingkungan produksi (production), kredensial ini sebaiknya disimpan menggunakan **Environment Variables (.env)** agar lebih aman.

---
**Author:** Gania Rafidah Huwaida (Teknik Komputer Universitas Brawijaya)






