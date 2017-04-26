# Introduction #

This is a server-side code written in Python to store the list of my favorite movies.

# Prerequisites: #
    Python 2.7 - https://www.python.org/download/releases/2.7/#download

# Steps to open the website #
    
    *Download .zip file and unzip it to a specific folder.
    *Open entertainment_center.py in idle and run it. A webpage will open automatically after compiling the code.
    *Click on any poster and its respective trailor will be played.

# Standard Python Libararies Used: #

    *urllib: The urlopen() function of urllib is used to open a network object denoted by a URL for reading.
    *webbrowser: The open() function of webbrowser is used to display url using the default browser.
    *json: This module helps to deal with data in JSON format.

# How to add your favorite movie #

    *Open entertainment.py using python IDLE.
    *Call the get_info method with your favorite movie as a string argument. For Example: data = get_info("Deadpool")
    *Add the title, Plot, Poster URL and Youtube URL of the movie as arguments in Movie class contructor in media.py file.
    *Add this object in the movies array and run the module.
    That's it!

# Changes Made #

    *Used omdb API to get the data of the website in JSON Format.

        def get_info(movie_name):
            response = urllib.urlopen("http://www.omdbapi.com/?t="+movie_name+"&y=&plot=short&r=json")
            output = response.read()
            wjdata = json.loads(output)
            return wjdata

    *Style:
        a. Changed the Background

            body {
                padding-top: 80px;
                background-image : url("red.jpg");
                -webkit-background-size: cover;
                -moz-background-size: cover;
                -o-background-size: cover;
                background-size: cover;
            }

        b. Change the font attributes of Header and Title of movies

            @import url('https://fonts.googleapis.com/css?family=Permanent+Marker|Sigmar+One');
            
            .main_font {
                font-family: 'Sigmar One', cursive;
                font-size: 40px;
                font-color: #FFFFFF;
                position: relative;
            }

            .title {
                font-family: 'Permanent Marker', cursive;
                color:white;
            }

        c. Added border in the Movie Tiles

            .movie-tile {
                margin-bottom: 20px;
                padding-top: 20px;
                border: 2px solid white;
                border-spacing: 10px;
            }
