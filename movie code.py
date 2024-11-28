
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Expanded dataset
data = {
    'title': [
        'Inception', 'The Matrix', 'Avengers: Endgame', 'Interstellar', 'The Dark Knight',
        'Titanic', 'The Shawshank Redemption', 'Pulp Fiction', 'Forrest Gump', 'The Godfather',
        'Jurassic Park', 'The Lion King', 'Frozen', 'Toy Story', 'Shrek',
        'Iron Man', 'Black Panther', 'Spider-Man: No Way Home', 'The Notebook', 'La La Land'
    ],
    'genres': [
        'Action Sci-Fi', 'Action Sci-Fi', 'Action Adventure', 'Sci-Fi Drama', 'Action Crime',
        'Romance Drama', 'Drama Crime', 'Crime Drama', 'Drama Romance', 'Crime Drama',
        'Sci-Fi Adventure', 'Animation Drama', 'Animation Musical', 'Animation Comedy', 'Animation Comedy',
        'Action Sci-Fi', 'Action Adventure', 'Action Adventure', 'Romance Drama', 'Romance Musical'
    ],
    'description': [
        'A thief who steals corporate secrets through dream-sharing technology.',
        'A hacker discovers the truth about his reality and his role in the war against its controllers.',
        'Superheroes come together to defeat a powerful foe threatening the universe.',
        'A team of explorers travel through a wormhole in space to ensure humanity’s survival.',
        'A vigilante defends his city while facing a cunning criminal mastermind.',
        'A romance blossoms aboard the ill-fated Titanic ship.',
        'Two imprisoned men bond over years, finding solace and redemption.',
        'The lives of two mob hitmen, a boxer, and others intertwine in violent stories.',
        'A slow-witted but kind man witnesses historical events while longing for his childhood love.',
        'The patriarch of an organized crime dynasty transfers control to his reluctant son.',
        'A theme park full of cloned dinosaurs becomes dangerous when the systems fail.',
        'A lion prince flees his kingdom but returns to take his rightful place.',
        'A fearless princess and her sister embark on a journey to break an icy curse.',
        'A cowboy doll and a spaceman action figure compete for the affection of their owner.',
        'An ogre and a donkey rescue a princess while discovering the meaning of friendship.',
        'A billionaire builds a suit of armor to fight evil and protect the world.',
        'A king of Wakanda fights to protect his people and legacy.',
        'Spider-Man teams up with other Spider-Men to fix the multiverse.',
        'A young couple struggles with love and life over the years.',
        'A jazz musician and an actress pursue their dreams in Los Angeles while falling in love.'
    ]
}

# Convert dataset to DataFrame
movies_df = pd.DataFrame(data)

# Combine genres and description for content-based filtering
movies_df['content'] = movies_df['genres'] + " " + movies_df['description']

# Use TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies_df['content'])

# Calculate cosine similarity between all movies
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get movie recommendations
def recommend_movies(movie_title, cosine_sim=cosine_sim):
    if movie_title not in movies_df['title'].values:
        return f"Sorry, we couldn't find the movie '{movie_title}' in our database."
    
    # Get the index of the movie
    idx = movies_df[movies_df['title'] == movie_title].index[0]
    
    # Compute similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort the movies based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]  # Top 5 similar movies
    
    # Get movie indices
    movie_indices = [i[0] for i in sim_scores]
    
    # Prepare recommendations
    recommendations = []
    for i in movie_indices:
        movie_title = movies_df.iloc[i]['title']
        shared_genres = movies_df.iloc[i]['genres']
        description = movies_df.iloc[i]['description']
        recommendations.append({
            "title": movie_title,
            "shared_genres": shared_genres,
            "description": description
        })
    
    return recommendations

# Interactive system
def interactive_recommender():
    print("Welcome to the Movie Recommendation System!")
    print("Here are some sample movies in our database:")
    print(movies_df['title'].tolist())
    print("\nWhich movie do you like?")
    user_input = input("Enter the movie title: ")
    
    print("\nFetching recommendations...")
    recommendations = recommend_movies(user_input)
    
    if isinstance(recommendations, str):
        print(recommendations)
    else:
        print("\nWe recommend these movies based on your choice:")
        for rec in recommendations:
            print(f"Movie: {rec['title']}")
            print(f"  - Shared Genres: {rec['shared_genres']}")
            print(f"  - Description: {rec['description']}\n")

# Run the interactive system
interactive_recommender()
