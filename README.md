# 🛒 Carrinho de Compras

Projeto web simples de carrinho de compras desenvolvido com **Flask**, utilizando formulários com **WTForms**, banco de dados com **Flask-SQLAlchemy** e variáveis de ambiente com **python-dotenv**.

---

## 📦 Sobre o Projeto

Este projeto tem como objetivo criar um sistema web funcional para simular um carrinho de compras, com funcionalidades como:

- Cadastro e autenticação de usuários
- Listagem de produtos
- Adição e remoção de produtos do carrinho
- Armazenamento de dados com SQLite (ou outro banco configurado)
- Interface simples com HTML + CSS

---

## 🚀 Tecnologias Utilizadas

- [Python 3.13+](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-WTF](https://flask-wtf.readthedocs.io/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [Poetry](https://python-poetry.org/)

---

## 📁 Estrutura do Projeto
```
carrinho-compras/
│
├── src/
│ └── carrinho_compras/
│ ├── init.py
│ ├── models.py
│ ├── routes/
│ ├── templates/
│ └── static/
│
├── .env
├── README.md
├── pyproject.toml
└── ...
```


---

## ⚙️ Como Rodar o Projeto

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/carrinho-compras.git
cd carrinho-compras

python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate      # Windows

poetry install

```

## Configure o arquivo .env

FLASK_APP=src/carrinho_compras
FLASK_ENV=development
SECRET_KEY=sua_chave_secreta
DATABASE_URL=sqlite:///banco.db


## Rode a aplicação
poetry run flask run
