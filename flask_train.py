from flask import Flask
from flask import redirect, url_for , render_template
app = Flask(__name__)

@app.route("/")
@app.route("/<string:username>")
def hello(username=""):
    return render_template('hello.html', name=username)

# @app.route("/hey_hey_hey")
# # def hey_hey_hey():
#     return redirect(url_for('ha'))


@app.route("/he")
def ha():
    return("hee")





# @app.route('/')
# def index():
#     return redirect(url_for('login'))

# @app.route('/login')
# def login():
#     abort(401)
#     this_is_never_executed()

if __name__=='__main__':
    app.run()