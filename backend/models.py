from backend.database import get_connection
from backend.utils import calcular_contador_total
from datetime import datetime, date

def add_process(data):
    fmt = "%Y-%m-%d"
    data_entrada = data['data_entrada']
    data_saida   = data.get('data_saida')
    contador     = calcular_contador_total(data_entrada, data_saida)
    hoje = date.today().isoformat()
    observacao = f"Saiu em {datetime.strptime(data_saida, fmt).strftime('%d/%m/%Y')}" if data_saida else ""
    dias_fora = int(data.get('dias_fora_setor') or 0)

    conn  = get_connection()
    cur   = conn.cursor()
    cur.execute('''
    INSERT INTO processos (
      data_entrada, numero_processo, unidade_demandante, modalidade_compra,
      objeto, qtd_itens, cotador, criacao_processo, numero_pesquisa,
      finalizacao_pesquisa, hoje1, status_processo, data_saida, hoje2,
      contador_total, dias_fora_setor, observacao, mes, peso_processos
    ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    ''', (
      data['data_entrada'], data['numero_processo'], data['unidade_demandante'], data['modalidade_compra'],
      data['objeto'], int(data['qtd_itens'] or 0), data['cotador'], data.get('criacao_proceso'),
      data.get('numero_pesquisa'), data.get('finalizacao_pesquisa'), hoje,
      data['status_processo'], data_saida, hoje,
      contador, dias_fora, observacao, data['mes'], int(data.get('peso_processos') or 0)
    ))
    conn.commit()
    conn.close()

def get_all_processes():
    conn = get_connection()
    cur  = conn.cursor()
    cur.execute("SELECT * FROM processos")
    rows = cur.fetchall()
    conn.close()
    return rows

def update_process(id, data):
    fmt = "%Y-%m-%d"
    data_entrada = data['data_entrada']
    data_saida   = data.get('data_saida')
    contador     = calcular_contador_total(data_entrada, data_saida)
    hoje = date.today().isoformat()
    observacao = f"Saiu em {datetime.strptime(data_saida, fmt).strftime('%d/%m/%Y')}" if data_saida else ""
    dias_fora = int(data.get('dias_fora_setor') or 0)

    conn = get_connection()
    cur  = conn.cursor()
    cur.execute('''
    UPDATE processos SET
      data_entrada=?, numero_processo=?, unidade_demandante=?, modalidade_compra=?,
      objeto=?, qtd_itens=?, cotador=?, criacao_processo=?, numero_pesquisa=?,
      finalizacao_pesquisa=?, hoje1=?, status_processo=?, data_saida=?, hoje2=?,
      contador_total=?, dias_fora_setor=?, observacao=?, mes=?, peso_processos=?
    WHERE id=?
    ''', (
      data['data_entrada'], data['numero_processo'], data['unidade_demandante'], data['modalidade_compra'],
      data['objeto'], int(data['qtd_itens'] or 0), data['cotador'], data.get('criacao_proceso'),
      data.get('numero_pesquisa'), data.get('finalizacao_pesquisa'), hoje,
      data['status_processo'], data_saida, hoje,
      contador, dias_fora, observacao, data['mes'], int(data.get('peso_processos') or 0),
      id
    ))
    conn.commit()
    conn.close()
