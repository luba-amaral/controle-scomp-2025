from backend.database import db

class Processo(db.Model):
    __tablename__ = 'processos'

    id = db.Column(db.Integer, primary_key=True)
    data_entrada = db.Column(db.Date)
    numero_processo = db.Column(db.String)
    unidade_demandante = db.Column(db.String)
    modalidade_compra = db.Column(db.String)
    objeto = db.Column(db.String)
    qtd_itens = db.Column(db.Integer)
    cotador = db.Column(db.String)
    criacao_processo = db.Column(db.Date)
    numero_pesquisa = db.Column(db.String)
    finalizacao_pesquisa = db.Column(db.Date)
    hoje1 = db.Column(db.Date)
    status_processo = db.Column(db.String)
    data_saida = db.Column(db.Date)
    hoje2 = db.Column(db.Date)
    contador_total = db.Column(db.Integer)
    dias_fora_setor = db.Column(db.Integer)
    observacao = db.Column(db.String)
    mes = db.Column(db.String)
    peso_processos = db.Column(db.Float)
