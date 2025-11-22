import pandas as pd
from sqlalchemy import create_engine

# --- 1. EXTRACT (Baca Data) ---
print("🚀 Memulai Proses ETL...")
# Kita pakai separator otomatis atau ; sesuai file terakhirmu
try:
    df = pd.read_csv('SampleSuperstore.csv', encoding='windows-1252')
except:
    df = pd.read_csv('SampleSuperstore.csv', sep=';', encoding='windows-1252')

print(f"✅ Data Terbaca: {len(df)} baris")

# --- 2. TRANSFORM (Bersih-bersih) ---
# Fix Postal Code (Biar jadi string dan ada nol di depan)
# Kalau kosong/NaN, isi dengan 0, lalu jadikan integer, lalu string zfill 5 digit
df['Postal Code'] = df['Postal Code'].fillna(0).astype(int).astype(str).str.zfill(5)

# Pastikan nama kolom tidak ada spasi biar gampang di SQL (Opsional)
# Mengganti 'Sub-Category' jadi 'Sub_Category', dst.
df.columns = [c.replace(' ', '_').replace('-', '_') for c in df.columns]

print("✅ Data Cleaning Selesai (Postal Code Fixed)")

# --- 3. LOAD (Masuk ke MySQL) ---
# Format koneksi: mysql+mysqlconnector://user:password@host:port/database
db_connection_str = 'mysql+mysqlconnector://analyst:password123@localhost:3306/superstore'
db_connection = create_engine(db_connection_str)

try:
    # Masukkan dataframe ke tabel SQL bernama 'sales_data'
    df.to_sql('sales_data', con=db_connection, if_exists='replace', index=False)
    print("🎉 SUKSES! Data berhasil masuk ke MySQL (Tabel: sales_data)")
except Exception as e:
    print(f"❌ Gagal Load ke DB: {e}")