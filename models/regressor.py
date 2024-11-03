import pandas as pd
from sklearn.linear_model import LinearRegression

# Novo conjunto de dados com 10 alunos, incluindo Leonardo Cesar
data = pd.DataFrame({
    'Nome': [
        'Harry Potter', 'Hermione Granger', 'Draco Malfoy', 'Luna Lovegood', 
        'Ron Weasley', 'Ginny Weasley', 'Neville Longbottom', 'Cho Chang', 
        'Cedric Diggory', 'Leonardo Cesar'
    ],
    'Casa': [
        'Grifinória', 'Grifinória', 'Sonserina', 'Corvinal', 'Grifinória', 
        'Grifinória', 'Grifinória', 'Corvinal', 'Lufa-Lufa', 'Sonserina'
    ],
    'DefesaContraArtes': [8.5, 10.0, 7.0, 9.0, 6.5, 8.0, 7.0, 8.0, 8.5, 10.0],
    'Pocoes': [6.0, 10.0, 8.0, 7.5, 6.0, 7.5, 6.5, 7.5, 9.0, 10.0],
    'Transfiguracao': [7.5, 9.5, 8.5, 7.0, 6.0, 8.0, 7.0, 7.0, 8.0, 10.0],
    'NotaFinal': [8.0, 9.8, 7.5, 8.2, 6.3, 7.8, 6.5, 7.5, 8.5, 9.9]  
})

X = data[['DefesaContraArtes', 'Pocoes', 'Transfiguracao']]
y = data['NotaFinal']
model = LinearRegression()
model.fit(X, y)
