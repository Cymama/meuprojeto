from app import app, db
from flask import render_template, url_for, request, flash, redirect
from app.forms import Contato
from app.models import ContatoModel
from app.forms import CadastroForm

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

@app.route('/login')
def login():
    return render_template ('login.html', titulo = 'Login')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastrar():
    cadastro = CadastroForm()
    
    if cadastro.validate_on_submit():
        print('Acessou a rota cadastro')
        nome = cadastro.nome.data
        sobrenome = cadastro.sobrenome.data
        email = cadastro.email.data
        senha = cadastro.senha.data

        novo_cadastro = CadastroForm(nome=nome, sobrenome=sobrenome, email=email, senha=senha)
        db.session.add(novo_cadastro)
        db.session.commit()
        
        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('index'))  
    return render_template ('cadastro.html', titulo = 'cadastro', cadastro = cadastro)
    

@app.route('/teste')
def teste():
    return render_template ('teste.html')