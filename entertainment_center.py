import media
import fresh_tomatoes

"""Create a list of Movie objects."""
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy an his toys that come to life..",
    "Tom Hanks, Tim Allen, Don Rickles, Jim Varney",
    "1995",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie(
    "Avatar",
    "A Paraplegic Marine dispatched to the moon Pandora on \
    a unique mission becomes torn between following his orders \
    and protecting the world he feels is his home..",
    "Sam Worthington, Zoe Saldana, Sigourney Weaver, Stephen Lang",
    "2009",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

school_of_rock = media.Movie(
    "School of Rock",
    "A rocker who poses as a substitute\
    teacher at a prestigious prep school..",
    "Tony Cavalero, Ricardo Hurtado, Lance Lim",
    "2003",
    "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie(
    "Ratatouille",
    "A rat who can cook makes an unusual alliance\
    with a young kitchen worker at a famous restaurant.",
    "Patton Oswalt, Ian Holm, Lou Romano, Brian Dennehy",
    "2007",
    "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "http://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie(
    "Midnight in Paris",
    "A screenwriter finds himself mysteriously going \
    back to the 1920s every day at midnight..",
    "Owen Wilson, Rachel McAdams, Kurt Fuller",
    "2011",
    "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
    "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie(
    "Hunger Games",
    "Katniss Everdeen is in District 13 after \
    she shatters the games forever..",
    "Jennifer Lawrence, Josh Hutcherson, Liam Hemsworth",
    "2014",
    "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
    "http://www.youtube.com/watch?v=PbA63a7H0bo")

#  create a list of movies.
movies = [
    toy_story, avatar, school_of_rock,
    ratatouille, midnight_in_paris, hunger_games,
    ]

#   call open_movies_page() function in fresh_tomatoes.py
#   to build the html file and display the website.
fresh_tomatoes.open_movies_page(movies)
