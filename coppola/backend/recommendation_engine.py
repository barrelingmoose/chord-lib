import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df):
    df['genres'] = df['genres'].fillna('')
    df['title'] = df['title'].fillna('')
    df['combined'] = df['genres'] + ' ' + df['title']
    return df

def compute_similarity(df):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df['combined'])
    similarity_matrix = cosine_similarity(tfidf_matrix)
    return similarity_matrix

def recommend_movies(df, similarity_matrix, movie_id, num_recommendations=5):
    indices = pd.Series(df.index, index=df['movieId']).drop_duplicates()
    idx = indices[movie_id]
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices]

if __name__ == "__main__":
    filepath = '../database/ml-latest-small/movies.csv'
    df = load_data(filepath)
    df = preprocess_data(df)
    similarity_matrix = compute_similarity(df)
    movie_id = 4
    recommended_movies = recommend_movies(df, similarity_matrix, movie_id)
    print(recommended_movies)