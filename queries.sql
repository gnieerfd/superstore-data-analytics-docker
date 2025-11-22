-- 1. ANALISIS PRODUK PALING RUGI
-- Mencari Sub-Kategori barang yang menghasilkan profit negatif terbesar
SELECT 
    Sub_Category, 
    SUM(Sales) as Total_Sales, 
    SUM(Profit) as Total_Profit
FROM sales_data
GROUP BY Sub_Category
ORDER BY Total_Profit ASC
LIMIT 5;

-- 2. ANALISIS WILAYAH PALING RUGI
-- Mencari Negara Bagian (State) dengan performa profit terburuk
SELECT 
    State, 
    SUM(Profit) as Total_Profit
FROM sales_data
GROUP BY State
ORDER BY Total_Profit ASC
LIMIT 5;

-- 3. ANALISIS DAMPAK DISKON (ROOT CAUSE)
-- Melihat korelasi antara besaran diskon dengan rata-rata profit
SELECT 
    Discount, 
    AVG(Profit) as Rata_Rata_Profit,
    COUNT(*) as Jumlah_Transaksi
FROM sales_data
GROUP BY Discount
ORDER BY Discount ASC;