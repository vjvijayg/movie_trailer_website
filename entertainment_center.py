# -*- coding: utf-8 -*-
import fresh_tomatoes
import media

# Importing the freshtomatoes and media libraries

"""Movie class from media library is used here to assign the movie content
   passed as parameters to Movie class attributes as followed
   movie_title, movie_storyline, poster_image, trailer_youtube"""

paris = media.Movie(
    "Midnight in Paris",
    "Gil Pender, a successful but creatively unfulfilled screenwriter, and his\
     fiancée Inez, are in Paris vacationing with Inez's wealthy, conservative\
     parents. Gil is struggling to finish his first novel, centered on a man\
     who works in a nostalgia shop. Inez dismisses his ambition as a romantic\
     daydream, & encourages him to stick with lucrative screenwriting. Gil is\
     considering moving to Paris.",
    "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
    "https://www.youtube.com/watch?v=BYRWfS2s2v4")

inception = media.Movie(
    "Inception",
    "Dominick Cobb & Arthur are extractors, who perform corporate espionage\
     using an experimental military technology to infiltrate the subconscious\
     of their targets & extract valuable information through a shared dream\
     world. Their latest target, Japanese businessman Saito, reveals that he\
     arranged their mission himself to test Cobb for a seemingly-impossible\
     job: planting an idea in a person's subconscious, or inception.",
    "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
    "https://www.youtube.com/watch?v=YoHD9XEInc0")

interstellar = media.Movie(
    "Interstellar",
    "Sometime in the 21st century, a series of crop blights on Earth threatens\
     humanity's survival. Joseph, a widowed former NASA pilot, runs a farm with\
     his father-in-law, son, & daughter. Living in a post-truth society,\
     Cooper encourages Murph to carefully observe and record what she sees.",
    "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
    "https://www.youtube.com/watch?v=M-xglYg-TTw")

chappie = media.Movie(
    "Chappie",
    "the South African government purchases a squadron of state-of-the-art,\
     armour-plated attack robots from weapons manufacturer Tetravaal, developed\
     by Deon Wilson. A competing project is the remotely controlled MOOSE,\
     developed by soldier-turned-engineer Vincent Moore. Deon is praised for\
     Tetravaal's success but Vincent grows jealous when the police are\
     unwilling to give his heavy weapons platform equal attention",
    "https://upload.wikimedia.org/wikipedia/en/7/71/Chappie_poster.jpg",
    "https://www.youtube.com/watch?v=l6bmTNadhJE")

nysm = media.Movie(
    "Now you see Me",
    "Four stage magicians, are each given a tarot card that lead them to the\
     same empty New York City apartment, where they find information from an\
     unknown benefactor.",
    "https://upload.wikimedia.org/wikipedia/en/c/c7/Now_You_See_Me_Poster.jpg",
    "https://www.youtube.com/watch?v=4OtM9j2lcUA")

focus = media.Movie(
    "Focus",
    "Seasoned con-man goes to an upscale restaurant, where an inexperienced\
     grifter, Jess, seduces him, and then pretends they've been caught by her\
     jealous husband. When the deception fails, Nicky them never to lose focus\
     when faced with unexpected situations. Jess finds him in another nightclub\
     a few days later and convinces Nicky to become her mentor.",
    "https://upload.wikimedia.org/wikipedia/en/b/bf/2015_Focus_film_poster.png",
    "https://www.youtube.com/watch?v=MxCRgtdAuBo")

pursuit = media.Movie(
    "The Pursuit of Happyness",
    "salesman invests his entire life savings in portable bone density\
     scanners. The scanners play a vital role in his life. While he is able\
     to sell most of them, the time lag between the sales & his growing\
     financial demands enrage his already bitter & alienated wife, who works\
     as a hotel maid. The financial instability increasingly erodes their\
     marriage, in spite of them caring for their 5 year old son.",
    "https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg",
    "https://www.youtube.com/watch?v=89Kq8SDyvfg")

baahubali = media.Movie(
    "Baahubali 2 - The Conclusion",
    "the ancient Empire of Mahishmati, Sivagami, the queenmother, emerges\
     injured from a cave adjoining a big waterfall, carrying a baby.\
     She kills the soldiers pursuing her & sacrifices herself to save baby\
     Local tribal communities save the baby & the tribal queen, adopts him.",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/Baahubali_the_Conclusion.jpg",
    "https://www.youtube.com/watch?v=G62HrubdD6o")

# Here all the Movies list is created
movies = [inception, interstellar, chappie,
          nysm, focus, paris, pursuit, baahubali]

# movies list and all the content passed to Browser through open_movies_page
# open_movies_page funstion is defined in fresh_tomatoes library
fresh_tomatoes.open_movies_page(movies)

