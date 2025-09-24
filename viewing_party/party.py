# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    pass

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating = 0.0
    count = 0

    if not user_data:
        return None

    for movies in user_data.values():
        if not movies:
            average_rating = 0.0
            return average_rating
        
        for movie in movies:
            count += 1
            rating += movie["rating"]
    
    rating = rating/count
    return rating

def get_most_watched_genre(user_data):
    genre_count = {}
    most_watched_genre = ""
    most_watched = 0

    if not user_data:
        return None

    for movies in user_data.values():
        if not movies:
            return None
        
        for movie in movies:
            genre = movie["genre"]
            
            if genre not in genre_count:
                genre_count[genre] = 1
            else:
                genre_count[genre] += 1
            most_watched = genre_count[genre]
    
    for genre in genre_count:
        if genre_count[genre] > most_watched:
            most_watched = genre_count[genre]
            most_watched_genre = genre
    return most_watched_genre



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

