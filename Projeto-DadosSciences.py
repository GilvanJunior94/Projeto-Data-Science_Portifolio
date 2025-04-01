import pandas as pd
# Dados Pegos do para portifolio - do Kaggle movielens 9000 movies dataset . 
# https://www.kaggle.com/datasets/akkefa/movielens-9000-movies-dataset
# Carregando os arquivos CSV
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")
tags = pd.read_csv("tags.csv")
links = pd.read_csv("links.csv")

# Visualizando as primeiras linhas de cada arquivo
movies.head(), ratings.head(), tags.head(), links.head()

import matplotlib.pyplot as plt

# Calculando a média de avaliação e número de avaliações por filme
rating_summary = ratings.groupby('movieId').agg(
    avg_rating=('rating', 'mean'),
    rating_count=('rating', 'count')
).reset_index()

# Filtrando filmes com pelo menos 50 avaliações
filtered_ratings = rating_summary[rating_summary['rating_count'] >= 50]

# Pegando os top 10 filmes com maior média de avaliação
top_movies = filtered_ratings.sort_values(by='avg_rating', ascending=False).head(10)

# Juntando com os títulos dos filmes
top_movies = top_movies.merge(movies[['movieId', 'title']], on='movieId')

# Plotando o gráfico
plt.figure(figsize=(12, 6))
plt.barh(top_movies['title'], top_movies['avg_rating'])
plt.xlabel('Média de Avaliação')
plt.title('Top 10 Filmes com Maiores Médias de Avaliação (50+ avaliações)')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
