from flask import Flask, render_template
import requests



app = Flask(__name__)
response = requests.get("https://api.npoint.io/1b64453181a3840a4cf9")
all_posts = response.json()
print(all_posts)

@app.route('/')
def get_all_posts():
    return render_template("index.html",all_posts=all_posts)

@app.route('/home')
def home():
    return render_template("index.html",all_posts=all_posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)