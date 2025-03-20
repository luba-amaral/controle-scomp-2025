from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, IntegerField, FloatField, BooleanField
from wtforms.validators import DataRequired


class ProcessoForm(FlaskForm):
    numero_processo = StringField(
        'Número do Processo', validators=[DataRequired()])
    unidade_demandante = SelectField('Unidade Demandante', choices=[('DIVLS', 'DIVLS'), ('OPMES', 'OPMES'), (
        'SFA', 'SFA'), ('SLA', 'SLA'), ('SEC', 'SEC'), ('DHH', 'DHH')], validators=[DataRequired()])
    modalidade_compra = StringField('Modalidade de Compra')
    objeto = StringField('Objeto')
    qtd_itens = IntegerField('Quantidade de Itens')
    cotador = StringField('Cotador')
    criacao_proc = DateField('Data de Criação do Processo', format='%Y-%m-%d')
    numero_pesquisa = StringField('Número da Pesquisa')
    finalizacao_pesquisa = DateField(
        'Data de Finalização da Pesquisa', format='%Y-%m-%d')
    status = SelectField('Status', choices=[('Finalizado', 'Finalizado'), ('Em Pesquisa no Mercado', 'Em Pesquisa no Mercado'), (
        'Despachado', 'Despachado'), ('Cancelado', 'Cancelado')], validators=[DataRequired()])
    data_saida = DateField(
        'Data de Saída', format='%Y-%m-%d', validators=[DataRequired()])
    observacao = StringField('Observação')
    mes = SelectField('Mês', choices=[('Janeiro', 'Janeiro'), ('Fevereiro', 'Fevereiro'), ('Março', 'Março'), ('Abril', 'Abril'), ('Maio', 'Maio'), ('Junho', 'Junho'), (
        'Julho', 'Julho'), ('Agosto', 'Agosto'), ('Setembro', 'Setembro'), ('Outubro', 'Outubro'), ('Novembro', 'Novembro'), ('Dezembro', 'Dezembro')], validators=[DataRequired()])
    peso_processos = FloatField('Peso dos Processos')

    # caixa de seleção unidade demandante
    divls = BooleanField('DIVLS')
    opmes = BooleanField('OPMES')
    sfa = BooleanField('SFA')
    sla = BooleanField('SLA')
    sec = BooleanField('SEC')
    dhh = BooleanField('DHH')
