from app import app, db , bcrypt
from flask import render_template, url_for, request, flash, redirect, session
from app.forms import Contato
from app.models import ContatoModel, CadastroModel
from app.forms import CadastroForm
from flask_bcrypt import check_password_hash
import time
@app.route('/')
def index():
    return render_template ('index.html', titulo = 'Página imicial')

@app.route('/contatos', methods=['POST', 'GET'])
def contatos():
    dados_formulario = None
    formulario = Contato()
    print('Acessou a rota contatos!')
    if formulario.validate_on_submit():
        flash('Seu formulário foi enviado com sucesso!')
        nome = formulario.nome.data
        email = formulario.email.data
        telefone = formulario.telefone.data
        mensagem = formulario.mensagem.data

        novo_contato = ContatoModel(nome=nome, email=email, telefone=telefone, mensagem=mensagem)
        db.session.add(novo_contato)
        db.session.commit()

 

    return render_template ('contatos.html', titulo = 'Contatos', formulario=formulario, dados_formulario = dados_formulario)

@app.route('/sobre')
def sobre():
    return render_template ('sobre.html', titulo = 'Sobre')

@app.route('/projetos')
def projetos():
    return render_template ('projetos.html', titulo = 'Projetos')

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email= request.form.get ('email').lower()
        senha= request.form.get ('senha')
        usuario = CadastroModel.query.filter_by(email=email).first()
        if usuario and check_password_hash (usuario.senha, senha):
            session ['email'] = usuario.email
            session['nome'] = usuario.nome
            session['sobrenome'] = usuario.sobrenome
            time.sleep(2)
            return redirect(url_for('index'))
        else:
            flash('Email ou senha invalido!')

    return render_template('login.html', titulo='Login')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastrar():
    cadastro = CadastroForm()
    
    if cadastro.validate_on_submit():
        print('Acessou a rota cadastro')
        nome = cadastro.nome.data
        sobrenome = cadastro.sobrenome.data
        email = cadastro.email.data
        cpf = cadastro.cpf.data
        telefone = cadastro.telefone.data
        endereco_rua = cadastro.endereco_rua.data
        endereco_cep = cadastro.endereco_cep.data
        endereco_bairro = cadastro.endereco_bairro.data
        endereco_cidade = cadastro.endereco_cidade.data
        endereco_uf = cadastro.endereco_uf.data
        senha = cadastro.senha.data
        hash_senha = bcrypt.generate_password_hash(senha).decode('utf-8')
        novo_cadastro = CadastroModel(nome=nome, sobrenome=sobrenome, email=email, cpf=cpf, telefone=telefone, endereco_rua=endereco_rua, endereco_cep=endereco_cep, endereco_bairro=endereco_bairro, endereco_cidade=endereco_cidade,endereco_uf=endereco_uf,senha=hash_senha)
        db.session.add(novo_cadastro)
        db.session.commit()
        
        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('index'))  
    return render_template ('cadastro.html', titulo = 'cadastro', cadastro = cadastro)
    

@app.route('/teste')
def teste():
    return render_template ('teste.html')



@app.route('/sair')
def sair():
    session.pop('email', None)
    session.pop('nome', None)
    session.pop('sobrenome', None)
    session.pop('senha', None)
    return redirect (url_for('login'))


@app.route('/editar', methods=['POST','GET'])
def editar():
    if 'email'not in session:
        return redirect (url_for('login'))
    
    usuario = CadastroModel.query.filter_by(email = session ['email']).first()
    if request.method == 'POST':
        usuario.nome = request.form.get('nome')
        usuario.sobrenome = request.form.get('sobrenome')
        usuario.email = request.form.get('email')
        senha = request.form.get('senha')
        usuario.senha = bcrypt.generate_password_hash(senha).decode('utf-8')
        db.session.commit()
        session['email'] = usuario.email
        session['nome'] = usuario.nome
        session['sobrenome'] = usuario.sobrenome
        session['senha'] = usuario.senha
        flash('Seus dados foram atualizados com sucesso')


    return render_template ('editar.html', titulo = 'Editar', usuario=usuario)

@app.route('/excluir_conta', methods=['GET'])
def excluir_conta():
    if 'email'not in session:
        return redirect (url_for('login'))
    
    usuario = CadastroModel.query.filter_by(email = session['email']).first()
    db.session.delete(usuario)
    db.session.commit()
    session.clear()

    flash('Sua conta foi excluida com sucesso!')
    return redirect(url_for('cadastrar'))



