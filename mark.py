"""
Generate static HTML from md files in tree.
"""
import datetime
import fnmatch
import glob
import os
import re
import sys
import time


import markdown
import PyRSS2Gen


#directories to scan
src_dirs = [
  '.',
  'projects',
  'notebook'
]


BASE = os.path.dirname(os.path.abspath(__file__))
BASE_URL = 'http://lawlesst.github.com'
template = open('template.html').read()


#For capturing title and dates
meta_re = re.compile('^(title\:)(.*)\n(date\:)(.*)\n(-*)', re.M)
#set date to blank text by default
str_post_date = ""
feed = []

#Twitter link for index page.
TWITTER = """<div><a href="https://twitter.com/tedlawless" class="twitter-follow-button" data-show-count="false">Follow @tedlawless</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
</div>"""


#build the html
for directory in src_dirs:
  sources = glob.glob('%s/*.md' % directory)
  for src_file in sources:
    d, fname = src_file.split(os.path.sep)
    print>>sys.stderr, d, fname
    txt = open(src_file).read()
    #Get the title marker
    match = meta_re.search(txt)
    if match:
      #Store the beginning and end of the matching text so we can remove it from the content later.
      match_start, match_end = match.span()
      title_field, title, date_field, post_date, delimiter = match.groups()
      title_marker = '%s%s' % (title_field, title)
      post_date = datetime.datetime.strptime(post_date.strip(), "%m-%d-%y")   
      str_post_date = datetime.datetime.strftime(post_date, "%m-%d-%y")
      print post_date
      #remove meta info
      txt = txt[match_end:]
    else: 
        field_label = ''
        title = ''
    #build the markdown
    content = markdown.markdown(unicode(txt, errors='ignore'), extensions=['toc'])
    #add the date
    html = template.replace('{{date}}', str_post_date)
    #if no date, remove pre element too
    if str_post_date == '':
      html = html.replace('<pre></pre>', '')
    #set the title if we have one
    if title == "":
      html = html.replace('{{title}}', '')
    else:
      html = html.replace('{{title}}', ' -- ' + title)

    #if we are in the root directory, adjust the media path
    if d == '.':
      html = html.replace('../media', './media')
      if fname == 'index.md':
        content += TWITTER

    #set the content
    html = html.replace('{{content}}', content)

    #write out to file.
    out_file = '%s/%s' % (directory, fname.replace('.md', '.html'))
    f = open(out_file, 'w')
    f.write(html)
    f.close()

    #store notebook files for rss
    if d == 'notebook':
      link = "%s/%s" % (BASE_URL, out_file)
      f = PyRSS2Gen.RSSItem(
        title = title,
        link = link,
        guid = link,
        description = content,
        pubDate = post_date,

      )
      feed.append(f)


#Generate the feed.
rss = PyRSS2Gen.RSS2(
    title = "Ted Lawless Notebook",
    link = BASE_URL,
    description = "Notes on projects.",
    lastBuildDate = datetime.datetime.utcnow(),
    items = feed
    )
rss.write_xml(open("feed.xml", "w"))

