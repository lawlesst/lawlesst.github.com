import os

from flask_frozen import Freezer

from app import app

os.environ["FLASK_ENV"] = "build"

freezer = Freezer(app)

@freezer.register_generator
def added_pages():
    yield "page", {"slug": "projects"}
    yield "page", {"slug": "presentations"}
    yield "page", {"slug": "baseballdb"}

if __name__ == '__main__':
    freezer.freeze()