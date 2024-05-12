from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['music']
collection = db['features']

@app.route('/')
def index():
    # Retrieve data from MongoDB
    songs = collection.find()

    # Pass data to template and render HTML
    return render_template('index.html', songs=songs)

if __name__ == '__main__':
    app.run(debug=True)
