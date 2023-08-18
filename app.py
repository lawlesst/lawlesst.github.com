"""
Flask Frozen app to generate HTML for github pages.
"""

import glob
import os
from datetime import datetime
from html.parser import HTMLParser

import dateparser
import markdown2
from bs4 import BeautifulSoup
from flask import Flask, make_response, render_template, url_for

app = Flask(__name__)

cwd = os.getcwd()
posts_dir = os.path.join(cwd, "content", "notebook")
pages_dir = os.path.join(cwd, "content", "pages")
is_deploy = os.getenv("env") == ""
link = "http://lawlesst.github.io/"

# see: https://stackoverflow.com/a/55825140/758157
class HTMLFilter(HTMLParser):
    text = ""

    def handle_data(self, data):
        self.text += data


def read_post(path):
    with open(path) as inf:
        title = next(inf).split(":")[1].strip()
        date = next(inf).split(":")[1].strip()
        slug = next(inf).split(":")[1].strip()
        md = inf.read()

    html = markdown2.markdown(md, extras=["footnotes", "fenced-code-blocks"])
    return {
        "title": title,
        "slug": slug,
        "date": date,
        "date_obj": dateparser.parse(date),
        "html": html,
    }


def index_posts():
    p = []
    for post in set(glob.glob(posts_dir + "/*.md")):
        details = read_post(post)
        if details not in p:
            p.append(details)
    sorted_posts = sorted(p, key=lambda x: x["date_obj"], reverse=True)
    return sorted_posts


@app.context_processor
def inject_datestamp():
    return dict(now=datetime.now().strftime("%m-%d-%Y %H:%M"))


@app.route("/")
def index():
    posts = index_posts()[:5]
    return render_template("index.html", recent_posts=posts)


@app.route("/archive")
@app.route("/archives.html")
def archive():
    posts = index_posts()
    return render_template("archive.html", recent_posts=posts)


@app.route("/notebook/<slug>.html")
def post(slug):
    post = read_post(os.path.join(posts_dir, f"{slug}.md"))
    return render_template("post.html", title=post["title"], date=post["date"], text=post["html"])


@app.route("/<slug>.html")
def page(slug):
    with open(f"{pages_dir}/{slug}.md") as inf:
        title = next(inf).split(":")[1]
        slug = next(inf).split(":")[1]
        md = inf.read()
    html = markdown2.markdown(md)
    return render_template("page.html", title=title, text=html)


@app.route("/feed.rss")
def rss():
    posts = index_posts()[:10]
    rss_posts = []
    for p in posts:
        try:
            f = HTMLFilter()
            f.feed(p["html"])
            p["description"] = ". ".join([f.strip() for f in f.text.split(". ")[:3]]) + "..."
        except AttributeError:
            p["description"] = None
        p["link"] = f"{ link }notebook/{ p['slug'] }.html"
        rss_posts.append(p)
    d = {
        "name": "Ted Lawless",
        "link": link,
        "description": "Work notebook",
        "feed_url": f"{link}/{url_for('rss')}",
        "pub_date": datetime.now(),
        "posts": rss_posts,
    }
    template = render_template("rss.xml.jinja2", **d)
    response = make_response(template)
    response.headers["Content-Type"] = "application/xml"
    return response
