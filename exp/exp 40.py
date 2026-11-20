
# Recommendation System using Collaborative Filtering

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Create sample user-item rating dataset
data = {
    'Movie1': [5, 4, 0, 0, 2],
    'Movie2': [4, 5, 0, 0, 1],
    'Movie3': [0, 0, 5, 4, 0],
    'Movie4': [0, 0, 4, 5, 0],
    'Movie5': [1, 2, 0, 0, 5]
}

# Create DataFrame
df = pd.DataFrame(
    data,
    index=['User1', 'User2', 'User3', 'User4', 'User5']
)

print("User-Item Rating Matrix:")
print(df)

# Calculate user similarity
similarity = cosine_similarity(df)

similarity_df = pd.DataFrame(
    similarity,
    index=df.index,
    columns=df.index
)

print("\nUser Similarity Matrix:")
print(similarity_df.round(2))

# Recommendation function
def recommend_movies(user):

    # Get similarity scores for selected user
    scores = similarity_df.loc[user]

    # Find similar users
    similar_users = scores.drop(user).sort_values(
        ascending=False
    )

    # Select the most similar user
    best_user = similar_users.index[0]

    # Find movies not watched by the selected user
    unwatched = df.loc[user][df.loc[user] == 0].index

    # Recommend movies based on similar user's ratings
    recommendations = df.loc[best_user, unwatched]

    recommendations = recommendations[
        recommendations > 0
    ].sort_values(ascending=False)

    print("\nRecommendations for", user, ":")
    
    if len(recommendations) == 0:
        print("No recommendations available.")
    else:
        for movie, rating in recommendations.items():
            print(movie, "- Rating:", rating)

# Generate recommendation
recommend_movies('User1')
