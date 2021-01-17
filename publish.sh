#!/bin/bash
set -e
#build html
python freeze.py
#Move output to ghp branch
ghp-import -m "Update site" output
#Push output
git push -f origin gh-pages:master
#Push source too
git push origin write:write
