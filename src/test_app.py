# src/test_app.py

import pytest
from app import app as flask_app

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_index_page(client):
    """Tes untuk memastikan halaman utama dapat diakses dan menampilkan data."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Daftar Barang Inventaris" in response.data
    assert b"Laptop" in response.data # Memeriksa salah satu item ada di halaman