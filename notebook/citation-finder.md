title:Free text citations to library content
date:10-17-12
----

On October 11, [CrossRef](http://crossref.org/) [announced](http://labs.crossref.org/site/crossref_metadata_search.html) a new metadata search service and [API](http://search.labs.crossref.org/help/api).  Jonathan Rochkind, as usual, has a nice [writeup](http://bibwild.wordpress.com/2012/10/11/new-crossref-metadata-search-with-api/) on the possibilities of integrating such a service with library software.  Jonathan writes the following in reference to the "links" feature which will take an unstructured citation and attempt to resolve it to a DOI: 

>Looks like they also have an API for submitting a free-form citation, and getting back matches with DOI!  It’s sort of a ‘holy grail’ for me to provide a service where users can paste in a free-form citation, and get to our access/delivery options.

I've been doing a lot of work with [delivery](./delivery.html) services myself lately and see the value in being able to match raw text citations to actual content the library has licensed.  So I took Jonathan's statement as a bit of a challenge and an opportunity to explore the CrossRef API.  

The result is a [demo application](http://sleepy-island-6218.herokuapp.com/) that takes input from users, sends it to the CrossRef service, and, if a DOI is found, sends that DOI off to the [360Link](http://www.serialssolutions.com/en/services/360-link) link resolver API to find a full text link in a library.  The screencast below shows two examples. 

<iframe src="http://www.screenr.com/embed/itV8" width="650" height="396" frameborder="0"></iframe>

The code for the demo is [available on Github](https://github.com/lawlesst/citation-finder).  The server side code is minimal and built with [Flask](http://flask.pocoo.org/), the Python microframework for building web applications.  The bulk of the action takes place on the client side, using jQuery and jQuery templates.  The user interface and interaction could certainly stand for some improvement and the citations that are resolvable are limited to what's in but this work indicates building a service like this for library users is feasible, or at least getting there.  

CrossRef apparently [doesn't parse](http://labs.crossref.org/quick_and_dirty_api_guides/resolving_citations.html) the free text into a formatted citation but constructs a query based on the free text against their database.  For further development, it would be nice to try a similar approach with the [Summon API](http://api.summon.serialssolutions.com/) and see if it could be possible to build a similar service on top of that data, since it contains a larger set of publications and articles.  

If you are short on citations to try, here are a few I pulled from dissertations.  The third citation is to a working paper and doesn't resolve to a DOI via CrossRef so the interface offers a link to a search in Google Scholar, which does return a [PDF to the paper](http://neeo.univ-tlse1.fr/294/1/collard_dellas.pdf).  

    Christiano, L. J., M. Eichenbaum, and C. L. Evans (2005): “Nominal Rigidities and the Dynamic Eﬀects of a Shock to Monetary Policy,” Journal of Political Economy, 113(1), 1—45.
    
    Clarida, R., J. Gali, and M. Gertler (1999): “The Science of Monetary Policy: A New Keynesian Perspective,” Journal of Economic Literature, 37(4), 1661—1707.
    
    Collard, F., and H. Dellas (2004): “The new Keynesian model with imperfect information and learning,” Working Paper, University of Toulouse.
    
Another item to note is that you can append a library's Serials Solutions code to the URL and the demo will search holdings for that library.  For example, this link will search the [University of Victoria](http://sleepy-island-6218.herokuapp.com/lg5jh7pa3n/) holdings.  John Durno of Victoria has an [article](http://journal.code4lib.org/articles/7308) in the most recent Code4Lib journal on some of their recent delivery work.  
 
