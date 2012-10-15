title:Citation Finder Demo
date:10-13-12
----

On October 11, [CrossRef](http://crossref.org/) [announced](http://labs.crossref.org/site/crossref_metadata_search.html) a new metadata search service and [API](http://search.labs.crossref.org/help/api).  One of the features of this new API is a service that will take an unstructed ciatation and attempt to resolve it to a DOI.  

As a proof of concept, I put together a [demo app](http://sleepy-island-6218.herokuapp.com/) that takes input from the users, sends it to this service, and if a DOI is found sends that DOI off to the 360Link link resolver API to find a full text link in a library.  

The code for the demo is [available on Github](https://github.com/lawlesst/citation-finder).  The server side code is minmial and build with [Flask](http://flask.pocoo.org/), the Python microframework for building web applications.  The bulk of the action takes place on the client side, using jQuery and jQuery templates.  Since the 360Link code we are calling supports JSONP, we can call it on the client side.

The user interface and interaction could certainly stand for some improvement but this work indicates to me that building a service like this for library users is feasible.  
