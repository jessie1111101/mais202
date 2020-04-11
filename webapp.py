from flask import Flask, redirect, url_for, render_template, request
from book_recommendation_generator import corpus_recommendations

app = Flask(__name__)

def add(n):
    new = n + "hi"
    return new

#give app a route / means default domain
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/sign')
def sign():
	return render_template('sign.html')

@app.route('/process', methods=['POST'])

def process():
	name = request.form['name']
	comment = request.form['comment']

	return render_template('index.html', name=corpus_recommendations(name), comment=comment)

@app.route('/home', methods=['GET', 'POST'])
def home():
	links = ['https://www.youtube.com', 'https://www.bing.com', 'https://www.python.org', 'https://www.enkato.com']
	return render_template('example.html', links=links)

if __name__ == "__main__":
    app.run(debug=True)
