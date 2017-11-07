#import modules
import fresh_tomatoes
import media
#calling the constructor media.Movie()to instantiate movie objects
justice_league = media.Movie("Justice League",
    "Bat Man is Back and He has Friends",
    "http://www.aceshowbiz.com/images/news/justice-league-poster-brings-back-superman.jpg",  # NOQA
    "https://https://www.youtube.com/watch?v=OiAmnKUaNmc")
star_wars = media.Movie("Star Wars the Last Jedi",
    "The Force awakens and Rey will continue her epic journey.",
    "http://static.metacritic.com/images/products/movies/7/886af5a18f3e5d38779237beb76cc42a.jpg",  # NOQA
    "https://www.youtube.com/watch?v=TYRy5bCsWF8")
edge_of_tomorrow = media.Movie("Edge of Tomorrow",
    "The Day to Save the World - Get it Right",
    "https://tse2.mm.bing.net/th?id=OIP.LynLECaR-zicJ9Hji2UkkAE0DK&w=242&h=160&c=7&qlt=90&o=4&pid=1.7",  # NOQA
    "https://www.youtube.com/watch?v=vw61gCe2oqI")
#load instances in fresh tomatoes function to build HTML
movies = [justice_league, star_wars, edge_of_tomorrow]
fresh_tomatoes.open_movies_page (movies)
