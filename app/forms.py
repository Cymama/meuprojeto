from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TelField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect


class Contato(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email= EmailField ('email', validators=[DataRequired()])
    telefone= TelField ('telefone', validators=[DataRequired()])    
    mensagem= TextAreaField ('mensagem') 
    enviar= SubmitField ('enviar') 
    


class CadastroForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    cpf = StringField('CPF', validators=[DataRequired()])
    telefone= TelField ('Telefone', validators=[DataRequired()])   
    endereco_rua = StringField('Endereço', validators=[DataRequired()])
    endereco_cep = StringField('CEP', validators=[DataRequired()])
    endereco_bairro = StringField('Bairro', validators=[DataRequired()])
    endereco_cidade = StringField('Cidade', validators=[DataRequired()])
    endereco_uf = StringField('UF', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    enviar= SubmitField ('enviar') 
    
