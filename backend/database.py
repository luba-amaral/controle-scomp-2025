import sqlite3

DB_PATH = 'Dados_2025.db'

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS processos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data_entrada TEXT,
        numero_processo TEXT,
        unidade_demandante TEXT,
        modalidade_compra TEXT,
        objeto TEXT,
        qtd_itens INTEGER,
        cotador TEXT,
        criacao_processo TEXT,
        numero_pesquisa TEXT,
        finalizacao_pesquisa TEXT,
        hoje1 TEXT,
        status_processo TEXT,
        data_saida TEXT,
        hoje2 TEXT,
        contador_total INTEGER,
        dias_fora_setor INTEGER,
        observacao TEXT,
        mes TEXT,
        peso_processos INTEGER
    )''')
    conn.commit()
    conn.close()
