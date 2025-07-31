# src/app.py

from flask import Flask, render_template

# Inisialisasi Aplikasi Flask
app = Flask(__name__)

# Data Inventaris Statis
inventory_items = [
    {'id': 1, 'name': 'Laptop', 'quantity': 10, 'price': 15000000.0},
    {'id': 2, 'name': 'Mouse', 'quantity': 50, 'price': 250000.0},
    {'id': 3, 'name': 'Keyboard', 'quantity': 35, 'price': 450000.0}
]

# Route Utama - Hanya Menampilkan Semua Item
@app.route('/')
def index():
    return render_template('index.html', items=inventory_items)

# Menjalankan Aplikasi
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)