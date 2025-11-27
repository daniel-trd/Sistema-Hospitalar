from models.models import db, Paciente, Medico, Exame

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

def editar_paciente(id, **dados):

    edit_paciente = Paciente.query.get(id)
    if not edit_paciente:
        return None
    
    for campo, valor in dados.items():
        setattr(edit_paciente, campo, valor)

    db.session.commit()
    return edit_paciente

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

def editar_exame(id, **dados):
    
    edit_exame = Exame.query.get(id)
    if not edit_exame:
        return None
    
    for campo, valor in dados.items():
        setattr(edit_exame, campo, valor)

    db.session.commit()
    return edit_exame

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

def editar_medico(id, **dados):
    edit_medico = Medico.query.get(id)
    if not edit_medico:
        return None
    
    for campo, valor in dados.items():
        setattr(edit_medico, campo, valor)

    db.session.commit()
    return edit_medico