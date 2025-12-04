from models.models import db, Paciente, Medico, Exame, Users, Agendamento

#CRUD PACIENTE
def listar_pacientes():
    
    return Paciente.query.all()

def cadastro_paciente (nome, endereco_rua, endereco_bairro, endereco_numero, endereco_complemento, endereco_cidade, endereco_uf, endereco_cep, telefone, email):
    
    new_paciente = Paciente(nome = nome, endereco_rua = endereco_rua, endereco_bairro = endereco_bairro, endereco_numero = endereco_numero, endereco_complemento = endereco_complemento, endereco_cidade = endereco_cidade, endereco_uf = endereco_uf, endereco_cep = endereco_cep, telefone = telefone, email = email)
    db.session.add(new_paciente)
    db.session.commit()
    
def excluir_paciente(id):

    delete_paciente = Paciente.query.get(id)
    if delete_paciente:
        db.session.delete(delete_paciente)
        db.session.commit()
        return True
    return False


# CRUD EXAME
def listar_exames():

    return Exame.query.all()

def registrar_exame(paciente_id, medico_id, tipo_exame, nome_exame, descricao_exame):

    new_exame = Exame (paciente_id = paciente_id, medico_id = medico_id, tipo_exame = tipo_exame, nome_exame = nome_exame, descricao_exame = descricao_exame)
    db.session.add(new_exame)
    db.session.commit()

def excluir_exame(id):
    
    delete_exame = Exame.query.get(id)
    if delete_exame:
        db.session.delete(delete_exame)
        db.session.commit()
        return True
    return False


#CRUD MEDICOS
def listar_medicos():

    return Medico.query.all()

def cadastro_medico(nome, crm, especialidade, telefone, email):

    new_medico = Medico(nome = nome, crm = crm, especialidade = especialidade, telefone = telefone, email = email)
    db.session.add(new_medico)
    db.session.commit()

def excluir_medico(id):

    delete_medico = Medico.query.get(id)
    if delete_medico:
        db.session.delete(delete_medico)
        db.session.commit()
        return True
    return False


#CRUD AGENDAMENTO

def listar_agendamentos():
    return Agendamento.query.all()

# CADASTRAR agendamento (recebe valores já validados pela rota)
def cadastro_agendamento(paciente_id, medico_id, tipo="consulta", descricao=None):
    # converte datetimes (expects ISO or 'YYYY-MM-DDTHH:MM' strings)

    # opcional: validar paciente/medico existem
    if paciente_id and not Paciente.query.get(int(paciente_id)):
        raise ValueError("paciente não existe")
    if medico_id and not Medico.query.get(int(medico_id)):
        raise ValueError("medico não existe")

    ag = Agendamento(
        paciente_id = int(paciente_id),
        medico_id = int(medico_id) if medico_id else None,
        tipo = tipo
    )
    db.session.add(ag)
    db.session.commit()
    return ag

# EXCLUIR por id
def excluir_agendamento(id):
    ag = Agendamento.query.get(id)
    if not ag:
        return False
    db.session.delete(ag)
    db.session.commit()
    return True
