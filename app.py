
"""
Flask Frozen app to generate HTML for github pages.
"""


import glob
import os

from flask import Flask
from flask import render_template
from flask import url_for

import dateparser
import markdown2

app = Flask(__name__)

cwd = os.getcwd()
posts_dir = os.path.join(cwd, "content", "notebook")
pages_dir = os.path.join(cwd, "content", "pages")
is_deploy = os.getenv("env") == ""


def read_post(path, compile_html=True):
    with open(path) as inf:
        print(path)
        title = next(inf).split(":")[1].strip()
        date = next(inf).split(":")[1].strip()
        slug = next(inf).split(":")[1].strip()
        md = inf.read()

    if compile_html is True:
        html = markdown2.markdown(md, extras=["footnotes", "fenced-code-blocks"])
    else:
        html = None
    return {
        "title": title,
        "slug": slug,
        "date": date,
        "date_obj": dateparser.parse(date),
        "html": html
    }


def index_posts():
    p = []
    for post in glob.glob(posts_dir + "/*.md"):
        p.append(read_post(post, compile_html=False))

    print(p)
    sorted_posts = sorted(p, key=lambda x: x["date_obj"], reverse=True)
    return sorted_posts


@app.route('/')
def index():
    posts = index_posts()[:10]
    return render_template('index.html', recent_posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/archive')
@app.route('/archives.html')
def archive():
    posts = index_posts()
    return render_template('archive.html', recent_posts=posts)


@app.route('/notebook/<slug>')
@app.route('/notebook/<slug>.html')
@app.route('/post/<slug>')
def post(slug):
    with open(f"{posts_dir}/{slug}.md") as inf:
        title = next(inf).split(":")[1]
        date = next(inf).split(":")[1]
        slug = next(inf).split(":")[1]
        md = inf.read()
    html = markdown2.markdown(md, extras=["footnotes", "fenced-code-blocks"])
    return render_template('post.html', title=title, date=date, text=html)


@app.route('/<slug>.html')
def page(slug):
    with open(f"{pages_dir}/{slug}.md") as inf:
        title = next(inf).split(":")[1]
        slug = next(inf).split(":")[1]
        md = inf.read()
    html = markdown2.markdown(md)
    return render_template('page.html', title=title, text=html)


@app.route('/feed.rss')
def rss():
    with open(f"{pages_dir}/{slug}.md") as inf:
        title = next(inf).split(":")[1]
        slug = next(inf).split(":")[1]
        md = inf.read()
    html = markdown2.markdown(md)
    return render_template('page.html', title=title, text=html)