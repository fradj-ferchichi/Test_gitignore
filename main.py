from modules import *
from getname import random_name



@app.route("/")
def hello_world():
    return f"<h1>Behold, I am {random_name('superhero')}! <i>Haha Haha!<i></h1>"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
