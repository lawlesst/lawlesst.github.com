title:Django, Heroku, and the 360Link API
date:09-11-12
----

> This post describes a [demo application](http://damp-tor-3124.herokuapp.com/) that serves as a front-end to the [360Link OpenURL resolver](http://www.serialssolutions.com/en/services/360-link)
from Serials Solutions.  The code is available on [Github](https://github.com/lawlesst/heroku-360link) and the application is running on Heroku.    

A recent [thread](http://serials.infomotions.com/code4lib/archive/2012/201209/2516.html) on the Code4Lib mailing list discussed technical details of the [360Link ](http://www.serialssolutions.com/en/services/360-link) OpenURL resolver.  The technical details are interesting because the OpenURL resolver is often the last handoff from the library systems to the location on the web where users can actually get what they are looking for.  If something goes wrong, it's a frustating experience for everyone involved. 

Over the last year, my colleagues and I at Brown University Library have developed a new front-end to 360Link using the [360Link API](http://www.serialssolutions.com/en/services/360-search/xml-api) .  It's been serving OpenURL requests since February and, as of August, has completely replaced our use of the default 360Link interface.  The main objective of this project was to streamline the delivery of content found in various databases.  

Since 360Link is rather popular in academic libraries and other libaries might be interested in implementing their own front-end, I decided to put together a demo [Django](https://www.djangoproject.com/) application that uses the API to create a basic link resolver.    

You can use the application and test it out here.  

 * [Main page with form for OpenURL lookups](http://damp-tor-3124.herokuapp.com/)  
 * [Sample article lookup](http://damp-tor-3124.herokuapp.com/?url_ver=Z39.88-2004&url_ctx_fmt=info:ofi/fmt:kev:mtx:ctx&ctx_ver=Z39.88-2004&rfr_id=info:sid/mendeley.com/mendeley&rft_val_fmt=info:ofi/fmt:kev:mtx:journal&rft.genre=article&rft.date=2007&rft.volume=5&rft.issue=2&rft.pages=na&rft.atitle=Fuel Ethanol Subsidies and Farm Price Support&rft.jtitle=Journal of Agricultural Food Industrial Organization&rft.title=Journal of Agricultural Food Industrial Organization&rft.aulast=Gardner&rft.aufirst=Bruce&rft_id=info:doi/10.2202/1542-0485.1188&rft.issn=15420485)
 * [Pubmed lookup](http://damp-tor-3124.herokuapp.com/?pmid=22953657)
 * [JSONP responses](http://damp-tor-3124.herokuapp.com/?pmid=22953657&output=json) via content negotiation or adding output=json to the OpenURL.  
  
The app is running on Heroku and the code is on [Github](https://github.com/lawlesst/heroku-360link).  As far as I know, any library that subscribes to 360Link also has access to the API, so you could checkout this code, make a few tweaks, and have it running for your library pretty quickly.  If you take a look, you'll notice that it's a couple of URL routes and a few dozen lines of controller (view in Django) code.  It doesn't take much to get started with the API.  

The demo app uses a Python library we put together at Brown- [py360link](https://github.com/lawlesst/py360link) - for working with the 360Link API.  This is mostly repurposed from Godmar Back's [link360.py](http://code.google.com/p/link360/) which parses the API XML into a Python dictionary that can then be used in Django view and template code.  

You can easily switch libraries by adding another library's Serials Solutions customer code to the URL.  While testing this, I noticed that some library's seem to have their API behind a firewall but most seem to be wide open.  

  * Brown's default 360Link interface is at http://rl3tp7zf5x.search.serialssolutions.com/.  So our customer code is the odd string between http and search.  
  * The University of Michigan's link rsolver could be used for testing by adding their customer code to the.  See here [demo url](http://damp-tor-3124.herokuapp.com/dl2af5jf3e/?pmid=22953657)

To run some real requests through this app, you could login too [Mendeley](http://www.mendeley.com/) and set it as your resolver in the “Find this paper at” dropdown menu.   

Since Daniel Talsky did a nice job of explaining the API in Issue 4, 2008  of the Code4Lib Journal, Daniel Talsky [wrote](http://journal.code4lib.org/articles/108), I won't go into much detail here.  But, generally speaking, the API is pretty straightforward.  

At Brown have seem some performance problems , particularly with Pubmed ID lookups, but these performance issues are seen in the default interface too.  Overall it's been quite rewarding to have control over the link resolver interface and to dive in and add new features that make it easier for patrons to get to library content.  