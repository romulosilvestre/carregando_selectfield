from app import app
from flask import render_template,flash,redirect,url_for
from app.forms.login_form import LoginForm
from app.models.usuario_model import Usuario
from flask_jwt_extended import create_access_token #para criar o access token
from datetime import timedelta #tempo de validade do access token

@app.route("/",methods=["POST","GET"])
def logar_usuario():
     form_login = LoginForm()
     if form_login.validate_on_submit():
        email = form_login.email.data
        senha = form_login.senha.data
        usuario_banco = consultar_email(email)
        
        if usuario_banco and usuario_banco.ver_senha(senha):
            access_token = create_access_token(
                identity=usuario_banco.id,
                expires_delta=timedelta(seconds=100)
            )
            flash('Login realizado com sucesso! Bem-Vindo ao projeto piloto', 'success')  # Mensagem de sucesso
            return render_template("sucesso/index.html")

        else:
            flash('Autenticação não sucedida. Projeto piloto não acessado. Verifique seu email e senha.', 'danger')  # Mensagem de falha
            return render_template("sucesso/erro.html")
    
   

def consultar_email(email):
    usuario = Usuario.query.filter_by(email=email).first()  # Consulta todos os registros na tabela Nivel
    return usuario

