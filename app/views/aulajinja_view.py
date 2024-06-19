from app import app
from flask import render_template
from app.forms.aulajinja_form import AulaJinjaForm
@app.route("/aulajinja",methods=["POST","GET"])
def mostrar_variavel():
    aulajinja_form  = AulaJinjaForm()
    x = aulajinja_form.x.data 
    if aulajinja_form.validate_on_submit():
       pass
    return render_template("aulajinja/index.html", teste=x)
 

