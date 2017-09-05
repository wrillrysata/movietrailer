
FRESH TOMATOES MOVIE TRAILER is an Udacity Fullstack Nanodegree Project. The idea is to be able to view trailers of selected movies on site.
It was built with Python, HTML, CSS and JQUERY.



## Table of contents

- [Demo](#demo)
- [Download](#download)
- [Prerequisites](#Prerequisites)
- [Contents](#contents)
- [Installation](#installation-and-usage)
- [Documentation](#documentation)
- [Credits](#copyright-and-license)

## Demo

For a demo, check out <>!

## Download

The files for the project, may be [downloaded here](https://github.com/Ijebusoma/movietrailer/archive/master.zip).

## Prerequisites
You need to have Python 2.7 installed on your local machine for this project to work. Click here to download and install Python. If you're on a linux machine, you should have Python installed already. To check, do CTRL + ALT + T and type python at the shell prompt. It should give you the python version.

## Contents
The projects contains the following files:
css
js
movieclass.py 
movie.py
freshtomatoes.py
freshtomatoes.html

## Installation and Usage
To install Fresh Tomatoes locally, clone the project into your system, on your terminal, switch into the directory you just cloned and do python movie.py. This command would trigger a new tab in your browser and generate a HTML page(freshtomatoes.html)

## Documentation
__class Movie__ This is the blueprint file. It is located in the movieclass.py file. It contains a simple constructor with 4 instance variables namely title, storyline, poster_image_url and trailer_youtube_url which is invoked when an object of this class is created.
__freshtomatoes.py__ This structures the HTML content and contains functions that dynamically generates content into the view.
__class movies.py__  Based on the properties defined(e.g movie_title) in the previous class(movieclass.py), this class stores the actual movies. This is where the movie objects are actually created and given values. 'freshtomatoes' and 'movieclass' are imported into this class for it to function. After giving real values to the movie objects, they are saved in an array called movies. The class then calls a function open_movies_page defined in freshtomatoes.py, takes in the array of movies as argument and prepares them from transportaion into the HTML view.

## Copyright and License

- Boilerplate code contributed by [Udacity](http://www.udacity.com).
- Additional code contributed by [Ijebusoma]() is offered under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).
Bootstrap 3


