import pandas as pd
from sklearn.linear_model import LinearRegression

# Dados fictícios de alunos de Hogwarts
data = pd.DataFrame({
    'Nome': ['Harry Potter', 'Hermione Granger', 'Draco Malfoy', 'Luna Lovegood', 'Ron Weasley'],
    'Casa': ['Grifinória', 'Grifinória', 'Sonserina', 'Corvinal', 'Grifinória'],
    'DefesaContraArtes': [8.5, 10.0, 7.0, 9.0, 6.5],
    'Pocoes': [6.0, 10.0, 8.0, 7.5, 6.0],
    'Transfiguracao': [7.5, 9.5, 8.5, 7.0, 6.0],
    'NotaFinal': [8.0, 9.8, 7.5, 8.2, 6.3]
})

# Modelo de Regressão Linear
X = data[['DefesaContraArtes', 'Pocoes', 'Transfiguracao']]
y = data['NotaFinal']
model = LinearRegression()
model.fit(X, y)
