# Dockerfile

# 1. Gunakan base image resmi Python yang ringan
FROM python:3.9-slim

# 2. Set direktori kerja di dalam container menjadi /app
WORKDIR /app

# 3. Salin file dependensi terlebih dahulu untuk memanfaatkan cache Docker
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 4. Salin semua kode dari direktori 'src' lokal ke direktori kerja di dalam container
COPY ./src .

# 5. Beri tahu Docker bahwa container akan berjalan di port 5001
EXPOSE 5001

# 6. Perintah default untuk menjalankan aplikasi saat container dimulai
CMD ["python", "app.py"]