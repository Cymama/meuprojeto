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
    email = StringField('Email', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    enviar= SubmitField ('enviar') 
    cadastrar = SubmitField('Cadastrar')
