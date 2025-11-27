from flask import Blueprint, render_template, request, redirect, url_for
from controllers.controllers import (
    listar_pacientes,
    cadastro_paciente,
    excluir_paciente,
    editar_paciente,
    listar_exames,
    excluir_exame,
    editar_exame,
    registrar_exame,
    listar_medicos,
    cadastro_medico,
    excluir_medico,
    editar_medico,
)

bp = Blueprint("main", __name__)

@bp.route("/")
def home():
    return redirect(url_for("main.pacientes"))

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


@bp.route("/exame")
def lista_ex():
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
    return redirect(url_for("main.lista_ex"))

@bp.post("/exame/excluir/<int:id>")
def excluir_exame_route(id):
    excluir_exame(id)
    return redirect("/exame")

@bp.get("/exame/editar/<int:id>")
def editar_exame_form(id):
    pass

@bp.post("/exame/editar/<int:id>")
def editar_exame_route(id):
    dados = {
        "nome_exame": request.form.get("exame"),
        "tipo_exame": request.form.get("tipo"),
        "descricao_exame": request.form.get("descricao_exame"),
    }
    editar_exame(id, **dados)
    return redirect(url_for("main.novo_exame"))



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
