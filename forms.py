from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FloatField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(message='O nome precisa ser preechido.')])
    senha = PasswordField('Senha', validators=[DataRequired(message='A senha deve ser preenchida.'),
                                               Length(min=8, message='A senha deve ter mais que 8 caracteres.')])
    login = SubmitField('Login')

class CarrinhoForm(FlaskForm):
    produto = StringField('Produto', validators=[DataRequired(message='Produto vazio.')])
    preco = FloatField('Preço', validators=[DataRequired(message='O valor não pode estar vazio.')])
    add_carrinho = SubmitField('Adicionar no carrinho')