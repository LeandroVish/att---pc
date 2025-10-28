# 9. Importe o pacote requests e faça uma requisição HTTP para um URL e exiba o código de status.

import requests
response = requests.get('https://www.example.com')
print(f"Código de status da requisição: {response.status_code}")