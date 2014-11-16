Title: Using Pelican for a Gitub personal page
Date: 11-16-2014
Slug: pelican
Summary: Notes on converting this Github user page based site to [Pelican](http://blog.getpelican.com/), a Python based static site generator.

I've been using my [Github user page](https://help.github.com/articles/user-organization-and-project-pages/#user--organization-pages) as a convenient way to publish [notes](../archives.html) about my [work](http://directory.brown.edu/uuid/2403c0a2-624f-a442-ee47-312376b77e3b). I choose GH personal pages over a service like Blogger or Wordpress because combining it with [Disqus](https://disqus.com/) for comments, allows for a lot of flexibility in how you write and arrange your content.

Up until this weekend I had used a somewhat clunky, [homemade Python script](https://github.com/lawlesst/lawlesst.github.com/blob/pre-pelican/mark.py) for converting Markdown to HTML, applying a template, and generating an RSS feed.  This has worked well but the script had to generate things like an RSS feed and list of all posts.  There are many nice [static site generation tools](https://www.staticgen.com/) available and at this point it makes sense for me to leverage one of those.  I chose [Pelican](http://blog.getpelican.com/) because of my experience with Python and Python's markdown library.  According to a site called [StaticGen](https://www.staticgen.com/), is the most popular Python based static site generation tool so made me choose it over the other Python based tools.

With a couple of hours of work I was able to convert my GH personal page to Pelican and was able to maintain my existing urls, Disqus comments, and Google Analytics code.  I was able to do this without writing any Python code, just by reading the Pelican docs, choosing and modifying a theme, changing the theme, and adjusting the site settings.  Overall it was a good experience.  Below are some specific notes that might help someone doing a project like this.  


###Specific notes

####Publishing to Github

Since Github treats your master branch as you static site content, you need to have your HTML files in the root directory.  Pelican expects to generate the HTML files to an `output` directory.  Initially I thought that I would have to use git to mv files around each time I wanted to publish new content.  Thankfully the the Pelican team has a concise set of [steps to follow](http://docs.getpelican.com/en/3.5.0/tips.html#user-pages) to support this workflow.  It uses [ghp-import](https://github.com/davisp/ghp-import) to copy the Pelican `output` directory to a `gh-pages` branch of your repository.  The next step is to push that branch to your Github personal repo as master.  I created a brief [publish script](https://github.com/lawlesst/lawlesst.github.com/blob/pelican/publish.sh) to automate this.  I keep the Pelican settings, content markdown, theme, etc in a separate Pelican branch and push that too to Github. 

####Preserving existing urls or naming your article pages
Since I had existing pages to convert, I used the `ARTICLE_SAVE_AS` [setting](http://docs.getpelican.com/en/latest/settings.html) to save articles with a slug filename that's added to the metata of each post/article rather than a date based, e.g. `2014/11/14/xxx.html', url.  This meant going back and adding the slug to 13 markdown files, not ideal but perserving the existing site urls was important to me.  Pelican's settings probably support doing something like this but I just went ahead and added the slug to each post's metadata. 

I was also able to easily change Pelican's auto-generated site feed file name, via the `FEED_RSS` setting, to match the feed name I have been using.

####Theming
There are many [themes](https://github.com/getpelican/pelican-themes) to choose from. I spent a fair amount of time trying out different themes, which was easy since appling a theme is as simple as changing a setttings file to point at the theme's location on the file system.  Since the themes use a [Jinja2](http://jinja.pocoo.org/docs/dev/) templates, I didn't have to learn a new syntax.  What few changes I needed to make were easy to apply.  The development server included with Pelican also allows you to run the server in the background, change content or themes in your text editor, and refresh your browser to see changes.  There were a few cases where changes I made didn't show up without restarting the development server so I added `LOAD_CONTENT_CACHE = False` to the Pelican settings file.  

####Support for common tools/features
Pelican's built in support for Disqus and Google Analytics made converting those tools to the new site really easy.  Just add `GOOGLE_ANALYTICS` and `DISQUS_SITENAME` to your Pelican settings file.  Many other common blog features, like tagging and blogrolls, are included with Pelican but I turned those off since I haven't been using them with my site and don't really want to.  It's nice to know that they exist though, particularly, tagging so that I can use them later if need be.    

####Outstanding issue
The Markdown TOC extensions seems to conflict with Pygments syntax highlighting.  I haven't been able to resolve this yet.  Since I'm only using a TOC on one page but using syntax highlighting in most articles, I decided this wasn't a blocker and just have turned off TOC generaton for now. 

