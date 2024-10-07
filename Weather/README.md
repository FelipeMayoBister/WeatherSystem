# Weather App

## Descrição
Este projeto é uma aplicação simples que permite ao usuário buscar informações sobre o clima de uma cidade, utilizando duas APIs do OpenWeatherMap: a API de Geocodificação e a API de Clima. O usuário pode inserir o nome da cidade, estado e país, e a aplicação retornará as coordenadas geográficas e as condições climáticas atuais.

## Tecnologias Utilizadas
- **Python**: Linguagem de programação utilizada para desenvolver a aplicação.
- **Requests**: Biblioteca Python para realizar requisições HTTP, utilizada para interagir com as APIs.
- **OpenWeatherMap API**:
  - **API de Geocodificação**: Usada para obter as coordenadas (latitude e longitude) de uma cidade com base no nome, estado e país fornecidos.
  - **API de Clima**: Usada para obter as condições climáticas atuais a partir das coordenadas retornadas pela API de Geocodificação.

## Funcionalidades
- Busca por cidades utilizando o nome, estado e país.
- Exibição das coordenadas geográficas da cidade.
- Apresentação das condições climáticas, incluindo temperatura, descrição do clima e umidade.
- Validação de entradas do usuário para evitar erros.
