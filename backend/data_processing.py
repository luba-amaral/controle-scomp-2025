import pandas as pd


def process_data(df):
    # cálculo automático para dias no setor
    df["dias fora do setor"] = (
        df["Data de Saída"] - df["Data de Entrada"]).dt.days

    df["Mês"] = df["Data de Entrada"].dt.month_name()  # cálculo do mes

    return df
