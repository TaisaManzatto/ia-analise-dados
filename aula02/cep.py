#API
import requests

cep = input("Digite seu CEP: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

dados = requests.get(url)
resposta = dados.json()
# Quando puxamos dados necessário informar formato (JSON)

# print(resposta)
#print(resposta["logradouro"])
print(f"Você mora na {resposta["logradouro"]}, no bairro {resposta["bairro"]}, na Cidade de {resposta["localidade"]}")
#GET = consultar informações
#POST = postar
