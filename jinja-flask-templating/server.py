from flask import Flask, render_template
import random
from datetime import datetime

CURRENT_YEAR = datetime.now()
MY_NAME ="Sam"
app = Flask(__name__)

@app.route('/')
def home():
    current_year = CURRENT_YEAR.strftime("%Y")
    user_name = MY_NAME
    random_num = random.randint(1, 10)
    return render_template('index.html', num=random_num, cur_yr=current_year, usr_name=user_name)


if __name__ == "__main__":
    app.run(debug=True)
