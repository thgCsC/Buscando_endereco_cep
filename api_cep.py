#!/home/thg-dev/Área de Trabalho/PY Projetos/Api_CEP/.env/bin/python3
import requests
pesquisa = input('Digite seu CEP: ')
buscar_cep =  [pesquisa]          # input('Digite seu CEP: ')
lista_endereco = []

#Estruturar a pesquisa na API
for cep in buscar_cep:
    url = 'https://viacep.com.br/ws/{}/json/'.format(cep)
    resposta = requests.get(url, timeout = 3)
    endereco = resposta.json()
    lista_endereco.append([endereco["cep"],
                           endereco["logradouro"],
                           endereco["bairro"],
                           endereco["localidade"],
                           endereco["uf"],
                           endereco["ddd"]])
for item in lista_endereco:
    print(item)