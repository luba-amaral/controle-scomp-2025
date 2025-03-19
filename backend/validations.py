import pandas as pd


def validate_dates(df):
    date_columns = ['Data de Entrada',
                    'Criação Proc./Pesquisa', 'Finalização da Pesquisa']
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce', format='%d/%m/%Y')
    return df
