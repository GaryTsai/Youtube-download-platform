from flask import Flask,render_template, request, session ,redirect, app
from modles import request_soup as rs
from modles.user  import User
from common.database import  Database
from datetime import timedelta
from modles.video import Video


app = Flask(__name__)
app.secret_key = "gary"

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(seconds=1)

@app.before_first_request
def init_db():
    Database.initialize()
    session['account'] = session.get('account')
    session['name'] = session.get('name')

@app.route("/")
@app.route("/index")
def hello():
    return render_template("home.html")
# 註冊
@app.route("/register", methods=['GET','POST'])
def register_method():
    if request.method == 'POST':
        name = request.form['InputName']
        account = request.form['InputAccount']
        password = request.form['InputPassword']
        result = User.register_user(name, account , password)
        if result == True:
            session['account'] = account
            session['name'] = User.find_user_data(account).get('name')
            return redirect("/")
        else:
             message = "Your account already exist"
             return  render_template("register.html",message = message)
    else:
        return render_template("register.html")
# login
@app.route("/login", methods=['GET','POST'])
def login_method():
    if request.method == 'POST':
        account = request.form['InputAccount']
        password = request.form['InputPassword']
        # print(account)
        # print(password)
        check = User.is_login_valid(account, password)
        if check is True:
            session['account'] = account
            session['name'] = User.find_user_data(account).get('name')

            return redirect("/")
        else:
             message = "Your email or password is worong"
             return  render_template("login.html",message = message)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout_method():
    session['account'] = not session['account']
    return redirect("/")
@app.route("/results")
def result_page():
    url = request.url
    page = request.args.get('sp')
    favorite_video = []
    user_favorite = Video.find_video(session['account'])
    for video in user_favorite:
        favorite_video.append(video['link'])

    if page is None:
        url = request.url
        search = request.args.get('search')
        soup = rs.find_search_content(search)
        all_item = rs.every_video(soup)
        # print(all_item)
        all_page =rs.page_bar(soup)
        return render_template("result.html",search = search,all_item=all_item,all_page = all_page,url = url, favorite_video = favorite_video)
    elif page is not None:
        search = request.args.get('search_query')
        print(search)
        page = request.args.get('sp')
        current_page = request.args.get('current_page')
        value = "q={}".format(search) +"&"+"sp={}".format(page)
        print(value)
        soup = rs.find_page_content(value)
        all_item = rs.every_video(soup)
        # print(all_item)
        all_page =rs.page_bar(soup)
        return render_template("result_page.html", search = search,all_item=all_item,all_page = all_page, current_page=current_page, int=int, url =url, favorite_video = favorite_video)
    else:
        return redirect("/")

@app.route("/favorite",methods=['GET', 'POST'])
def favorite_method():
    # print(session['account'])
    if session['account']:
        if request.method == 'POST':
            url = request.form['url']
            title = request.form['title']
            link = request.form['link']
            img = request.form['img']
            account = session['account']
            Video(account, title, link, img).save_to_db()
            return redirect(url)
        else:
            account = session['account']
            user_video = Video.find_video(account)
            return render_template("favorite.html", user_video = user_video)
    else:
        return redirect("/login")
@app.route("/delete", methods=['POST'])
def delete_method():
    link = request.form['link']
    account = session['account']
    Video.delete(account, link)
    return redirect("/favorite")


@app.route("/download")
def download():
    value = request.args.get('value')
    download_type,url = value.split("&")
    print(download_type)
    print(url)
    if download_type=="MP3":
        rs.download_mp3(url)
        return render_template("download.html")
    elif download_type=="MP4":
        rs.download_mp4(url)
        return render_template("download.html")

if __name__ == "__main__":
    app.run(debug="False")