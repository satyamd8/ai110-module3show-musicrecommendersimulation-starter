from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genres: List[str]
    disliked_genres: List[str]
    favorite_moods: List[str]
    disliked_moods: List[str]
    target_energy_range: Tuple[float, float]
    target_tempo_range: Tuple[float, float]
    target_valence: float
    target_danceability: float
    target_acousticness: float
    favorite_artists: List[str]

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file as a list of dictionaries."""
    import csv
    songs = []
    numerical_fields = {
        "id": int,
        "energy": float,
        "tempo_bpm": float,
        "valence": float,
        "danceability": float,
        "acousticness": float
    }
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            song = {}
            for key, value in row.items():
                if key in numerical_fields:
                    try:
                        song[key] = numerical_fields[key](value)
                    except Exception:
                        song[key] = None
                else:
                    song[key] = value
            songs.append(song)
    print(f"loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, str]:
    """Score a song for a user and return (score, explanation)."""
    score = 0.0
    explanation = []

    # Helper for safe access and type conversion
    def get_str(song, key):
        val = song.get(key, "")
        return str(val).strip().lower()
    def get_float(song, key):
        try:
            return float(song.get(key, 0))
        except Exception:
            return 0.0

    # Genre
    genre = get_str(song, "genre")
    if genre in [g.lower() for g in user_prefs.get("favorite_genres", [])]:
        score += 3
        explanation.append(f"+3 genre match: {genre}")
    elif genre in [g.lower() for g in user_prefs.get("disliked_genres", [])]:
        score -= 2
        explanation.append(f"-2 disliked genre: {genre}")

    # Mood
    mood = get_str(song, "mood")
    if mood in [m.lower() for m in user_prefs.get("favorite_moods", [])]:
        score += 2
        explanation.append(f"+2 mood match: {mood}")
    elif mood in [m.lower() for m in user_prefs.get("disliked_moods", [])]:
        score -= 1
        explanation.append(f"-1 disliked mood: {mood}")

    # Artist
    artist = get_str(song, "artist")
    if artist in [a.lower() for a in user_prefs.get("favorite_artists", [])]:
        score += 2
        explanation.append(f"+2 favorite artist: {artist}")

    # Helper for similarity scoring
    def similarity_score(song_val, target_val, max_points, value_range=1.0):
        diff = abs(song_val - target_val)
        sim = max_points * (1 - (diff / value_range))
        return max(sim, 0)

    # Energy (range 0-1)
    energy = get_float(song, "energy")
    if user_prefs.get("target_energy_range"):
        min_e, max_e = user_prefs["target_energy_range"]
        if min_e <= energy <= max_e:
            s = 2.0
            score += s
            explanation.append(f"+2 energy in range: {energy}")
        else:
            # Reward closeness to nearest bound
            target = min(max(energy, min_e), max_e)
            s = similarity_score(energy, target, 2.0, 1.0)
            score += s
            explanation.append(f"+{s:.2f} energy similarity: {energy}")

    # Tempo (range: use 60-200 bpm as typical bounds)
    tempo = get_float(song, "tempo_bpm")
    if user_prefs.get("target_tempo_range"):
        min_t, max_t = user_prefs["target_tempo_range"]
        if min_t <= tempo <= max_t:
            s = 2.0
            score += s
            explanation.append(f"+2 tempo in range: {tempo}")
        else:
            # Reward closeness to nearest bound
            target = min(max(tempo, min_t), max_t)
            s = similarity_score(tempo, target, 2.0, 140.0)  # 60-200 bpm = 140 range
            score += s
            explanation.append(f"+{s:.2f} tempo similarity: {tempo}")

    # Valence (range 0-1)
    valence = get_float(song, "valence")
    if user_prefs.get("target_valence") is not None:
        s = similarity_score(valence, user_prefs["target_valence"], 1.0, 1.0)
        score += s
        explanation.append(f"+{s:.2f} valence similarity: {valence}")

    # Danceability (range 0-1)
    danceability = get_float(song, "danceability")
    if user_prefs.get("target_danceability") is not None:
        s = similarity_score(danceability, user_prefs["target_danceability"], 1.0, 1.0)
        score += s
        explanation.append(f"+{s:.2f} danceability similarity: {danceability}")

    # Acousticness (range 0-1)
    acousticness = get_float(song, "acousticness")
    if user_prefs.get("target_acousticness") is not None:
        s = similarity_score(acousticness, user_prefs["target_acousticness"], 1.0, 1.0)
        score += s
        explanation.append(f"+{s:.2f} acousticness similarity: {acousticness}")

    return score, "; ".join(explanation)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top k recommended songs for a user, with scores and explanations."""
    # Score each song and collect (song, score, explanation)
    results = []
    for song in songs:
        score, explanation = score_song(user_prefs, song)
        results.append((song, score, explanation))

    # Print all songs and their scores
    print("\nAll songs and their scores:")
    for song, score, _ in results:
        print(f"{song['title']}: {score:.2f}")

    # Sort results by score descending
    # sorted() returns a new sorted list, leaving the original unchanged.
    # .sort() sorts a list in place and returns None.
    # Here, we use sorted() for clarity and to avoid side effects.
    results_sorted = sorted(results, key=lambda x: x[1], reverse=True)

    # Return top k
    return results_sorted[:k]
