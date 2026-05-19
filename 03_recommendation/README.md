# Movie Recommendation System

A content-based movie recommender using Cosine Similarity on the MovieLens dataset.

## Features
- Loads 9,742 movies and 100,836 ratings from MovieLens
- One-hot encodes 19 genres
- User selects preferred genres interactively
- Returns Top 10 recommended movies with similarity scores
- Visualizes results with bar charts

## How to Run
```
jupyter notebook recommendation_system.ipynb
```

Make sure movies.csv and ratings.csv are in the same folder.

## Tech Stack
- Python
- scikit-learn
- pandas
- matplotlib
