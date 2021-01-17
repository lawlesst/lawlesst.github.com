#!/bin/bash
set -e
#build html
python freeze.py
#Move build to ghp branch
ghp-import -m "Update site" build
#Push build pages
git push -f origin gh-pages:master
#Push source too
git push origin write:write
