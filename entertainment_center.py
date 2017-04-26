import media
import fresh_tomatoes
import urllib
import json


def get_info(movie_name):
    # Get a response after opening the URL
    response = urllib.urlopen("http://www.omdbapi.com/?t="+movie_name+
                              "&y=&plot=short&r=json")
    # Data from the website in the form of JSON is recieved
    output = response.read()
    # Parsing Values from JSON data
    wjdata = json.loads(output)
    return wjdata

# get_info method takes the Movie name as the argument
# and stores the returned data in info variable
info = get_info("Batman v Superman: Dawn of Justice")
# Constructor of Movie Class takes title, description, image URL
# and YouTube Link of the trailer as argument
bat_vs_sup = media.Movie(info['Title'], info['Plot'], info['Poster'],
                         "https://www.youtube.com/watch?v=fis-9Zqu2Ro")

info = get_info("Ice Age: Collision Course")
tarzan = media.Movie(info['Title'], info['Plot'], info['Poster'],
                     "https://www.youtube.com/watch?v=Aj7ty6sViiU")

info = get_info("Captain America: Civil War")
capt_america = media.Movie(info['Title'], info['Plot'], info['Poster'],
                           "https://www.youtube.com/watch?v=dKrVegVI0Us")

info = get_info("Suicide Squad")
suicide = media.Movie(info['Title'], info['Plot'], info['Poster'],
                      "https://www.youtube.com/watch?v=CmRih_VtVA")

info = get_info("Doctor Strange")
doc_strange = media.Movie(info['Title'], info['Plot'], info['Poster'],
                          "https://www.youtube.com/watch?v=HSzx-zryEgM")

info = get_info("Deadpool")
deadpool = media.Movie(info['Title'], info['Plot'], info['Poster'],
                       "https://www.youtube.com/watch?v=gtTfd6tISfw")

# Array of Movie objects
movies = [bat_vs_sup, tarzan, capt_america, suicide, doc_strange, deadpool]
# movies array is passed to open_movies_page function to load
# the webpage with the information provided
fresh_tomatoes.open_movies_page(movies)
