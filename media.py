import webbrowser


class Movie():
    """Create Movie object.
        Attributes:
            movie_title: A string describing the title of the movie
            movie_storyline: A string describing the storyline of the movie
            movie_actors: A string showing the actors of the movie
            movie_year: A string describing the year of the movie
            movie_poster: A string containing the url of the movie poster image
            trailer_youtube_url:
                A string containing the youtube url of the movie trailer
    """
    def __init__(self, movie_title, movie_storyline, movie_actors,
                 movie_year, movie_poster, trailer_youtube_url):
        """Initializes Movie class with some movie attributes."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.actors = movie_actors
        self.year = movie_year
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = trailer_youtube_url
