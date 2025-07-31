from flask import Blueprint, render_template, redirect, url_for, flash, session
from forms import LoginForm, CarrinhoForm, CadastroForm
from models import Produto, UsuarioCarrinho, db
from werkzeug.security import check_password_hash, generate_password_hash

carrinho_route = Blueprint('carrinho', __name__, url_prefix='/carrinho')


@carrinho_route.route('/', methods=['GET', 'POST'])
def carrinho():
    form = CarrinhoForm()
    
    if form.validate_on_submit():
        produto = form.produto.data
        preco = form.preco.data
        
        produto_existente = Produto.query.filter_by(produto=produto).first()

        if not produto_existente:
            produto_table = Produto(produto=produto, preco=preco, usuario_carrinho_id=UsuarioCarrinho.query.get(session['usuario_nome']))

            db.session.add(produto_table)
            db.session.commit()

            flash ('Produto adicionado', 'success')
            return redirect(url_for('carrinho.carrinho'))
        else:
            produto_existente.qnt_produto += 1
            db.session.commit()

            flash ('Produto adicionado', 'success')
            return redirect(url_for('carrinho.carrinho'))

    if 'usuario_nome' not in session:

        flash ('Usuário não logado.')
        return redirect(url_for('carrinho.login'))
    else:
        return render_template('carrinho.html', form=form, usuario_nome = session.get('usuario_nome'))

@carrinho_route.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        senha = form.senha.data

        usuario_existente = UsuarioCarrinho.query.filter_by(email=email).first()
        if usuario_existente:
            if check_password_hash(usuario_existente.senha, senha):
                session['usuario_nome'] = usuario_existente.nome
                
                flash ('Usuário logado com sucesso', 'success')
                return redirect(url_for('carrinho.carrinho'))
            else:
                flash ('Senha incorreta.', 'danger')
                return redirect(url_for('carrinho.login'))
        else:
            flash ('Usuário não existe, cadastre-se', 'danger')
            return redirect(url_for('carrinho.cadastrar'))

    return render_template('login.html', form=form, usuario_nome = session.get('usuario_nome'))

@carrinho_route.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    form = CadastroForm()

    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        senha = form.senha.data
        senha_hash = generate_password_hash(senha)

        usuario_existente = UsuarioCarrinho.query.filter_by(email=email).first()

        if not usuario_existente:
            usuario = UsuarioCarrinho(nome=nome, email=email, senha=senha_hash)
            
            db.session.add(usuario)
            db.session.commit()

            return redirect(url_for('carrinho.login'))
        
        else:
            flash ('Usuário já existe.', 'success')
            return redirect(url_for('carrinho.login'))

    return render_template('cadastro.html', form=form, usuario_nome = session.get('usuario_nome'))

@carrinho_route.route('/logout')
def logout():
    session.pop('usuario_nome', None)
    return redirect(url_for('home.home'))