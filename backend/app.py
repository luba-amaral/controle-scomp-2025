from flask import Flask, render_template, request, redirect, url_for
from backend.database     import init_db
from backend.models       import add_process, get_all_processes, update_process
from backend.export_excel import exportar_para_excel

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    processos = get_all_processes()
    return render_template('index.html', processos=processos)

@app.route('/add', methods=['POST'])
def add():
    dados = request.form.to_dict()
    add_process(dados)
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    dados = request.form.to_dict()
    update_process(id, dados)
    return redirect(url_for('index'))

@app.route('/export')
def export():
    exportar_para_excel()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
