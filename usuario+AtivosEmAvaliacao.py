import pandas as pd
import matplotlib.pyplot as plt

# Dados do portfólio - Kaggle: MovieLens 9000 Movies Dataset
# https://www.kaggle.com/datasets/akkefa/movielens-9000-movies-dataset

# Carregando os arquivos CSV
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")
tags = pd.read_csv("tags.csv")
links = pd.read_csv("links.csv")

# Descobrindo os 10 usuários que mais avaliaram filmes
user_activity = ratings['userId'].value_counts().reset_index()
user_activity.columns = ['userId', 'rating_count']
top_users = user_activity.head(10)

# Gráfico: Top 10 usuários mais ativos
plt.figure(figsize=(10, 5))
plt.barh(top_users['userId'].astype(str), top_users['rating_count'])
plt.title("Top 10 Usuários Mais Ativos (Quantidade de Avaliações)")
plt.xlabel("Quantidade de Avaliações")
plt.ylabel("ID do Usuário")
plt.tight_layout()
plt.show()
