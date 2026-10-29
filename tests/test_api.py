from app import app


def test_accueil():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert "Campus Café" in response.get_data(as_text=True)


def test_health():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"
    assert "build" in response.json and response.json["machine"]


def test_commande_deux():
    response = app.test_client().get("/commande/2")
    assert response.status_code == 200
    assert response.json == {"quantite": 2, "total": 24, "devise": "DH"}


def test_commande_onze():
    assert app.test_client().get("/commande/11").status_code == 400
