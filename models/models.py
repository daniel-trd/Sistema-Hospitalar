from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class Paciente (db.Model):
    __tablename__ = "pacientes"

    id = db.Column (db.Integer, primary_key = True)
    nome = db.Column (db.String(200))
    endereco_rua = db.Column (db.String(100))
    endereco_bairro = db.Column (db.String(50))
    endereco_numero = db.Column (db.String(10))
    endereco_complemento = db.Column (db.String(200))
    endereco_cidade = db.Column (db.String(100))
    endereco_uf = db.Column (db.String(2))
    endereco_cep = db.Column (db.String(10))
    telefone = db.Column (db.String(15))
    email = db.Column (db.String(150))
    data_cadastro = db.Column (db.Date, default = date.today)
    status = db.Column (db.Boolean, default = True)

class Medico (db.Model):
    __tablename__ = "medico"

    id = db.Column (db.Integer, primary_key = True)
    nome = db.Column (db.String(200))
    crm = db.Column (db.String(15))
    especialidade = db.Column (db.String(200))
    telefone = db.Column (db.String(15))
    email = db.Column (db.String(150))
    data_cadastro = db.Column (db.Date)
    status = db.Column (db.Boolean)

class Exame (db.Model):
    __tablename__ = "exames"

    exame_id = db.Column (db.Integer, primary_key = True)
    paciente_id = db.Column (db.Integer, db.ForeignKey("pacientes.id"))
    medico_id = db.Column (db.Integer, db.ForeignKey("medico.id"))
    tipo_exame = db.Column (db.String(150))
    nome_exame = db.Column (db.String(200))
    descricao_exame = db.Column (db.String(200))
    status = db.Column (db.Boolean)