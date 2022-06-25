# Spotify-Top-100-Billboard-Playlist
Creates a spotify playlist from user input of a specific date in time

-It first gets the Spotify authentication from user's id and secrets
-Then asks user for input of a specific date in the format YYYY-MM-DD
-Using BeautifulSoup, a web scraping API, it finds the titles from the Billboard 100 website and appends it to a list
-Then, it creates a playlist and then adds the songs using its specific URI id
