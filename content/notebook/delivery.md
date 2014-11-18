Title:Focusing on Delivery
Date:09-30-12
Slug:delivery

A [Twitter exchange](https://twitter.com/hochstenbach/status/251929102024597504) between [Patrick Hochstenbach](https://twitter.com/intent/user?screen_name=hochstenbach) and [Rosemie Callewaert
](https://twitter.com/rcallewaert) voiced the opinion that library "discovery systems should focus more on delivery".  I agree - completely - and would like to describe some of the work I've been a part of recently that focuses on delivery of library content. 

At the Brown University Library, we have recently taken steps to improve the delivery of journal articles to library users.  We call the project easyArticle[^code].  When a user clicks on the 'Findit @Brown' link in various databases (including Google Scholar) or clicks the access link in our [Summon](http://www.serialssolutions.com/en/services/summon/) [front-end](http://library.brown.edu/find/Summon/Search?lookfor=learning+to+use+word+processors&type=AllFields&filter[]=holdingsOnly%3A%22false%22&view=list), she is routed through this system.  

In its most basic form, easyArticle is a front-end to the 360Link link resolver from Serials Solutions.  However it adds a fair amount of functionality beyond the typical link resolver.  The biggest addition to date is the automated submission of Interlibrary Loan and document delivery requests.  This along with the [easyBorrow](http://library.brown.edu/its/software/easyborrow/) project at Brown, which focuses on obtaining copies of books, consist of our "delivery" services.  

[^code]: Many of the components of this application are [available on Github](https://github.com/lawlesst) as separate Python modules.  I also [wrote previously](http://lawlesst.github.com/notebook/heroku360link.html) about building a demo application on Heroku that provides the basic functionality of this application. 

This screencast demonstrates a search in Google Scholar that leads to the user requesting an article via Interlibrary Loan through this application[^code].  Below the screencast is a list of user scenarios and how the easyArticle system is delivery the content to the user.    
<div style="width: 700px; margin: 1em; margin-left:auto; margin-right:auto; padding:1em;">
<iframe src="http://www.screenr.com/embed/B1a8" width="650" height="396" frameborder="0"></iframe>
</div>

###User scenarios for our easyArticle link resolver, or article delivery platform.

####Library has a license to an electronic version of the article or knows of an open access electronic copy of the article.

The user is [presented with link](http://library.brown.edu/easyarticle/get/eaB/) to the electronic version, much like most link resolvers.  Although this page is served by a locally developed web application so we have complete control over its appearance and content.  

####Library holds the print version of the article.

Students are presented with the location in the stacks of the item.  [Example](http://library.brown.edu/easyarticle/get/eaC/). This also uses a locally developed web service, called the [book locator](https://bitbucket.org/bul/book-locator), to give the user the exact floor and aisle location of the item.

Faculty can click a 'request' link that will create a document delivery request in Illiad.  Library staff will then retrieve the item from the stacks, scan it, and it will be delivered via the document delivery software. 

#### Library does not license an electronic copy of the article and does not hold a print copy of the article.

Users are offered a request link.  If the user is not authenticated, the user is prompted to login via the campus Shibboleth system.  After clicking a confirmation button, the request is submitted to Illiad.  

The library is a member of the [RapidILL](http://rapid2.library.colostate.edu/Public/AboutRapid) resource sharing network.  Requests that are available via this network are delivered to the users with 24 hours (Monday through Friday) of receipt.  If you aren't familiar with Rapid, there is more information in this [presentation](http://www.ilds2011.org/presentations/Delaney_RapidILL_ILDS2011_2011-09-19.pdf).  It's a great collaborative effort.  

Requests not available via Rapid are then processed through normal ILL procedures and documents are delivered directly via the Illiad software.  

#### Something goes wrong.

Unfortunately not all OpenURLs contain enough metadata or the holdings information in the knowledgebase isn't quite right and users can't get the article they are looking for.  In these instances, we offer users a simple problem report form that contains a link to the citation and their IP address that will help staff track down the problem.  This has led to speedier resolution of problems and a more centralized place to track problems and identify which platforms aren't working well with OpenURL.  

