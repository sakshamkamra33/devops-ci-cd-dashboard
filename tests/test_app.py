import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_home():
    app.testing = True
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200


def test_about():
    app.testing = True
    client = app.test_client()
    response = client.get('/about')
    assert response.status_code == 200


def test_status():
    app.testing = True
    client = app.test_client()

    # 🔐 Step 1: Login
    login_response = client.post('/login', json={
        "username": "admin",
        "password": "123"
    })

    assert login_response.status_code == 200

    token = login_response.get_json()['token']

    # 🔑 Step 2: Call protected route with token
    response = client.get('/status', headers={
        'x-access-token': token
    })

    assert response.status_code == 200