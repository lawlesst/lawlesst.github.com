from flask_frozen import Freezer
from app import app

import os

os.environ["FLASK_ENV"] = "build"

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()