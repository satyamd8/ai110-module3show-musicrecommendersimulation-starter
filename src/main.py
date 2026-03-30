"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs

example:
user_profile = {
   "favorite_genres": ["hiphop", "lofi"],
   "disliked_genres": ["rock"],
   "favorite_moods": ["chill"],
   "disliked_moods": ["intense"],
   "target_energy_range": (0.3, 0.6),
   "target_tempo_range": (60, 100),
   "target_valence": 0.4,
   "target_danceability": 0.6,
   "target_acousticness": 0.2,
   "favorite_artists": ["LoRoom", "Frank Ocean"]
}
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {
        "favorite_genres": ["pop", "lofi"],
        "disliked_genres": ["rock"],
        "favorite_moods": ["happy", "chill"],
        "disliked_moods": ["intense"],
        "target_energy_range": (0.6, 0.9),
        "target_tempo_range": (80, 130),
        "target_valence": 0.7,
        "target_danceability": 0.7,
        "target_acousticness": 0.3,
        "favorite_artists": [],
    }

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
