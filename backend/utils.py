from datetime import datetime, date

def calcular_contador_total(data_entrada_str, data_saida_str):
    fmt = "%Y-%m-%d"
    if not data_entrada_str:
        return 0
    data_entrada = datetime.strptime(data_entrada_str, fmt).date()
    data_saida = datetime.strptime(data_saida_str, fmt).date() if data_saida_str else date.today()
    return (data_saida - data_entrada).days
