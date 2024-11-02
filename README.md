# Projeto Hogwarts

Este é um projeto desenvolvido em Python utilizando o framework Flask, que simula um sistema de previsão de notas finais para alunos da escola de magia de Hogwarts. O projeto inclui gráficos interativos utilizando a biblioteca Plotly e um modelo de regressão linear para fazer previsões com base em notas de disciplinas específicas.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

/projeto_hogwarts ├── app.py ├── models │ └── regressor.py ├── templates │ ├── base.html │ ├── index.html │ └── graficos.html └── static └── styles.css


### Descrição dos Arquivos

- `app.py`: Arquivo principal onde o aplicativo Flask é configurado e as rotas são registradas.
- `models/regressor.py`: Contém o modelo de regressão linear e os dados fictícios dos alunos.
- `views.py`: Define as rotas que utilizam o Blueprint para gerenciar gráficos e previsões.
- `templates/`: Contém os templates HTML utilizados para renderizar as páginas.
  - `base.html`: Template base com cabeçalho e rodapé reutilizáveis.
  - `index.html`: Página inicial onde os usuários podem inserir dados para previsão.
  - `graficos.html`: Exibe os gráficos das médias de notas por casa.
- `static/`: Contém arquivos estáticos como CSS e JavaScript.
  - `styles.css`: Estilos para a interface do usuário.
  - `scripts.js`: Script para gerenciar a lógica de previsão.

## Instalação

Para executar o projeto, siga os passos abaixo:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Leonardocsp/projeto_hogwarts.git
   cd projeto_hogwarts
Instale as dependências: É recomendado criar um ambiente virtual. Você pode fazer isso com o venv:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Em seguida, instale as bibliotecas necessárias:

pip install Flask pandas scikit-learn plotly
Execução
Para iniciar o servidor Flask, execute o seguinte comando no terminal:

python app.py
O aplicativo estará disponível em http://127.0.0.1:5000/.

Funcionalidades
Previsão de Notas Finais: Os usuários podem inserir suas notas em "Defesa Contra as Artes das Trevas", "Poções" e "Transfiguração" para prever sua nota final.
Gráficos Interativos: Visualize as médias das notas por casa em gráficos de barras interativos.
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

Licença
Este projeto é de código aberto e pode ser usado livremente. Por favor, verifique o arquivo LICENSE para mais detalhes.

### Dicas para Uso

1. **Adapte o README**: Você pode personalizar as seções conforme a necessidade do seu projeto, adicionando informações relevantes como instruções específicas para o ambiente de desenvolvimento ou detalhes sobre as dependências.
2. **Exemplos de Uso**: Considere adicionar uma seção de exemplos de uso, mostrando como interagir com a interface ou exemplos de dados de entrada e saída para a previsão.
3. **Screenshots**: Se você tiver capturas de tela do aplicativo em execução, é uma boa prática incluí-las para dar uma visão visual do que os usuários podem esperar.

Esse modelo serve como um bom ponto de partida para documentar seu projeto. Se precisar de mais ajustes ou adicionar mais seções, é só avisar!





