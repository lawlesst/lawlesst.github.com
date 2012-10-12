title:Django, Heroku, and the 360Link API
date:09-11-12
----

> This post describes a [demo application](http://damp-tor-3124.herokuapp.com/) that serves as a front-end to the [360Link OpenURL resolver](http://www.serialssolutions.com/en/services/360-link)
from Serials Solutions.  The code is available on [Github](https://github.com/lawlesst/heroku-360link) and the application is running on Heroku.    

A recent [thread](http://serials.infomotions.com/code4lib/archive/2012/201209/2516.html) on the Code4Lib mailing list discussed technical details of the [360Link ](http://www.serialssolutions.com/en/services/360-link) OpenURL resolver.  The technical details are interesting because the OpenURL resolver is often the last handoff from the library systems to the location on the web where users can actually get what they are looking for.  If something goes wrong, it's a frustating experience for everyone involved. 

Over the last year, my colleagues and I at Brown University Library have developed a new front-end to 360Link using the [360Link API](http://www.serialssolutions.com/en/services/360-search/xml-api).  It's been serving OpenURL requests since February and, as of August, has completely replaced our use of the default 360Link interface.  The main objective of this project was to streamline the delivery of content found in various databases.  

Since 360Link is rather popular in academic libraries and other libaries might be interested in implementing their own front-end, I decided to put together a demo [Django](https://www.djangoproject.com/) application that uses the API to create a basic link resolver.    

Here are a few sample links.  You can also paste an OpenURL into the form on the [index page](http://damp-tor-3124.herokuapp.com/)
 
 * [Sample article lookup](http://damp-tor-3124.herokuapp.com/?doi=doi/10.2202/1542-0485.1188)
 * [Pubmed lookup](http://damp-tor-3124.herokuapp.com/?pmid=22953657)
 * [JSON(P) responses](http://damp-tor-3124.herokuapp.com/?pmid=22953657&output=json) via content negotiation or adding output=json to the OpenURL. 
 * [Another sample response](http://damp-tor-3124.herokuapp.com/dl2af5jf3e/?pmid=22953657) but a customer code has been added to the url to switch to another library's API.  

You can easily switch libraries by adding another library's Serials Solutions customer code to the URL - e.g Brown's default 360Link interface is at http://rl3tp7zf5x.search.serialssolutions.com/ so the customer code is "rl3tp7z5x".  While testing this, I noticed that some library's API requires authentictation but most seem to be open and testable.  

To run some real requests through this app, you could login to [Mendeley](http://www.mendeley.com/) and set it as your resolver in the “Find this paper at” dropdown menu.   
  
The app is running on Heroku and the code is on [Github](https://github.com/lawlesst/heroku-360link).  As far as I know, any library that subscribes to 360Link also has access to the API, so you could checkout this code, make a few tweaks, and have it running for your library pretty quickly.  If you take a look, you'll notice that it's a couple of URL routes and a few dozen lines of controller (view in Django) code.  So it takes less work to get started with the API than you might suspect.  

For more details about working with the API, Daniel Talsky did a nice job of [explaining the API](http://journal.code4lib.org/articles/108) in Issue 4, 2008  of the Code4Lib Journal.    

At Brown we have seen some performance issues with the API, particularly with Pubmed ID lookups, but these issues are also present in the default interface too.  Overall it's been quite rewarding to have control over the link resolver interface and to dive in and add new features that make it easier for patrons to get to library content.  