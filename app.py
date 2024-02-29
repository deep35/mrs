from flask import Flask, render_template, request
from MRS import search

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        music_preferences = request.form.get('music_preferences')
        music_recommendations = search(music_preferences)
        return render_template('index.html', music_recommendations=music_recommendations)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
