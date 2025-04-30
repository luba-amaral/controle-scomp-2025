import pandas as pd
from backend.database import get_connection

def exportar_para_excel(caminho_saida="relatorio_processos.xlsx"):
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM processos", conn)
    df.to_excel(caminho_saida, index=False)
    conn.close()
    print(f"Exportado para {caminho_saida}")
