from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from markupsafe import escape
from db import DictionaryDb


app = Flask(__name__)

app.config.from_pyfile('settings.py')
app.secret_key = 'super secret key'

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        d = DictionaryDb(refresh_db=False)
        session = d.create_db()
        d.insert_word(session, request.form["word"], request.form["meaning"])
        flash('New word added')

    return render_template("index.html")

@app.route('/words')
def words():
    d = DictionaryDb(refresh_db=False)
    session = d.create_db()
    words = d.get_words(session)
    return render_template('words.html', words=words)

@app.route('/word/<w>')
def word(w):
    app.logger.info(w)
    return 'Ali'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
