#!/bin/bash
set -e

pelican content -o output -s settings.py
ghp-import output
git push origin gh-pages:master
