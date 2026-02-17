from flask import Flask, render_template
import feedparser
app = Flask(__name__)

REDDIT_RSS = "https://www.reddit.com/r/football/top/.rss?t=day"

def fetch_reddit_feed(url=REDDIT_RSS):
    # feedparser is used to parse the RSS feed from Reddit 
    # good for fetching the latest posts
    feed = feedparser.parse(url)
    # this is a list of dictionaries, each representing a post
    items = []
    for e in feed.entries:
        items.append({
            "title": e.get("title"),
            "link": e.get("link"),
            "author": getattr(e, "author", "Reddit"),
            "published": getattr(e, "published", ""),
            "summary": getattr(e, "summary", ""),  # HTML snippet from Reddit
        })
    return items

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/blog")
def blog():
    posts = fetch_reddit_feed()
    return render_template("blog.html", posts=posts)

@app.route("/news")
def news():
    return render_template("table.html")

@app.route("/games")
def games():
    return render_template("games.html")

@app.route("/about")
def about():
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True, port=5000)