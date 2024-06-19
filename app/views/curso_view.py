from app import app
from flask import render_template
from app.models.escola_model import Escola
from app.forms.curso_form import CursoForm


@app.route("/cadcurso",methods=["POST","GET"])
def cadastrar_curso():
    form_curso = CursoForm()
    # Carregar os níveis do banco de dados
    escolas = Escola.query.all()
    # Formatar os níveis para o formato necessário para o campo de seleção
    escolas_choices = [(escola.id, escola.nome) for escola in escolas]
    form_curso.escola_id.choices = escolas_choices
    if form_curso.validate_on_submit():
        pass
    
    return render_template("curso/index.html",form_curso=form_curso)


