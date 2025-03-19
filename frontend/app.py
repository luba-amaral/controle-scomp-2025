from flask import Flask, render_template, request, redirect, url_for
from backend.excel_handler import ExcelProcessor
from datetime import datetime
import pandas as pd

app = Flask(__name__)

planilha_path = "2025 - PLANILHA CONTROLE SCOMP-2025.xlsx"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/visualizar')
def visualizar():
    processor = ExcelProcessor(planilha_path)
    df = processor.ler_dados()
    return render_template("visualizar.html", dados=df.to_dict('records'))


@app.route('/salvar', methods=['POST'])
def salvar():
    dados = {
        "Data de Entrada": request.form.get("data_entrada"),
        "N° do Processo": request.form.get("numero_processo"),
        "Unidade Demandante": request.form.get("unidade_demandante"),
        "Modalidade de Compra": request.form.get("modalidade_compra"),
        "Objeto": request.form.get("objeto"),
        "Qtd. De itens": request.form.get("quantidade_itens"),
        "Cotador": request.form.get("cotador"),
        "Criação Proc./Pesquisa": request.form.get("criacao_processo"),
        "Nº Pesquisa": request.form.get("numero_pesquisa"),
        "Finalização da Pesquisa": request.form.get("finalizacao_pesquisa"),
        "Hoje": request.form.get("hoje"),
        "Status do Processo": request.form.get("status_processo"),
        "Data de Saída": request.form.get("data_saida"),
        "dias fora do setor": request.form.get("dias_fora_setor"),
        "Mês": request.form.get("mes"),
        "Peso dos Processos": request.form.get("peso_processos"),
    }

    # converte datas para formato datetime
    dados["Data de Entrada"] = pd.to_datetime(
        dados["Data de Entrada"], format="%Y-%m-%d")
    dados["Criação Proc./Pesquisa"] = pd.to_datetime(
        dados["Criação Proc./Pesquisa"], format="%Y-%m-%d")
    dados["Finalização da Pesquisa"] = pd.to_datetime(
        dados["Finalização da Pesquisa"], format="%Y-%m-%d")
    dados["Hoje"] = pd.to_datetime(dados["Hoje"], format="%Y-%m-%d")
    dados["Data de Saída"] = pd.to_datetime(
        dados["Data de Saída"], format="%Y-%m-%d") if dados["Data de Saída"] else None

    # cálculos automáticos
    dados["Contador Total"] = (datetime.now() - dados["Data de Entrada"]).days
    dados["Observação"] = f"Saiu em {dados['Data de Saída'].strftime('%d/%m/%Y')}" if dados["Data de Saída"] else ""
    dados["Mês"] = dados["Data de Entrada"].strftime('%B')

    # contador
    if dados["Data de Saída"]:
        contador_total = (dados["Data de Saída"] -
                          dados["Data de Entrada"]).days

    else:
        contador_total = (datetime.now() - dados["Data de Entrada"]).days

    contador_total -= int(dados["dias fora do setor"])
    dados["Contador Total"] = contador_total

    # dias fora do setor
    if dados["Data de Saída"]:
        diferenca = dados["Data de Saída"] - dados["Data de Entrada"]
        dados["dias fora do setor"] = diferenca.days

    else:
        dados["dias fora do setor"] = 0

    # Converte para DataFrame
    df = pd.DataFrame([dados])

    # Atualiza a planilha
    processor = ExcelProcessor(planilha_path)
    processor.salvar_dados(df)
    processor.update_fechamento_sheet(df)

    return redirect(url_for('visualizar'))


if __name__ == "__main__":
    app.run(debug=True)
