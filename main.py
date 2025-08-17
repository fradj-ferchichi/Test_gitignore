from modules import *
from getname import random_name



@app.route("/")
def hello_world():
    return f"<h1>Behold, I am {random_name('superhero')}!</h1>"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
