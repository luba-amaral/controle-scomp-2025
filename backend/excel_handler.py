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

        # vai calcular os dados de entrada e saida de acoro com mes e ano
    def calcular_entradas_saidas(self, df, mes, ano):
        inicio_mes = datetime(ano, mes, 1)
        fim_mes = datetime(
            ano, mes + 1, 1) if mes < 12 else datetime(ano + 1, 1, 1)

        dados_mes = df[(df["Data de Entrada"] >= inicio_mes)
                       & (df["Data de Entrada"] < fim_mes)]
        entradas = dados_mes[dados_mes["Status do processo"].str.contains(
            "SEI*", na=False)]
        saidas = dados_mes[(dados_mes["Status do Processo"].str.contains(
            "SEI*", na=False)) & (dados_mes["Data de Saída"].notna())]

        return {
            "entradas": len(entradas),
            "saídas": len(saidas)
        }

    def update_fechamento_sheet(self, df):
        # preserva formilas e formatação
        with pd.ExcelWriter(self.planilha_path, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
            # atualiza a aba fechamento, caso exista
            if "Fechamento" in pd.ExcelFile(self.planilha_path). sheet_names:
                fechamento_df = pd.read_excel(
                    self.planilha_path, sheet_name="Fechamento")

                for mes in range(1, 13):
                    resultados = self.calcular_entradas_saidas(df, mes, 2025)
                    fechamento_df.loc[mes - 1,
                                      "Entradas"] = resultados["entradas"]
                    fechamento_df.loc[mes - 1, "Saídas"] = resultados["saidas"]

                fechamento_df.to_excel(
                    writer, sheet_name="Fechamento", index=False)
            else:
                print("Erro: Aba 'Fechamento' não encontrada")
