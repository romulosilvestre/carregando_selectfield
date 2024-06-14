from app import app
from flask import render_template,redirect,url_for,request #renderização
from app.forms import escola_form
from app.models import escola_model
from app import db

@app.route("/cadescola",methods=["POST","GET"])
def cadastrar_escola():
    form = escola_form.EscolaForm()
    
    if form.validate_on_submit():
       nome = form.nome.data #capturando o conteúdo validado
       telefone = form.telefone.data
       escola = escola_model.Escola(nome=nome,telefone=telefone)
       try:
          #adicionar na sessão 
          db.session.add(escola)
          #salvar a sessão
          db.session.commit()
          if request.method == 'POST':
           return redirect(url_for('listar_escolas'))
       except:
         print("nivel não cadastrado")
    return render_template("escola/index.html",form=form,Editar=False)

@app.route("/listarescolas")
def listar_escolas():
    escolas= escola_model.Escola.query.all()  # Consulta todos os registros na escola
    return render_template("escola/lista_escola.html", escolas=escolas)



@app.route("/listaescola/<int:id>")
def listar_escola(id):
    escola = escola_model.Escola.query.filter_by(id=id).first()  # Consulta todos os registros na tabela Nivel
    return render_template("escola/lista_escola_id.html",escola=escola)

@app.route("/editarescola/<int:id>",methods=["POST","GET"])
def editar_escola(id):

   
   escola = escola_model.Escola.query.filter_by(id=id).first() 
   # vamos agora criar nossa escola de formulário
   form = escola_form.EscolaForm(obj=escola)
   # verificar se todos os dados estão ok
   if form.validate_on_submit():
      nome = form.nome.data
      telefone = form.telefone.data
      try:
        escola.nome = nome
        escola.telefone = telefone
        db.session.commit()
        return redirect(url_for("listar_escolas"))
      except:
        print("a escola não foi editado")
         
   return render_template("escola/index.html",form=form,editar=True)

@app.route("/removerescola/<int:id>",methods=["POST","GET"])
def remover_escola(id):
     escola= escola_model.Escola.query.filter_by(id=id).first() 
     # vamos indicar que o usuário clicou no botão remover
     # importe request
     if request.method == "POST":
        try:
             db.session.delete(escola)
             db.session.commit()
             return redirect(url_for("listar_escolas"))
        except:
             print("erro ao deletar escola")
     return render_template("escola/remover_escola.html",escola=escola)