#importando o flask
from flask import Flask
#importando o SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,upgrade
from flask_wtf import CSRFProtect
from flask_jwt_extended import JWTManager
#criando o aplicativo
app = Flask(__name__)
#puxando o arquivo config.py
app.config.from_object('config')
#criando um objeto db da classe SQLAlchemy
db = SQLAlchemy(app)
#criar uma variável migrate e passar a instância da aplicação e do db
migrate = Migrate(app,db)
jwt = JWTManager(app)
csrf = CSRFProtect(app)
csrf.init_app(app)



#FIXME:model
from app.models import nivel_model
from app.models import usuario_model
from app.models import escola_model
from app.models import curso_model

#FIXME:view
from .views import nivel_view
from .views import usuario_view
from .views import escola_view
from .views import curso_view
from .views import aulajinja_view
from .views import login_view














