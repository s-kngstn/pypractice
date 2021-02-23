from flask import Flask, render_template
import random
from datetime import datetime
import requests

CURRENT_YEAR = datetime.now()
MY_NAME ="Sam"
app = Flask(__name__)

@app.route('/guess/')
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

    age_res = requests.get("https://api.agify.io/", params=parameters)
    gender_res = requests.get("https://api.genderize.io/", params=parameters)

    age = age_res.json()['age']
    gender = gender_res.json()['gender']
    return render_template('name.html', age=age, gender=gender, name=name_here)

if __name__ == "__main__":
    app.run(debug=True)
