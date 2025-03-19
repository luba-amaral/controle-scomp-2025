import pandas as pd
from datetime import datetime


class ExcelProcessor:
    def __init__(self, planilha_path):
        self.planilha_path = planilha_path
        
        # le os dados da aba dados
    def ler_dados(self):
        return pd.read_excel(self.planilha_path, sheet_name="Dados 2025")

    def salvar_dados(self, df):
        with pd.ExcelWriter(self.planilha_path, engine='openpyxl', mode="a", if_sheet_exists="replace") as writer:
            df.to_excel(writer, sheet_name="Dados 2025", index=False)

    def calcular_entradas_saidas(self, df, mes, ano):

        

        self.ws_fechamento.unmerge_cells()

        self.ws_fechamento.delete_rows(1, self.ws_fechamento.max_row)

        self.ws_fechamento['A1'] = "Analista"
        self.ws_fechamento['B1'] = "Finalizados"
        self.ws_fechamento['C1'] = "Cancelados"

        analistas = df.groupby('Cotador')[
            'Status do Processo'].value_counts().unstack()
        for idx, (analista, row) in enumerate(analistas.iterrows(), start=2):
            self.ws_fechamento[f'A{idx}'] = analista
            self.ws_fechamento[f'B{idx}'] = row.get('Finalizado', 0)
            self.ws_fechamento[f'C{idx}'] = row.get('Cancelado', 0)

    def ler_fechamento(self):

        return pd.read_excel(self.planilha_path, sheet_name="Fechamento")

    def add_data_validations(self):

        dv_unidade = DataValidation(
            type="list", formula1='"DIVLS,OPMES,SFA,SLA,SEC,DHH"', allow_blank=True)
        self.ws_dados.add_data_validation(dv_unidade)
        dv_unidade.add("C2:C1048576")

        dv_status = DataValidation(
            type="list", formula1='"Finalizado,Em pesquisa no mercado,Despachado,Cancelado"', allow_blank=True)
        self.ws_dados.add_data_validation(dv_status)
        dv_status.add("L2:L1048576")

    def save(self):

        self.wb.save(self.planilha_path)
