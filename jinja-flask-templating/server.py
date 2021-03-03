from flask import Flask, render_template
import random
from datetime import datetime
import requests

CURRENT_YEAR = datetime.now()
MY_NAME ="Sam"
app = Flask(__name__)

@app.route('/')
def home():
    current_year = CURRENT_YEAR.strftime("%Y")
    user_name = MY_NAME
    random_num = random.randint(1, 10)
    return render_template('index.html', num=random_num, cur_yr=current_year, usr_name=user_name)

@app.route('/guess/<name_here>')
def name(name_here):
    parameters = {
        "name": name_here,
    }

    age_data = requests.get("https://api.agify.io/", params=parameters)
    gender_data = requests.get("https://api.genderize.io/", params=parameters)

    age = age_data.json()['age']
    gender = gender_data.json()['gender']
    return render_template('name.html', age=age, gender=gender, name=name_here)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/dda847db0143e6f02e4d"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)



if __name__ == "__main__":
    app.run(debug=True)
