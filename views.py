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

@bp.route('/quadribol')
@login_required
def quadribol():
    # Dados fictícios de jogadores
    jogadores = [
        {'Nome': 'Harry Potter', 'Casa': 'Grifinória', 'Posicao': 'Apanhador', 'PartidasJogadas': 20, 'PontosMarcados': 1500},
        {'Nome': 'Draco Malfoy', 'Casa': 'Sonserina', 'Posicao': 'Apanhador', 'PartidasJogadas': 18, 'PontosMarcados': 1100},
        {'Nome': 'Cedric Diggory', 'Casa': 'Lufa-Lufa', 'Posicao': 'Artilheiro', 'PartidasJogadas': 22, 'PontosMarcados': 1350},
        {'Nome': 'Cho Chang', 'Casa': 'Corvinal', 'Posicao': 'Apanhadora', 'PartidasJogadas': 19, 'PontosMarcados': 1200},
        {'Nome': 'Angelina Johnson', 'Casa': 'Grifinória', 'Posicao': 'Artilheira', 'PartidasJogadas': 24, 'PontosMarcados': 1600}
    ]

    # Dados fictícios do campeonato
    partidas = [
        {'Time': 'Grifinória', 'Casa': 'Grifinória', 'Pontos': 450, 'Resultado': 'Vitória'},
        {'Time': 'Sonserina', 'Casa': 'Sonserina', 'Pontos': 320, 'Resultado': 'Vitória'},
        {'Time': 'Corvinal', 'Casa': 'Corvinal', 'Pontos': 380, 'Resultado': 'Vitória'},
        {'Time': 'Lufa-Lufa', 'Casa': 'Lufa-Lufa', 'Pontos': 280, 'Resultado': 'Derrota'},
        {'Time': 'Grifinória', 'Casa': 'Grifinória', 'Pontos': 500, 'Resultado': 'Vitória'},
        {'Time': 'Sonserina', 'Casa': 'Sonserina', 'Pontos': 400, 'Resultado': 'Vitória'},
        {'Time': 'Lufa-Lufa', 'Casa': 'Lufa-Lufa', 'Pontos': 450, 'Resultado': 'Vitória'}
    ]

    # Gráfico de barras (média de pontos por casa)
    media_por_casa = pd.DataFrame(jogadores).groupby('Casa')[['PontosMarcados']].mean().reset_index()
    fig_bar = px.bar(media_por_casa, x='Casa', y='PontosMarcados', title='Média de Pontos por Casa', color='Casa')
    graph_html = fig_bar.to_html(full_html=False)

    # Gráfico de dispersão de desempenho
    desempenho_df = pd.DataFrame(jogadores)
    fig_scatter = px.scatter(desempenho_df, x='PartidasJogadas', y='PontosMarcados', 
                             color='Casa', size='PontosMarcados', hover_name='Nome', 
                             title='Desempenho nas Partidas')
    scatter_html = fig_scatter.to_html(full_html=False)

    # Pontuação total por casa
    df_partidas = pd.DataFrame(partidas)
    pontuacao_por_casa = df_partidas.groupby('Casa')['Pontos'].sum().reset_index()
    fig_pontuacao = px.bar(pontuacao_por_casa, x='Casa', y='Pontos', 
                           title='Pontuação Total por Casa', color='Casa')
    pontuacao_html = fig_pontuacao.to_html(full_html=False)

    # Contagem de vitórias por time
    vitorias = (df_partidas[df_partidas['Resultado'] == 'Vitória']
                .groupby(['Time', 'Casa'])
                .size()
                .reset_index(name='Vitorias')
                .to_dict('records'))

    # Estatísticas gerais do campeonato
    total_partidas = len(partidas)
    total_pontos = df_partidas['Pontos'].sum()
    media_pontos = round(total_pontos / total_partidas, 2)

    return render_template('quadribol.html',
                           graph_html=graph_html,
                           jogadores=jogadores,
                           scatter_html=scatter_html,
                           pontuacao_html=pontuacao_html,
                           vitorias=vitorias,
                           total_partidas=total_partidas,
                           total_pontos=total_pontos,
                           media_pontos=media_pontos)


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
    fig_hist = px.histogram(data, x='NotaFinal', title='Distribuição das Notas Finais')

    # Boxplot para detectar outliers
    fig_box = px.box(data, y='NotaFinal', title='Boxplot das Notas Finais')
    
    # Gráfico de dispersão entre duas variáveis (exemplo: Defesa Contra Artes vs. Transfiguração)
    fig_scatter = px.scatter(data, x='DefesaContraArtes', y='Transfiguracao', 
                             title='Correlação entre Defesa Contra Artes e Transfiguração', 
                             color='Casa')

    # Filtrando apenas as colunas numéricas para calcular a correlação
    numeric_data = data.select_dtypes(include=['number'])

    # Estatísticas de correlação
    correlation_matrix = numeric_data.corr()

    # Convertendo a matriz de correlação para um formato amigável para exibição
    corr_html = correlation_matrix.to_html(classes='table table-striped')

    # Gerando gráficos
    histogram_html = fig_hist.to_html(full_html=False)
    boxplot_html = fig_box.to_html(full_html=False)
    scatter_html = fig_scatter.to_html(full_html=False)

    return render_template('eda.html', stats=stats, 
                           histogram_html=histogram_html, 
                           boxplot_html=boxplot_html, 
                           scatter_html=scatter_html, 
                           corr_html=corr_html)

@bp.route('/export')
@login_required
def export():
    # Salva os dados de notas dos alunos
    data.to_csv('notas_hogwarts.csv', index=False)

    # Dados fictícios de jogadores
    jogadores = [
        {'Nome': 'Harry Potter', 'Casa': 'Grifinória', 'Posicao': 'Apanhador', 'PartidasJogadas': 20, 'PontosMarcados': 1500},
        {'Nome': 'Draco Malfoy', 'Casa': 'Sonserina', 'Posicao': 'Apanhador', 'PartidasJogadas': 18, 'PontosMarcados': 1100},
        {'Nome': 'Cedric Diggory', 'Casa': 'Lufa-Lufa', 'Posicao': 'Artilheiro', 'PartidasJogadas': 22, 'PontosMarcados': 1350},
        {'Nome': 'Cho Chang', 'Casa': 'Corvinal', 'Posicao': 'Apanhadora', 'PartidasJogadas': 19, 'PontosMarcados': 1200},
        {'Nome': 'Angelina Johnson', 'Casa': 'Grifinória', 'Posicao': 'Artilheira', 'PartidasJogadas': 24, 'PontosMarcados': 1600}
    ]
    df_jogadores = pd.DataFrame(jogadores)
    df_jogadores.to_csv('jogadores_quadribol.csv', index=False)

    # Dados fictícios do campeonato
    partidas = [
        {'Time': 'Grifinória', 'Casa': 'Grifinória', 'Pontos': 450, 'Resultado': 'Vitória'},
        {'Time': 'Sonserina', 'Casa': 'Sonserina', 'Pontos': 320, 'Resultado': 'Vitória'},
        {'Time': 'Corvinal', 'Casa': 'Corvinal', 'Pontos': 380, 'Resultado': 'Vitória'},
        {'Time': 'Lufa-Lufa', 'Casa': 'Lufa-Lufa', 'Pontos': 280, 'Resultado': 'Derrota'},
        {'Time': 'Grifinória', 'Casa': 'Grifinória', 'Pontos': 500, 'Resultado': 'Vitória'},
        {'Time': 'Sonserina', 'Casa': 'Sonserina', 'Pontos': 400, 'Resultado': 'Vitória'},
        {'Time': 'Lufa-Lufa', 'Casa': 'Lufa-Lufa', 'Pontos': 450, 'Resultado': 'Vitória'}
    ]
    df_partidas = pd.DataFrame(partidas)
    df_partidas.to_csv('partidas_quadribol.csv', index=False)

    # Criação de um arquivo ZIP com todos os dados
    import zipfile
    with zipfile.ZipFile('dados_hogwarts.zip', 'w') as zf:
        zf.write('notas_hogwarts.csv')
        zf.write('jogadores_quadribol.csv')
        zf.write('partidas_quadribol.csv')

    return send_file('dados_hogwarts.zip', as_attachment=True)

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
