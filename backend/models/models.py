from flask_sqlalchemy import SQLAlchemy
from datetime import date
from app import db

db = SQLAlchemy()


class Processo(db.Model):
    __tablename__ = 'processos'

    id = db.Column(db.Integer, primary_key=True)
    data_entrada = db.Column(db.Date, nullable=False)
    numero_processo = db.Column(db.String(100), nullable=False)
    unidade_demandante = db.Column(db.String(50), nullable=False)
    modalidade_compra = db.Column(db.String(50))
    objeto = db.Column(db.Text, nullable=False)
    qtd_itens = db.Column(db.Integer, nullable=False)
    cotador = db.Column(db.String(100), nullable=False)
    criacao_proc = db.Column(db.Date, nullable=False)
    numero_pesquisa = db.Column(db.String(50))
    finalizacao_pesquisa = db.Column(db.Date)
    data_saida = db.Column(db.Date)
    status = db.Column(db.String(50))
    contador_total = db.Column(db.Integer)
    dias_fora_setor = db.Column(db.Integer)
    observacao = db.Column(db.String(255))
    #mes = db.Column(db.String(50))
    peso_processos = db.Column(db.Float)

    # Coluna de caixa de seleção
    divls = db.Column(db.Boolean, default=False)
    opmes = db.Column(db.Boolean, default=False)
    sfa = db.Column(db.Boolean, default=False)
    sla = db.Column(db.Boolean, default=False)
    sec = db.Column(db.Boolean, default=False)
    dhh = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Processo {self.numero_processo}>'

def init_db():
    db.create_all()
