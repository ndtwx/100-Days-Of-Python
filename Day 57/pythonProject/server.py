from datetime import datetime
from flask import Flask, render_template
import requests
import random

# AGIFY_URL = "https://api.agify.io?name={name}"
# GENDERIZE_URL = "https://api.genderize.io?name={name}"
app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<name>")
def guess(name):
    agify_response = requests.get(url=f"https://api.agify.io?name={name}")
    genderize_response = requests.get(url=f"https://api.genderize.io?name={name}")
    agify_data = agify_response.json()
    genderize_data = genderize_response.json()
    age = agify_data["age"]
    gender = genderize_data["gender"]
    return render_template("guess.html", name=name, gender=gender, age=age)


@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
