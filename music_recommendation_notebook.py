# Music Recommendation Engine - Complete Implementation
# =====================================================

# Cell 1: Import Required Libraries
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD
from scipy.sparse import csr_matrix
import warnings
warnings.filterwarnings('ignore')

print("Libraries imported successfully!")

# Cell 2: Load and Explore the Dataset
# Load the training data
train_df = pd.read_csv('train.csv')
recommendations_df = pd.read_csv('recommendations.csv')

print("Dataset Information:")
print(f"Training data shape: {train_df.shape}")
print(f"Recommendations data shape: {recommendations_df.shape}")
print("\nTraining data columns:", train_df.columns.tolist())
print("\nFirst few rows of training data:")
print(train_df.head())

print("\nRecommendations data:")
print(recommendations_df.head())

# Cell 3: Data Preprocessing and Exploration
# Check for missing values
print("Missing values in training data:")
print(train_df.isnull().sum())

# Basic statistics
print("\nDataset Statistics:")
print(f"Total unique users: {train_df['user_id'].nunique()}")
print(f"Total unique songs: {train_df['song_id'].nunique()}")
print(f"Total unique artists: {train_df['artist_name'].nunique()}")
print(f"Date range: {train_df['year'].min()} - {train_df['year'].max()}")

# Check listen count distribution
print(f"\nListen count statistics:")
print(train_df['listen_count'].describe())

# Cell 4: Exploratory Data Analysis
# Analyze user behavior
user_stats = train_df.groupby('user_id').agg({
    'song_id': 'count',
    'listen_count': 'sum'
}).rename(columns={'song_id': 'songs_listened', 'listen_count': 'total_listens'})

print("User behavior statistics:")
print(user_stats.describe())

# Analyze song popularity
song_stats = train_df.groupby('song_id').agg({
    'user_id': 'count',
    'listen_count': 'sum'
}).rename(columns={'user_id': 'unique_listeners', 'listen_count': 'total_listens'})

print("\nSong popularity statistics:")
print(song_stats.describe())

# Cell 5: Create User-Song Matrix for Collaborative Filtering
def create_user_song_matrix(df):
    """Create a user-song interaction matrix"""
    # Use listen_count as the interaction strength
    user_song_matrix = df.pivot_table(
        index='user_id', 
        columns='song_id', 
        values='listen_count', 
        fill_value=0
    )
    return user_song_matrix

user_song_matrix = create_user_song_matrix(train_df)
print(f"User-Song matrix shape: {user_song_matrix.shape}")
print(f"Matrix sparsity: {(user_song_matrix == 0).sum().sum() / (user_song_matrix.shape[0] * user_song_matrix.shape[1]):.4f}")

# Cell 6: Content-Based Filtering Features
def create_content_features(df):
    """Create content-based features for songs"""
    # Combine artist and year information
    df['content_features'] = df['artist_name'].astype(str) + ' ' + df['year'].astype(str)
    
    # Create TF-IDF vectors for content features
    tfidf = TfidfVectorizer(max_features=1000, stop_words='english')
    content_matrix = tfidf.fit_transform(df['content_features'].fillna(''))
    
    return content_matrix, tfidf

# Create content features
unique_songs = train_df.drop_duplicates('song_id')[['song_id', 'artist_name', 'year', 'title']]
content_matrix, tfidf_vectorizer = create_content_features(unique_songs)
print(f"Content feature matrix shape: {content_matrix.shape}")

# Cell 7: Popularity-Based Recommendations
def get_popular_songs(df, n_recommendations=10):
    """Get most popular songs based on listen count and unique listeners"""
    song_popularity = df.groupby('song_id').agg({
        'user_id': 'nunique',
        'listen_count': 'sum'
    }).rename(columns={'user_id': 'unique_listeners', 'listen_count': 'total_listens'})
    
    # Create a popularity score combining both metrics
    song_popularity['popularity_score'] = (
        song_popularity['unique_listeners'] * 0.6 + 
        song_popularity['total_listens'] * 0.4
    )
    
    return song_popularity.nlargest(n_recommendations, 'popularity_score').index.tolist()

popular_songs = get_popular_songs(train_df, 20)
print(f"Top popular songs: {popular_songs[:10]}")

# Cell 8: Collaborative Filtering with Matrix Factorization
def matrix_factorization_recommendations(user_song_matrix, target_users, n_recommendations=10):
    """Use SVD for collaborative filtering"""
    # Convert to sparse matrix for efficiency
    sparse_matrix = csr_matrix(user_song_matrix.values)
    
    # Apply SVD
    svd = TruncatedSVD(n_components=50, random_state=42)
    user_factors = svd.fit_transform(sparse_matrix)
    song_factors = svd.components_.T
    
    # Reconstruct the matrix
    reconstructed = np.dot(user_factors, song_factors.T)
    reconstructed_df = pd.DataFrame(
        reconstructed, 
        index=user_song_matrix.index, 
        columns=user_song_matrix.columns
    )
    
    recommendations = {}
    for user_id in target_users:
        if user_id in reconstructed_df.index:
            user_row = reconstructed_df.loc[user_id]
            # Get songs the user hasn't listened to
            listened_songs = set(user_song_matrix.loc[user_id][user_song_matrix.loc[user_id] > 0].index)
            # Get top recommendations excluding already listened songs
            user_recommendations = user_row.drop(listened_songs).nlargest(n_recommendations).index.tolist()
            recommendations[user_id] = user_recommendations
    
    return recommendations

# Cell 9: Content-Based Filtering
def content_based_recommendations(df, target_users, content_matrix, unique_songs, n_recommendations=10):
    """Generate content-based recommendations"""
    # Create song similarity matrix
    song_similarity = cosine_similarity(content_matrix)
    song_similarity_df = pd.DataFrame(
        song_similarity,
        index=unique_songs['song_id'],
        columns=unique_songs['song_id']
    )
    
    recommendations = {}
    for user_id in target_users:
        user_songs = df[df['user_id'] == user_id]['song_id'].tolist()
        
        if user_songs:
            # Find similar songs to user's listening history
            similar_songs_scores = {}
            for song_id in user_songs:
                if song_id in song_similarity_df.index:
                    similar_songs = song_similarity_df.loc[song_id].drop(song_id)
                    for similar_song, score in similar_songs.items():
                        if similar_song not in user_songs:  # Exclude already listened songs
                            similar_songs_scores[similar_song] = similar_songs_scores.get(similar_song, 0) + score
            
            # Get top recommendations
            if similar_songs_scores:
                recommended_songs = sorted(similar_songs_scores.items(), key=lambda x: x[1], reverse=True)
                recommendations[user_id] = [song for song, score in recommended_songs[:n_recommendations]]
            else:
                recommendations[user_id] = popular_songs[:n_recommendations]
        else:
            # New user - recommend popular songs
            recommendations[user_id] = popular_songs[:n_recommendations]
    
    return recommendations

# Cell 10: Hybrid Recommendation System
def hybrid_recommendations(df, user_song_matrix, target_users, content_matrix, unique_songs, n_recommendations=10):
    """Combine collaborative and content-based filtering"""
    
    # Get collaborative filtering recommendations
    collab_recs = matrix_factorization_recommendations(user_song_matrix, target_users, n_recommendations)
    
    # Get content-based recommendations
    content_recs = content_based_recommendations(df, target_users, content_matrix, unique_songs, n_recommendations)
    
    # Combine recommendations
    hybrid_recs = {}
    for user_id in target_users:
        user_recs = []
        
        # Get collaborative recommendations
        if user_id in collab_recs:
            user_recs.extend(collab_recs[user_id][:n_recommendations//2])
        
        # Get content-based recommendations
        if user_id in content_recs:
            content_user_recs = [song for song in content_recs[user_id] if song not in user_recs]
            user_recs.extend(content_user_recs[:n_recommendations//2])
        
        # Fill remaining slots with popular songs if needed
        if len(user_recs) < n_recommendations:
            remaining_slots = n_recommendations - len(user_recs)
            popular_additions = [song for song in popular_songs if song not in user_recs]
            user_recs.extend(popular_additions[:remaining_slots])
        
        hybrid_recs[user_id] = user_recs[:n_recommendations]
    
    return hybrid_recs

# Cell 11: Generate Recommendations for Target Users
# Get target users from recommendations.csv
target_users = recommendations_df['user_id'].tolist() if 'user_id' in recommendations_df.columns else recommendations_df.iloc[:, 0].tolist()

print(f"Generating recommendations for {len(target_users)} users...")

# Generate hybrid recommendations
final_recommendations = hybrid_recommendations(
    train_df, 
    user_song_matrix, 
    target_users, 
    content_matrix, 
    unique_songs, 
    n_recommendations=10
)

print("Recommendations generated successfully!")

# Cell 12: Format Output for Submission
def format_recommendations_for_submission(recommendations, target_users):
    """Format recommendations according to the required output format"""
    formatted_recommendations = []
    
    for user_id in target_users:
        if user_id in recommendations and recommendations[user_id]:
            # Format: user_id,song_id1,song_id2,...,song_id10
            recommendation_line = [user_id] + recommendations[user_id]
            formatted_recommendations.append(','.join(map(str, recommendation_line)))
        else:
            # Fallback to popular songs if no recommendations
            recommendation_line = [user_id] + popular_songs[:10]
            formatted_recommendations.append(','.join(map(str, recommendation_line)))
    
    return formatted_recommendations

# Format the recommendations
formatted_output = format_recommendations_for_submission(final_recommendations, target_users)

# Create the output DataFrame
output_df = pd.DataFrame(formatted_output, columns=['recommendations'])
print("Sample recommendations:")
for i, rec in enumerate(formatted_output[:5]):
    print(f"User {i+1}: {rec[:100]}...")

# Cell 13: Save Recommendations to File
# Save to recommendations.csv (overwrite the original file)
output_df.to_csv('recommendations.csv', index=False, header=False)
print("Recommendations saved to 'recommendations.csv'")

# Verify the output
verification_df = pd.read_csv('recommendations.csv', header=None)
print(f"Verification - Output file shape: {verification_df.shape}")
print("First few lines of output:")
print(verification_df.head())

# Cell 14: Evaluation Metrics (Optional - for understanding model performance)
def calculate_recommendation_coverage(recommendations, all_songs):
    """Calculate how many unique songs are being recommended"""
    recommended_songs = set()
    for user_recs in recommendations.values():
        recommended_songs.update(user_recs)
    
    coverage = len(recommended_songs) / len(all_songs)
    return coverage

def calculate_personalization(recommendations):
    """Calculate how personalized the recommendations are"""
    all_user_recs = list(recommendations.values())
    if len(all_user_recs) < 2:
        return 0
    
    similarities = []
    for i in range(len(all_user_recs)):
        for j in range(i+1, len(all_user_recs)):
            intersection = len(set(all_user_recs[i]) & set(all_user_recs[j]))
            union = len(set(all_user_recs[i]) | set(all_user_recs[j]))
            if union > 0:
                jaccard_sim = intersection / union
                similarities.append(jaccard_sim)
    
    # Personalization is 1 - average similarity
    return 1 - (sum(similarities) / len(similarities) if similarities else 0)

# Calculate metrics
all_songs = train_df['song_id'].unique()
coverage = calculate_recommendation_coverage(final_recommendations, all_songs)
personalization = calculate_personalization(final_recommendations)

print(f"\nRecommendation System Metrics:")
print(f"Coverage: {coverage:.4f} ({len(set().union(*final_recommendations.values()))} unique songs recommended)")
print(f"Personalization: {personalization:.4f}")
print(f"Total users with recommendations: {len(final_recommendations)}")

# Cell 15: Summary and Next Steps
print("\n" + "="*60)
print("RECOMMENDATION ENGINE SUMMARY")
print("="*60)
print(f"✓ Processed {train_df.shape[0]} training records")
print(f"✓ Generated recommendations for {len(target_users)} target users")
print(f"✓ Used hybrid approach combining collaborative and content-based filtering")
print(f"✓ Each user has up to 10 song recommendations")
print(f"✓ Recommendations saved to 'recommendations.csv'")
print(f"✓ Model coverage: {coverage:.2%}")
print(f"✓ Model personalization: {personalization:.2%}")
print("\nThe recommendation engine is ready for submission!")
print("="*60)

# Cell 16: Validation Check
def validate_recommendations():
    """Validate that recommendations meet the requirements"""
    df = pd.read_csv('recommendations.csv', header=None)
    
    issues = []
    
    for idx, row in df.iterrows():
        line = row[0]
        parts = line.split(',')
        
        if len(parts) < 2:
            issues.append(f"Row {idx}: No recommendations provided")
            continue
            
        user_id = parts[0]
        song_recommendations = parts[1:]
        
        # Check if user has recommendations for songs they already listened to
        if user_id in train_df['user_id'].values:
            user_listened_songs = set(train_df[train_df['user_id'] == user_id]['song_id'].values)
            recommended_songs = set(song_recommendations)
            
            overlap = user_listened_songs.intersection(recommended_songs)
            if overlap:
                issues.append(f"User {user_id}: Recommending already listened songs: {list(overlap)[:3]}")
        
        # Check recommendation count
        if len(song_recommendations) > 10:
            issues.append(f"User {user_id}: More than 10 recommendations ({len(song_recommendations)})")
        elif len(song_recommendations) == 0:
            issues.append(f"User {user_id}: No recommendations provided")
    
    if issues:
        print("Validation Issues Found:")
        for issue in issues[:10]:  # Show first 10 issues
            print(f"- {issue}")
        if len(issues) > 10:
            print(f"... and {len(issues) - 10} more issues")
    else:
        print("✓ All validations passed! Recommendations file is ready for submission.")
    
    return len(issues) == 0

# Run validation
validation_passed = validate_recommendations()

if validation_passed:
    print("\n🎉 SUCCESS: Your recommendation engine is complete and ready!")
else:
    print("\n⚠️ Please fix the validation issues before submitting.")
