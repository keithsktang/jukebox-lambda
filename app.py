from chalice import Chalice

app = Chalice(app_name='jukebox')

songs_list = [
[
{"id":1,"album_id":1,"song_name":"Legend","song_order":5,"song_label":["explicit","upbeat"],"song_duration":"4:01"},
{"id":2,"album_id":1,"song_name":"Energy","song_order":1,"song_label":"","song_duration":"3:01"},
{"id":3,"album_id":1,"song_name":"10 Bands","song_order":4,"song_label":["explicit","upbeat"],"song_duration":"2:57"},
{"id":4,"album_id":1,"song_name":"Know Yourself","song_order":2,"song_label":"","song_duration":"4:35"},
{"id":5,"album_id":1,"song_name":"No Tellin'","song_order":3,"song_label":["explicit","upbeat"],"song_duration":"5:10"}],
[
{"id":6,"album_id":2,"song_name":"Did I Hear You Say You Love Me","song_order":3,"song_label":["explicit","upbeat"],"song_duration":"4:07"},
{"id":7,"album_id":2,"song_name":"All I Do","song_order":5,"song_label":["explicit"],"song_duration":"5:06"},
{"id":8,"album_id":2,"song_name":"Rocket Love","song_order":4,"song_label":[],"song_duration":"4:39"},
{"id":9,"album_id":2,"song_name":"I Ain't Gonna Stand for It","song_order":2,"song_label":["explicit"],"song_duration":"4:39"},
{"id":10,"album_id":2,"song_name":"As If You Read My Mind","song_order":1,"song_label":[],"song_duration":"3:37"}],
[
{"id":11,"album_id":3,"song_name":"One More Night","song_order":4,"song_label":["explicit","upbeat"],"song_duration":"3:39"},
{"id":12,"album_id":3,"song_name":"Payphone","song_order":3,"song_label":[],"song_duration":"3:51"},
{"id":13,"album_id":3,"song_name":"Daylight","song_order":1,"song_label":["explicit","upbeat"],"song_duration":"3:45"},
{"id":14,"album_id":3,"song_name":"Lucky Strike","song_order":5,"song_label":"","song_duration":"3:05"},
{"id":15,"album_id":3,"song_name":"The Man Who Never Lied","song_order":2,"song_label":["explicit","upbeat"],"song_duration":"3:25"}],
[
{"id":16,"album_id":4,"song_name":"Million $ Show","song_order":3,"song_label":["explicit","upbeat"],"song_duration":"3:39"},
{"id":17,"album_id":4,"song_name":"Payphone","song_order":5,"song_label":["explicit"],"song_duration":"3:51"},
{"id":18,"album_id":4,"song_name":"Ain't About 2 Stop","song_label":["explicit"],"song_order":1,"song_duration":"3:39"},
{"id":19,"album_id":4,"song_name":"Like a Mack","song_order":2,"song_label":["slow"],"song_duration":"4:05"},
{"id":20,"album_id":4,"song_name":"This Could B Us","song_order":4,"song_duration":"4:11"}],
[
{"id":21,"album_id":5,"song_name":"Everlasting Light","song_order":5,"song_label":["explicit","upbeat"],"song_duration":"3:24"},
{"id":22,"album_id":5,"song_name":"Next Girl","song_order":3,"song_label":["explicit"],"song_duration":"3:18"},
{"id":23,"album_id":5,"song_name":"Tighten Up","song_order":2,"song_duration":"3:31"},
{"id":24,"album_id":5,"song_name":"Howlin' for You","song_order":4,"song_label":["explicit"],"song_duration":"3:12"},
{"id":25,"album_id":5,"song_name":"She's Long Gone","song_order":1,"song_duration":"3:12"}]
]

albums = [
{"id":1,"name":"If Your'e Reading This It's Too Late","artist_name":"DRAKE","cover_photo_url":"https://s3.amazonaws.com/jukebox-album/album-1.png"},
{"id":2,"name":"Hotter Than July","artist_name":"Stevie Wonder","cover_photo_url":"https://s3.amazonaws.com/jukebox-album/album-2.png"},
{"id":3,"name":"Overexposed","artist_name":"Maroon 5","cover_photo_url":"https://s3.amazonaws.com/jukebox-album/album-3.png"},
{"id":4,"name":"Hit n Run Phase One","artist_name":"PRINCE","cover_photo_url":"https://s3.amazonaws.com/jukebox-album/album-4.png"},
{"id":5,"name":"Brothers","artist_name":"The Black Keys","cover_photo_url":"https://s3.amazonaws.com/jukebox-album/album-5.png"}]

@app.route('/')
def index():
    return {"welcome": "to Jukebox"}

@app.route('/album')
def album():
    return albums

@app.route('/songs/{song_id}')
def songs(song_id):
    return songs_list[int(song_id)-1]




# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
