from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UsuarioCarrinho(db.Model):
    __tablename__ = 'usuario_carrinho'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    produtos = db.relationship('Produto', backref='usuario_carrinho')

class Produto(db.Model):
    __tablename__ = 'produto'

    id = db.Column(db.Integer, primary_key=True)
    produto = db.Column(db.String(150), nullable=False, unique=True)
    qnt_produto = db.Column(db.Integer, nullable=False, default=1)
    preco = db.Column(db.Float, nullable=False)

    usuario_carrinho_id = db.Column(db.Integer, db.ForeignKey('usuario_carrinho.id'))
