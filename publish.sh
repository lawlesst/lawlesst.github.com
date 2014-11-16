#!/bin/bash
set -e
#build html
pelican content -o output -s settings.py
#Move output to ghp branch
ghp-import output -m Update site
#Push output
git push origin gh-pages:master
#Push source too
git push origin pelican:pelican
