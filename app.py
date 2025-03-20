from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Configuração da aplicação
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Dados_2025.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definição do modelo (tabela)


class Processo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero_processo = db.Column(db.String(100), nullable=False)
    unidade_demandante = db.Column(db.String(50), nullable=False)
    modalidade_compra = db.Column(db.String(50), nullable=False)
    objeto = db.Column(db.Text, nullable=False)
    qtd_itens = db.Column(db.Integer, nullable=False)
    cotador = db.Column(db.String(100), nullable=False)
    data_entrada = db.Column(db.Date, nullable=False)
    data_criacao_processo = db.Column(db.Date, nullable=False)
    numero_pesquisa = db.Column(db.String(50))
    data_finalizacao_pesquisa = db.Column(db.Date)
    data_saida = db.Column(db.Date)
    status_processo = db.Column(db.String(50), nullable=False)
    dias_fora_setor = db.Column(db.Integer)
    contador_total = db.Column(db.Integer)

    def __repr__(self):
        return f'<Processo {self.numero_processo}>'


with app.app_context():
    db.create_all()

# Rota para renderizar o formulário na página inicial


@app.route('/')
def index():
    return render_template('index.html')

# Rota para adicionar um novo processo


@app.route('/processos', methods=['POST'])
def adicionar_processo():
    data = request.form.to_dict()  # Obtém os dados do formulário HTML

    novo_processo = Processo(
        numero_processo=data['numero_processo'],
        unidade_demandante=data['unidade_demandante'],
        modalidade_compra=data['modalidade_compra'],
        objeto=data['objeto'],
        qtd_itens=int(data['qtd_itens']),
        cotador=data['cotador'],
        data_entrada=datetime.strptime(data['data_entrada'], '%Y-%m-%d'),
        data_criacao_processo=datetime.strptime(
            data['data_criacao_processo'], '%Y-%m-%d'),
        numero_pesquisa=data['numero_pesquisa'],
        data_finalizacao_pesquisa=datetime.strptime(
            data['data_finalizacao_pesquisa'], '%Y-%m-%d') if data.get('data_finalizacao_pesquisa') else None,
        status_processo=data['status_processo']
    )

    # Adiciona e faz o commit no banco
    db.session.add(novo_processo)
    db.session.commit()

    return jsonify({'message': 'Processo adicionado com sucesso!'}), 201


if __name__ == '__main__':
    app.run(debug=True)
