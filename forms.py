from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(message='O nome precisa ser preechido.'),
                                              Email(message='E-mail inválido.')])
    senha = PasswordField('Senha', validators=[DataRequired(message='A senha deve ser preenchida.'),
                                               Length(min=8, message='A senha deve ter mais que 8 caracteres.')])
    login = SubmitField('Login')

class CadastroForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(message='O nome precisa ser preenchido')])
    email = StringField('E-mail', validators=[DataRequired(message='O e-mail precisa ser preenchido.'),
                                              Email(message='E-mail inválido.')])
    senha = PasswordField('Senha', validators=[DataRequired(message='A senha precisa ser preenchida.'),
                                               Length(min=8, message='A senha precisa ser superior a 8 caracteres.')])
    conf_senha = PasswordField('Confirmar senha', validators=[DataRequired(message='A senha precisa ser preenchida.'),
                                               Length(min=8, message='A senha precisa ser superior a 8 caracteres.'),
                                               EqualTo('senha', message='As senhas não coincidem.')])
    cadastrar = SubmitField('Cadastrar')

class CarrinhoForm(FlaskForm):
    produto = StringField('Produto', validators=[DataRequired(message='Produto vazio.')])
    preco = FloatField('Preço', validators=[DataRequired(message='O valor não pode estar vazio.')])
    add_carrinho = SubmitField('Adicionar no carrinho')