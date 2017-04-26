import webbrowser


class Movie():

    """
    This is the constructor of Movie class and accepts 4 extra arguments -
    movie_title - Title of the movie
    movie_storyline - Description of the movie
    poster_image_url - URL of the poster of the movie
    trailer_youtube_url - URL of the movie trailer
    """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    # Opens the webpage with trailor URL provided in entertainment_center.
    def show_trailor(self):
        webbrowser.open(self.trailor_url)
