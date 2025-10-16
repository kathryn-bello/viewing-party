# ------------- WAVE 1 --------------------

def create_movie(movie_title, genre, rating):
    if not movie_title or not genre or not rating:
        return None
    return {"title":movie_title, "genre":genre, "rating":rating}


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data
    
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data
    
def watch_movie(user_data, movie_title):
    for movie in user_data["watchlist"]:
        if movie_title == movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            break
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0.0
    
    rating = 0.0
    for movie in user_data["watched"]:
        rating += movie["rating"]
    
    return rating / len(user_data["watched"])

def get_most_watched_genre(user_data):
    genre_count = {}
    most_watched_genre = ""
    most_watched = 0

    if not user_data["watched"]:
        return None
    
    for movies in user_data["watched"]:
        if 'genre' in movies:
            genre = movies["genre"]
            genre_count[genre] = genre_count.get(genre, 0) +1
    
    for genre in genre_count:
        if genre_count[genre] > most_watched:
            most_watched = genre_count[genre]
            most_watched_genre = genre

    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    friend_watched_titles = get_friends_movie_titles(user_data)
    user_unique_watched_movies = []

    for movie in user_data["watched"]:
        if movie["title"] not in friend_watched_titles:
            user_unique_watched_movies.append(movie)

    return user_unique_watched_movies

def get_friends_unique_watched(user_data):
    user_watched_titles = get_movie_titles(user_data["watched"])
    friends_movies = get_friends_movies(user_data)
    friends_watched_titles = set()
    friends_unique_watched_movies = []

    for movie in friends_movies:
        title = movie["title"]
        if title not in friends_watched_titles and title not in user_watched_titles:
            friends_watched_titles.add(title)
            friends_unique_watched_movies.append(movie)

    return friends_unique_watched_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    if "subscriptions" not in user_data or not user_data["subscriptions"]:
        return []
    
    friends_movie_list = get_friends_unique_watched(user_data)
    subscriptions = set(user_data["subscriptions"])
    user_watched_titles = get_movie_titles(user_data["watched"])
    recommended_movies = []
    recommended_set = set()
    
    for movie in friends_movie_list:
        if movie['host'] in subscriptions:
            movie_title = movie['title']
            if movie_title not in user_watched_titles and movie_title not in recommended_set:
                recommended_movies.append(movie)
                recommended_set.add(movie_title)

    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)
    available_recs = get_available_recs(user_data)
    
    # list comprehension
    return [movie for movie in available_recs if movie['genre'] == most_watched_genre]


def get_rec_from_favorites(user_data):
    if not user_data["favorites"]:
        return []
    
    # getting all the movie titles friends have watched
    friends_movie_titles = get_friends_movie_titles(user_data)
    
    recommended_movies = []
    user_watched = set()

    for movie in user_data["favorites"]:
        movie_title = movie['title']
        if movie_title not in friends_movie_titles and movie_title not in user_watched:
            recommended_movies.append(movie)
            user_watched.add(movie_title)

    return recommended_movies

# -----------------------------------------
# ---------- HELPER FUNCTIONS -------------
# -----------------------------------------
# To extract movie titles
def get_movie_titles(movies_list):
    return { movie["title"] for movie in movies_list }

# To extract friends movies from user_data
def get_friends_movies(user_data):
    friends_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movies.append(movie)
    return friends_movies

# To extract titles from friends movies
def get_friends_movie_titles(user_data):
    friends_movies = get_friends_movies(user_data)
    return get_movie_titles(friends_movies)
