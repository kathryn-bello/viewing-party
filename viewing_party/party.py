# ------------- WAVE 1 --------------------

def create_movie(movie_title, genre, rating):
    if movie_title == None or genre == None or rating == None:
        return None
    movie = {"title":movie_title, "genre":genre, "rating":rating}
    return movie

def add_to_watched(user_data, movie):
    if movie["title"] not in user_data["watched"]:
        user_data["watched"].append(movie)
    return user_data
    
def add_to_watchlist(user_data, movie):
    if movie["title"] not in user_data["watchlist"]:
        user_data["watchlist"].append(movie)
    return user_data
    
def watch_movie(user_data, movie_title):
    for movie in user_data["watchlist"]:
        if movie_title == movie["title"] and movie_title not in user_data["watched"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data
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
            if 'genre' in movie:
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
def get_unique_watched(user_data):
    user_watched = []
    friend_watched = []  
    user_unique_watched = []

    for watched_movie in user_data['friends']:
        for movie in watched_movie["watched"]:
            friend_watched.append(movie)
    for movie in user_data["watched"]:
        user_watched.append(movie)
    for movie in user_watched:
        if movie not in friend_watched:
            user_unique_watched.append(movie)

    
    return user_unique_watched    

def get_friends_unique_watched(user_data):
    user_watched = []
    friend_watched = []  
    friends_unique_watched = []

    for watched_movies in user_data['friends']:
        for movie in watched_movies["watched"]:
            if movie not in friend_watched:
                friend_watched.append(movie)
    for movie in user_data["watched"]:
        user_watched.append(movie)
    for movie in friend_watched:
        if movie not in user_watched:
            friends_unique_watched.append(movie)

    return friends_unique_watched    

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    user_list = user_data["watched"]
    friends_list = user_data["friends"]

    # check if subscriptions key exists
    if "subscriptions" not in user_data or not user_data["subscriptions"]:
        subscriptions = set([])
    else:
        subscriptions = set(user_data["subscriptions"])

    user_set = set()
    recommended_set = set()
    recommended = []
    
    for movie in user_list:
        user_set.add(movie['title'])
        
    for friend in friends_list:
        if friend['watched']:
            for movie in friend['watched']:
                if movie['host'] in subscriptions:
                    movie_title = movie['title']
                    # check if user hasn't watched movie and we didn't add it already
                    if movie_title not in user_set and movie_title not in recommended_set:
                        recommended.append(movie)
                        recommended_set.add(movie_title)

    return recommended

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    genre = get_most_watched_genre(user_data)
    recommended = get_available_recs(user_data)
    recommended_by_genre = []

    for movie in recommended:
        if movie['genre'] == genre:
            recommended_by_genre.append(movie)

    return recommended_by_genre

def get_rec_from_favorites(user_data):
    recommended = []
    recommended_set = set()
    friends_set = set()
    friends_list = user_data["friends"]
    favorites_list = user_data["favorites"]

    # if empty favorites list -> return empty recommneded list
    if not favorites_list:
        return recommended
    else:
        # if empty friends list -> return favorites list
        if not friends_list:
            recommended = list(favorites_list)
            return recommended
        
        for friend in friends_list:
            for movie in friend['watched']:
                friends_set.add(movie['title'])

        for movie in favorites_list:
            movie_title = movie['title']
            # check if friends have not watched movie and we didn't add it already
            if movie_title not in friends_set and movie_title not in recommended_set:
                recommended.append(movie)
                recommended_set.add(movie_title)

    return recommended