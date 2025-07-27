# 📰 Mock Feed Server com FastAPI

Este projeto fornece um servidor local para simular um feed de notícias com anúncios nativos, útil para testes em apps iOS ou Android que consomem uma API.

## 🚀 Requisitos

- Python 3.8+
- pip (gerenciador de pacotes)

## 🔧 Instalação

1. Clone este repositório:

```bash
git clone https://github.com/asfcarvalho/FeedServerMock
cd mock_feed_server
```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install fastapi uvicorn
```

## ▶️ Como Rodar o Servidor

Execute o servidor com:

```bash
uvicorn main:app --reload
```

A API estará disponível em:

```
http://127.0.0.1:8000/feed
```

## 🔗 Exemplo de resposta

```json
[
  {
    "id": "news1",
    "type": "news",
    "title": "Notícia 1",
    "imageUrl": "https://source.unsplash.com/400x300/?news,1",
    "description": "Resumo da notícia 1",
    "fullDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla nec quam a nisi tristique sagittis. Sed vel felis in erat feugiat malesuada.\n\nCurabitur sagittis ligula sit amet augue vulputate, nec malesuada odio ullamcorper. Praesent euismod nisi vitae sem malesuada, ac placerat libero euismod.\n\nFusce vulputate, turpis ac rhoncus cursus, lorem justo pulvinar nibh, a vulputate lorem mi eget justo."
  },
  {
    "id": "ad1",
    "type": "ad",
    "adUnitId": "AD-001",
    "imageUrl": "https://source.unsplash.com/400x300/?advertisement",
    "destinationUrl": "https://example.com/promo"
  }
]
```

## 🧪 Testar com cURL

```bash
curl http://127.0.0.1:8000/feed
```

## 🧰 Tecnologias

- Python
- FastAPI
- Uvicorn

## 📄 Licença

MIT – use livremente.
