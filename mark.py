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
from PyRSS2Gen import RSSItem

BASE = os.path.dirname(os.path.abspath(__file__))
BASE_URL = 'http://lawlesst.github.com'
template = open('template.html').read()


#For capturing title and dates
meta_re = re.compile('^(title\:)(.*)\n(date\:)(.*)\n(-*)', re.M)
#set date to blank text by default
str_post_date = ""
feed = []
NOTEBOOK_DIR = 'notebook'
#directories to scan
src_dirs = [
  '.',
  'projects',
  NOTEBOOK_DIR
]

#Twitter link for index page.
TWITTER = """<div><a href="https://twitter.com/tedlawless" class="twitter-follow-button" data-show-count="false">Follow @tedlawless</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
</div>"""

DISQUS = """
<div id="disqus_thread"></div>
        <script type="text/javascript">
            /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
            var disqus_shortname = 'tedlawlessnotebook'; // required: replace example with your forum shortname

            /* * * DON'T EDIT BELOW THIS LINE * * */
            (function() {
                var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
                dsq.src = 'http://' + disqus_shortname + '.disqus.com/embed.js';
                (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
            })();
        </script>
        <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
        <a href="http://disqus.com" class="dsq-brlink">comments powered by <span class="logo-disqus">Disqus</span></a>
"""

from PyRSS2Gen import _element
class MyRSSItem(RSSItem):
  def __init__(self, content, *args, **kwargs):
    self.content = content
    super(MyRSSItem, self).__init__(*args, **kwargs)

  def publish_extensions(self, handler):
    """
    Could just put this in PyRSS2Gen since I've forked it anyway.  
    See content:encoded.
    https://developer.mozilla.org/en-US/docs/RSS/Article/Why_RSS_Content_Module_is_Popular_-_Including_HTML_Contents
    """
    content = self.content
    #_element(handler, "content:encoded", '<![CDATA[%s]]' % content)
    handler.startElement("content:encoded", self.element_attrs)
    handler.characters('<![CDATA[%s]]>' % content, skip=True)
    handler.endElement("content:encoded")
    #_element(handler, "content:encoded", content)


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
    #add the date for notebook pages
    if d == NOTEBOOK_DIR:
      html = template.replace('{{date}}', str_post_date)
    else:
      html = template.replace('{{date}}', '')
      html = html.replace('<pre></pre>', '')

    #set the title if we have one
    if title == "":
      html = html.replace('{{title}}', '')
    else:
      html = html.replace('{{title}}', ' -- ' + title)
      #for non notebook pages don't add the title to the h1
      #if d == NOTEBOOK_DIR:

    #if we are in the root directory, adjust the media path
    if d == '.':
      html = html.replace('../media', './media')
      if fname == 'index.md':
        content += TWITTER

    #set the content
    html = html.replace('{{content}}', content)

    if d == NOTEBOOK_DIR:
      #add disqus
      html += DISQUS

    #write out to file.
    out_file = '%s/%s' % (directory, fname.replace('.md', '.html'))
    f = open(out_file, 'w')
    f.write(html)
    f.close()

    #store notebook files for rss
    if d == NOTEBOOK_DIR:
      link = "%s/%s" % (BASE_URL, out_file)
      f = MyRSSItem(
        title = title,
        link = link,
        guid = link,
        description = '',
        pubDate = post_date,
        content = content,

      )
      feed.append(f)


#Generate the feed.
rss = PyRSS2Gen.RSS2(
    title = "Ted Lawless",
    link = BASE_URL,
    description = "Notes on projects.",
    lastBuildDate = datetime.datetime.utcnow(),
    items = feed
    )
rss.write_xml(open("feed.rss", "w"))

