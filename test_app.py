from app import app

def test_hello():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Hello from CI/CD Pipeline!" in response.data
