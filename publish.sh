#!/bin/bash
set -e
#build html
pelican content -o output -s settings.py
#Move output to ghp branch
ghp-import -m "Update site" output
#Push output
git push origin gh-pages:master
#Push source too
git push origin pelican:pelican
