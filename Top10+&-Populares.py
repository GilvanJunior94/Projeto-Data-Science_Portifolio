import pandas as pd
import matplotlib.pyplot as plt

# Dados do portfólio - Kaggle: MovieLens 9000 Movies Dataset
# https://www.kaggle.com/datasets/akkefa/movielens-9000-movies-dataset

# Carregando os arquivos CSV
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")
tags = pd.read_csv("tags.csv")
links = pd.read_csv("links.csv")

# Contando o número de avaliações por filme
popularity = ratings.groupby('movieId').size().reset_index(name='rating_count')

# Juntando com os títulos
popularity = popularity.merge(movies[['movieId', 'title']], on='movieId')

# Filmes mais populares (com mais avaliações)
most_popular = popularity.sort_values(by='rating_count', ascending=False).head(10)

# Filmes menos populares (com pelo menos 1 avaliação)
least_popular = popularity.sort_values(by='rating_count', ascending=True).head(10)

# Separando os 10 filmes mais e menos populares (ordenando pro gráfico ficar bonito)
top_10_popular = most_popular.sort_values(by='rating_count', ascending=True)
bottom_10_popular = least_popular.sort_values(by='rating_count', ascending=False)

# Gráfico: Filmes mais populares
plt.figure(figsize=(12, 5))
plt.barh(top_10_popular['title'], top_10_popular['rating_count'])
plt.title("Top 10 Filmes Mais Populares (Mais Avaliados)")
plt.xlabel("Número de Avaliações")
plt.tight_layout()
plt.show()

# Gráfico: Filmes menos populares
plt.figure(figsize=(12, 5))
plt.barh(bottom_10_popular['title'], bottom_10_popular['rating_count'])
plt.title("Top 10 Filmes Menos Populares (Menos Avaliados)")
plt.xlabel("Número de Avaliações")
plt.tight_layout()
plt.show()
