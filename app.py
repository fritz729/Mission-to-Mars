from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#home route
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scraping():
    mars = mongo.db.mars
    mars_data = scrape.scrape_all()
    mars.update_many({}, {'$set': mars_data}, upsert=True, array_filters=None)
    return redirect('/', code=302)

if __name__ == "__main__":
    app.run()
