import numpy as np
from datetime import datetime


def calcular_contador_total(data_entrada, data_saida=None):
    data_final = data_saida if data_saida else datetime.now().date()
    contador_total = np.busday_count(data_entrada.date(), data_final)
    return contador_total


def calcular_dias_fora_setor(data_saida, data_retorno):
    if data_saida and data_retorno:
        return np.busday_count(data_saida.date(), data_retorno.date())
    return 0


def calcular_observacao(status, data_saida):
    if status == "Finalizado" and data_saida:
        return f"Processo finalizado em {data_saida.strftime('%d/%m/%Y')}"
    return "Em andamento"
