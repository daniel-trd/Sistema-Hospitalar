from flask import Blueprint, render_template, request, redirect, url_for
from controllers.controllers import (
    listar_pacientes,
    cadastro_paciente,
    excluir_paciente,
    listar_exames,
    excluir_exame,
    registrar_exame,
    listar_medicos,
    cadastro_medico,
    excluir_medico,
    listar_agendamentos,
    cadastro_agendamento,
    excluir_agendamento,
)
from models import models as m
from models.models import Paciente, Exame

bp = Blueprint("main", __name__)

@bp.route("/")
def home():
    return redirect(url_for("main.home"))

# ===== Rota Pacientes =====

@bp.route("/pacientes")
def pacientes():
    pacien = listar_pacientes()
    return render_template("pacientes.html", pacientes=pacien)

@bp.route("/pacientes/new", methods=["POST"])
def new_patient():

    cadastro_paciente(
        request.form.get("nome"),
        request.form.get("endereco_rua"),
        request.form.get("endereco_bairro"),
        request.form.get("endereco_numero"),
        request.form.get("endereco_complemento"),
        request.form.get("endereco_cidade"),
        request.form.get("endereco_uf"),
        request.form.get("endereco_cep"),
        request.form.get("telefone"),
        request.form.get("email")
    )
    return redirect(url_for("main.pacientes"))

@bp.post("/pacientes/excluir/<int:id>")
def excluir_paciente_route(id):
    excluir_paciente(id)
    return redirect("/pacientes")

# ===== Rota Exames =====

@bp.route("/exame")
def exames():
    le = listar_exames()
    return render_template("exame.html", exames=le)

@bp.route("/exame/new", methods=["POST"])
def novo_exame():
    registrar_exame(
        request.form.get("paciente_id"),
        request.form.get("medico_id"),
        request.form.get("tipo_exame"),
        request.form.get("nome_exame"),
        request.form.get("descricao_exame")
    )
    return redirect(url_for("main.exames"))

@bp.post("/exame/excluir/<int:id>")
def excluir_exame_route(id):
    excluir_exame(id)
    return redirect("/exame")

# ===== Rota Medicos =====

@bp.route("/medicos")
def medicos():
    lista = listar_medicos()
    return render_template("medicos.html", medicos=lista)

@bp.route("/medicos/new", methods=["POST"])
def novo_medico():
    cadastro_medico(
        request.form.get("nome"),
        request.form.get("crm"),
        request.form.get("especialidade"),
        request.form.get("telefone"),
        request.form.get("email")
    )
    return redirect("/medicos")

@bp.post("/medicos/excluir/<int:id>")
def excluir_medico_route(id):
    excluir_medico(id)
    return redirect("/medicos")



# ===== Rota Dashboard =====

@bp.route("/dashboard")
def dashboard():

    qnt_paciente = Paciente.query.count()
    qnt_exame = Exame.query.count()

    agendamento_model = None
    for candidate in ("Agendamento", "Agendamentos", "Appointment", "Appointments", "Consulta", "Consultas"):
        agendamento_model = getattr(m, candidate, None)
        if agendamento_model:
            break

    try:
        qtd_agendamentos = agendamento_model.query.count() if agendamento_model else 0
    
    except Exception:
        qtd_agendamentos = 0

    return render_template(
        "dashboard.html",
        qtd_agendamentos = qtd_agendamentos,
        qnt_exame = qnt_exame,
        qnt_paciente = qnt_paciente
    )



# ===== Rota Agendamento =====

@bp.route("/agendamentos")
def agendamento():   # endpoint = main.agendamento
    ags = listar_agendamentos()
    return render_template("agendamento.html", agendamentos=ags)

@bp.route("/agendamentos/new", methods=["POST"])
def novo_agendamento():
    # pegar do form/request.json
    paciente = request.form.get("paciente") or request.json.get("paciente")
    medico = request.form.get("medico") or request.json.get("medico")
    start = request.form.get("start") or request.json.get("start")
    end = request.form.get("end") or request.json.get("end")
    tipo = request.form.get("tipo") or request.json.get("tipo")
    descricao = request.form.get("descricao") or request.json.get("descricao")

    cadastro_agendamento(paciente, medico, start, end, tipo, descricao)
    return redirect(url_for("main.agendamento"))

@bp.post("/agendamentos/excluir/<int:id>")
def excluir_agendamento_route(id):
    excluir_agendamento(id)
    return redirect(url_for("main.agendamento"))

@bp.route("/agendamentos/editar/<int:id>", methods=["GET","POST"])
def editar_agendamento_route(id):
    if request.method == "GET":
        # renderiza form com dados
        ag = Agendamento.query.get(id)
        return render_template("edit_agendamento.html", ag=ag)
    else:
        dados = {
            "paciente_id": request.form.get("paciente"),
            "medico_id": request.form.get("medico"),
            "start": request.form.get("start"),
            "end": request.form.get("end"),
            "tipo": request.form.get("tipo"),
            "descricao": request.form.get("descricao"),
        }
        editar_agendamento(id, **dados)
        return redirect(url_for("main.agendamento"))
