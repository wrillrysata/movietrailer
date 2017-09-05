import webbrowser
import os
import re

# Styles and scripting for the page

main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="css/main.css">
    <link rel="stylesheet" href="css/css/font-awesome.min.css">
    <link href="https://fonts.googleapis.com/css?family=Dosis" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Shadows+Into+Light" rel="stylesheet">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
   <script type="text/javascript" src="js/main.js"></script>
  </head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <div class="container">
   <!--medium sized posters -->
    <div class="tv-section">
    <h3>On Tv</h3>
    <img class="img-responsive" src = "images/suits.jpg" width="550" height="500">
    </div>
    <div class="cinema-section">
    <h3>In Cinemas</h3>
    </div>
    <div id="container">
    <div id="floated-imgs">
        <img class = "img-responsive" src="images/darktower.jpg">
        <img class="hitman img-responsive" src="images/hit.jpg">
    </div>
 </div>
</div>
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          
           <h3 class="caption">Fresh Tomatoes Movie Trailer</h3>
           </div>
        </div>
      <h4><center>Featured Movies</center</h4>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
    <footer>
<div class="content"> Made with <i class="fa fa-heart love" aria-hidden="true"></i> by Vanessa
</div>
</footer>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center">
    <img src="{poster_image_url}" movie_storyline="{movie_storyline}" class="poster" width="220" height="342">
    <h2>{movie_title}</h2>
   <!-- <h3 class ="storyline">{movie_storyline}</h3> -->
    <button class="btn btn-primary play" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer"><i class="fa fa-play" aria-hidden="true">Watch</button></i>
    
</div>

'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None
# Append the tile for the movie with its content filled in
    content += movie_tile_content.format(
            movie_title=movie.title,
            movie_storyline = movie.storyline,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))


# Output the file
output_file.write(main_page_head + rendered_content)
output_file.close()
# open the output file in the browser
url = os.path.abspath(output_file.name)
webbrowser.open('file://' + url, new=2)  # open in a new tab, if possible
