# Projeto Hogwarts

Este é um projeto desenvolvido em Python utilizando o framework Flask, que simula um sistema de previsão de notas finais para alunos da escola de magia de Hogwarts. O projeto inclui gráficos interativos utilizando a biblioteca Plotly e um modelo de regressão linear para fazer previsões com base em notas de disciplinas específicas.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

/projeto_hogwarts ├── app.py ├── models │ ├── regressor.py │ └── user.py ├── views.py ├── templates │ ├── base.html │ ├── index.html │ ├── graficos.html │ ├── eda.html │ ├── comparar.html │ └── quadribol.html # Nova página para estatísticas de quadribol └── static ├── styles.css └── scripts.js


### Descrição dos Arquivos

- **app.py**: Arquivo principal onde o aplicativo Flask é configurado e as rotas são registradas.
- **models/regressor.py**: Contém o modelo de regressão linear e os dados fictícios dos alunos.
- **models/user.py**: Define o modelo de usuário para o sistema de login.
- **views.py**: Define as rotas que utilizam o Blueprint para gerenciar gráficos, previsões e análise exploratória de dados.
- **templates/**: Contém os templates HTML utilizados para renderizar as páginas.
  - **base.html**: Template base com cabeçalho e rodapé reutilizáveis.
  - **index.html**: Página inicial onde os usuários podem inserir dados para previsão.
  - **graficos.html**: Exibe os gráficos das médias de notas por casa.
  - **eda.html**: Apresenta estatísticas descritivas e gráficos de distribuição de notas.
  - **comparar.html**: Permite comparar as notas de diferentes alunos.
  - **quadribol.html**: Exibe estatísticas detalhadas sobre o campeonato de Quadribol, com gráficos interativos sobre desempenho de jogadores, vitórias por time e pontuação total por casa.
- **static/**: Contém arquivos estáticos como CSS e JavaScript.
  - **styles.css**: Estilos para a interface do usuário.
  - **scripts.js**: Script para gerenciar a lógica de previsão.

## Instalação

Para executar o projeto, siga os passos abaixo:

1. **Clone o repositório:**
   git clone https://github.com/Leonardocsp/projeto_hogwarts.git
   cd projeto_hogwarts
Crie e ative um ambiente virtual (recomendado):

No Linux/Mac:

python -m venv venv
source venv/bin/activate
No Windows:

python -m venv venv
venv\Scripts\activate
Instale as dependências: As bibliotecas necessárias para o funcionamento do projeto são listadas abaixo. Você pode instalá-las usando o pip:
pip install Flask pandas scikit-learn plotly flask-login flask-sqlalchemy
Bibliotecas necessárias:

Flask: Framework para criação da aplicação web.
pandas: Biblioteca para manipulação de dados.
scikit-learn: Biblioteca para machine learning, utilizada para o modelo de regressão linear.
plotly: Biblioteca para criação de gráficos interativos.
flask-login: Para gerenciamento de sessões e autenticação de usuários.
flask-sqlalchemy: Para integração com banco de dados SQL.
Execução
Após instalar as dependências, para iniciar o servidor Flask, execute o seguinte comando no terminal:

python app.py


O aplicativo estará disponível em http://127.0.0.1:5000/.

Funcionalidades

Previsão de Notas Finais: Os usuários podem inserir suas notas nas disciplinas "Defesa Contra as Artes das Trevas", "Poções" e "Transfiguração" para prever sua nota final.

Gráficos Interativos: Visualize as médias das notas por casa em gráficos de barras interativos.

Estatísticas de Quadribol: Uma nova página com gráficos e estatísticas detalhadas sobre o campeonato de Quadribol, incluindo:
Média de pontos por casa.
Desempenho dos jogadores nas partidas.
Pontuação total por casa e contagem de vitórias dos times.