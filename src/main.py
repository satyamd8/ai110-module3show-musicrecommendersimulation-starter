"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # User Profile 1: From comments (typical, hiphop and r&b)
    user_profile_1 = {
        "favorite_genres": ["hiphop", "r&b"],
        "disliked_genres": ["country"],
        "favorite_moods": ["chill", "intense"],
        "disliked_moods": ["dramatic"],
        "target_energy_range": (0.3, 0.6),
        "target_tempo_range": (80, 160),
        "target_valence": 0.4,
        "target_danceability": 0.6,
        "target_acousticness": 0.2,
        "favorite_artists": ["Paris Texas", "Frank Ocean"]
    }

    # User Profile 2: Random typical user profile
    user_profile_2 = {
        "favorite_genres": ["pop", "edm"],
        "disliked_genres": ["country"],
        "favorite_moods": ["happy", "energetic"],
        "disliked_moods": ["sad"],
        "target_energy_range": (0.7, 1.0),
        "target_tempo_range": (100, 140),
        "target_valence": 0.8,
        "target_danceability": 0.8,
        "target_acousticness": 0.2,
        "favorite_artists": ["The Weeknd", "Ed Sheeran"]
    }

    # User Profile 3: Edge case - likes everything (should produce high scores for most songs)
    user_profile_3 = {
        "favorite_genres": ["pop", "rock", "lofi", "jazz", "edm", "grunge", "reggaeton", "classic rock", "country", "r&b", "indie pop", "alternative", "trap", "ambient", "soul", "synthpop", "synthwave"],
        "disliked_genres": [],
        "favorite_moods": ["happy", "chill", "intense", "relaxed", "moody", "focused", "energetic", "sad", "romantic", "rebellious", "festive", "dramatic", "emotional", "melancholic", "nostalgic", "edgy", "hype"],
        "disliked_moods": [],
        "target_energy_range": (0.0, 1.0),
        "target_tempo_range": (0, 300),
        "target_valence": 0.5,
        "target_danceability": 0.5,
        "target_acousticness": 0.5,
        "favorite_artists": ["LoRoom", "Frank Ocean", "The Weeknd", "Adele", "Ed Sheeran", "Nirvana", "Luis Fonsi", "Queen", "Lady Gaga & Bradley Cooper", "Rex Orange County", "Paris Texas", "Playboi Carti"]
    }

    # Choose which profile to test:
    user_prefs = user_profile_3

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for rec in recommendations:
        song, score, explanation = rec
        print(f"{song['title']}\n  Score: {score:.2f}")
        reasons = [r.strip() for r in explanation.split(';') if r.strip()]
        for reason in reasons:
            print(f"  - {reason}")
        print()


if __name__ == "__main__":
    main()
