from flask import Blueprint, render_template, request, jsonify, send_file, flash, redirect, url_for
from flask_login import login_required, current_user
from models.regressor import model, data
from models.user import User
import plotly.express as px
import pandas as pd

bp = Blueprint('views', __name__)

@bp.route('/graficos')
@login_required
def graficos():
    media_notas_casa = data.groupby('Casa')[['DefesaContraArtes', 'Pocoes', 'Transfiguracao']].mean().reset_index()
    fig = px.bar(media_notas_casa, x='Casa', y=['DefesaContraArtes', 'Pocoes', 'Transfiguracao'],
                 title="Média de Notas por Casa", barmode='group', 
                 hover_name='Casa')  # Adiciona interatividade
    graph_html = fig.to_html(full_html=False)
    return render_template('graficos.html', graph_html=graph_html)

@bp.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Retrieve JSON data from POST request

    # Extract the input features
    defesa = data.get("DefesaContraArtes")
    pocoes = data.get("Pocoes")
    transfiguracao = data.get("Transfiguracao")

    # Create DataFrame for model input
    novas_notas = pd.DataFrame({
        "DefesaContraArtes": [defesa],
        "Pocoes": [pocoes],
        "Transfiguracao": [transfiguracao]
    })

    # Make prediction
    predicao = model.predict(novas_notas)
    
    # Return prediction result
    return jsonify({"predicao": float(predicao[0])})

@bp.route('/eda')
@login_required
def eda():
    # Estatísticas descritivas
    stats = data.describe().to_dict()
    
    # Gráfico de distribuição de notas
    fig = px.histogram(data, x='NotaFinal', title='Distribuição das Notas Finais')
    histogram_html = fig.to_html(full_html=False)

    return render_template('eda.html', stats=stats, histogram_html=histogram_html)

@bp.route('/export')
@login_required
def export():
    # Salva os dados em um arquivo CSV
    data.to_csv('notas_hogwarts.csv', index=False)
    return send_file('notas_hogwarts.csv', as_attachment=True)

@bp.route('/comparar', methods=['GET', 'POST'])
@login_required
def comparar():
    if request.method == 'POST':
        alunos = request.form.getlist('alunos')  # Pega os alunos selecionados
        dados_comparacao = data[data['Nome'].isin(alunos)]
        fig = px.bar(dados_comparacao, x='Nome', y=['DefesaContraArtes', 'Pocoes', 'Transfiguracao'],
                     title="Comparação de Notas entre Alunos", barmode='group')
        graph_html = fig.to_html(full_html=False)
        return render_template('comparar.html', graph_html=graph_html, alunos=alunos)

    # Passar todos os alunos disponíveis para a seleção
    alunos = data['Nome'].tolist()
    return render_template('comparar.html', alunos=alunos)
