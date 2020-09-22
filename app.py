from flask import Flask, render_template, flash, redirect, url_for, request, redirect, session, abort
import flask
from flask_caching import Cache
import random
from datetime import date
import get_weather
import get_songs
import db
import model


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
weather = get_weather.weather()
time_ = get_weather.timeZone()
today_ = date.today().strftime("%B %d, %Y")



@app.route("/", methods=["GET", "POST"])
def index():
    global id_
    global pwd_
    global songList_user
    global songList
    global gender_, age_, genre1, genre2, genre3
    weather_tag = get_weather.get_weather_tag()
    playlist = model.recommendation(weather_tag[0], weather_tag[1])
    songList = get_songs.song_playlist(playlist)
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]

        login = db.user_info_select(uname,passw)

        if login is not None:
            gender_,age_,genre1,genre2,genre3 = login[2],int(login[3]),login[4],login[5],login[6]
            playlist = model.recommendation(weather_tag[0], weather_tag[1], gender_, age_, genre1, genre2, genre3)
            genre_ = get_songs.get_genre(genre1, genre2, genre3)
            songList_user = get_songs.song_playlist((playlist+genre_))
            random.shuffle(songList_user)
            return redirect(url_for("user"))


    return render_template("index.html")

@app.route("/update", methods=["GET", "POST"])
def update():
    id_ = request.form.get('id_')
    pwd_ = request.form.get('pwd_')
    age = request.form.get('age')
    gender = request.form.get('gender')
    genre1 = request.form.get('jazz')
    genre2 = request.form.get('rock')
    genre3 = request.form.get('hiphop')
    genre4 = request.form.get('ballad')
    genre5 = request.form.get('dance')
    genre6 = request.form.get('others')

    aList = [genre1,genre2,genre3,genre4,genre5,genre6]
    genre = list()
    for g in aList:
        if g != None:
            genre.append(g)
    if len(genre)==1:
        genre = [genre[0]]+[genre[0]]+[genre[0]]
    if len(genre)==2:
        genre = [genre[0]]+[genre[0]]+[genre[1]]

    db.user_info_insert(id_,pwd_,gender,age,genre[0],genre[1],genre[2])

    return redirect(url_for("index"))



@app.route("/signup", methods=["GET", "POST"])
def signup():
        return render_template("signup.html")







@app.route("/user")
def user():
    today_ = date.today().strftime("%B %d, %Y")
    weather_info = get_weather.get_weather()
    song = songList_user[:6]

    try:
        print(id_, pwd_, "day")
        return render_template("user.html",songList=song,weather_info=weather_info, today=today_,theme=get_weather.get_weather_theme())
    except(NameError):
        return render_template("user.html",songList=song,weather_info=weather_info, today=today_, theme=get_weather.get_weather_theme())

@app.route("/guest")
def guest():
    song=list()
    today_ = date.today().strftime("%B %d, %Y")
    weather_info = get_weather.get_weather()
    songs = songList[:6]
    while len(song) < 6:
        s = random.choices(songs)
        if s[0] not in song:
            song += s
    return render_template("guest.html",songList=song,weather_info=weather_info, today=today_,theme=get_weather.get_weather_theme('비','밤'))



@app.route('/re_user')
def re_user():
    song=[]
    today_ = date.today().strftime("%B %d, %Y")
    weather_info = get_weather.get_weather()
    songs = songList_user[6:]
    print(songs)
    while len(song) < 6:

        s = random.choices(songs)
        print(s)
        if s[0] not in song:
            song+=s
            print(song)
    try:
        print(id_, pwd_, "day")
        return render_template("user.html",songList=song,weather_info=weather_info, today=today_,theme=get_weather.get_weather_theme())
    except(NameError):
        return render_template("user.html",songList=song,weather_info=weather_info, today=today_,theme=get_weather.get_weather_theme())


@app.route('/re')
def re():
    song=[]
    today_ = date.today().strftime("%B %d, %Y")
    weather_info = get_weather.get_weather()
    songs = songList[6:]
    print(songs)
    while len(song) < 6:

        s = random.choices(songs)
        print(s)
        if s[0] not in song:
            song+=s
            print(song)
    try:
        print(id_, pwd_, "day")
        return render_template("guest.html",songList=song,weather_info=weather_info, today=today_,theme=get_weather.get_weather_theme())
    except(NameError):
        return render_template("guest.html",songList=song,weather_info=weather_info, today=today_,theme=get_weather.get_weather_theme())


if __name__ == '__main__':
    app.run(debug=True)
