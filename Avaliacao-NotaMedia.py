import pandas as pd
# Dados Pegos do para portifolio - do Kaggle movielens 9000 movies dataset . 
# https://www.kaggle.com/datasets/akkefa/movielens-9000-movies-dataset
# Carregando os arquivos CSV
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")
tags = pd.read_csv("tags.csv")
links = pd.read_csv("links.csv")

import matplotlib.pyplot as plt

# Calculando a média de avaliação por filme
avg_rating_per_film = ratings.groupby('movieId')['rating'].mean()

# Gráfico da distribuição da média de avaliação por filme
plt.figure(figsize=(10, 5))
plt.hist(avg_rating_per_film, bins=20, edgecolor='black', color='orange')
plt.title("Distribuição da Média de Avaliação por Filme")
plt.xlabel("Média de Avaliação")
plt.ylabel("Quantidade de Filmes")
plt.tight_layout()
plt.show()
