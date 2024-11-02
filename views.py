from flask import Blueprint, render_template, request, jsonify
from models.regressor import model, data
import plotly.express as px

bp = Blueprint('views', __name__)

@bp.route('/graficos')
def graficos():
    media_notas_casa = data.groupby('Casa')[['DefesaContraArtes', 'Pocoes', 'Transfiguracao']].mean().reset_index()
    fig = px.bar(media_notas_casa, x='Casa', y=['DefesaContraArtes', 'Pocoes', 'Transfiguracao'],
                 title="Média de Notas por Casa", barmode='group')
    graph_html = fig.to_html(full_html=False)
    return render_template('graficos.html', graph_html=graph_html)

@bp.route('/predict', methods=['POST'])
def predict():
    try:
        dados = request.json
        input_data = [[dados['DefesaContraArtes'], dados['Pocoes'], dados['Transfiguracao']]]
        predicao = model.predict(input_data)[0]
        return jsonify({'predicao': predicao})
    except (KeyError, TypeError, ValueError):
        return jsonify({'error': 'Dados inválidos, verifique as entradas.'}), 400
