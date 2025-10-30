from app import app


def test_index_route():
client = app.test_client()
response = client.get('/')
assert response.status_code == 200
assert b'MaÃ§Ã£' in response.data # verifica se "Maçã" aparece


# Teste simples para verificar a rota /greet/<name>
def test_greet_route():
client = app.test_client()
response = client.get('/greet/Rai')
assert response.status_code == 200
assert b'Rai' in response.data
