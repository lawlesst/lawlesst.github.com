title: A Python module for placing requests in ILLiad 
date:12-31-12
----

> This post describes a [Python module](https://github.com/lawlesst/illiad-api) for creating requests in [ILLiad](http://www.atlas-sys.com/illiad/), the interlibrary loan software used in libraries.  

Many libraries use [ILLiad](http://www.atlas-sys.com/illiad/) as the software system for document delivery and interlibrary loan services.  As a developer working with this system, you might find a need to create ILLiad requests programmatically from another system.  This other system could be your library catalog or OpenURL resolver or just a standalone script that processes batches of requests.  However ILLiad doesn't support an API for creating requests.  In response to this, at [Brown University Libraries](http://library.brown.edu) we have developed a Python module that serves as a programming interface to ILLiad.  The code for the module is [available on Github](https://github.com/lawlesst/illiad-api) for downloading, forking, and inspection.  It relies on two Python libraries, [requests](http://docs.python-requests.org/en/latest/) for creating HTTP requests and [pyquery](http://packages.python.org/pyquery/), which provides a nice syntax for parsing HTML documents.

###Request workflow
This is the basic worfklow for the module:

 * authenticate or verify the user in your external system.  
 * establish an ILLiad session on behalf of the user.  Retain the returned session cookie for further requests.
 * pass an OpenURL to ILLiad for the item the user is requesting.
 * parse the response, which is an HTML form with populated values from the OpenURL.  If you were doing this manually from the ILLiad user interface, this would be the pre-populated form that the user sees and either enhances with more information or clicks submit to process.  
 * post the values returned by the step above to the ILLiad server. 
 * parse the response.  This will response will contain either an error message or the transaction number for the request.  
 * log the user out.    

###Example in code
<div style="width: 800px; margin: 1em; padding:1em;">
<script src="https://gist.github.com/4422229.js"></script>
</div>

###How does the module work? 
ILLiad ships with a set of web forms that will respond to [OpenURL](http://en.wikipedia.org/wiki/OpenURL) requests and pre-populate forms with the appropriate data.  This module will complete the ILLiad web forms and submit requests on users' behalf.  The module is made possible by opening ILLiad web pages on a user's behalf, parsing the responses, and posting values to the ILLiad server.

The library does rely on screen scraping the HTML returned by the ILLiad application but experience has shown that this method is quite stable and robust enough to be used in production systems.  Versions of this library have been in place at Brown for four years or more and have processed over 10,000 user requests during the last six months.  One of the common problems encountered when relying on screen scraping to provide functionality is that the HTML can change without notice.  In this case the ILLiad software is managed by the library so the chances of it changing without notice is small.  As an extra measure to protect against unforeseen HTML changes, we have place the HTML pages that are used with this library on a different web path than the user pages (something like http://illiad.school.edu/api-pages/) so that we can update the user pages without changing the markup that this library relies on.  

The module as implemented relies on the [RemoteAuth](https://prometheus.atlas-sys.com/display/illiad/RemoteAuth+Authentication) in ILLiad.  This allows users to be authenticated via an HTTP header and can be used with systems like [Shibboleth](http://en.wikipedia.org/wiki/Shibboleth) or [CAS](http://en.wikipedia.org/wiki/Central_Authentication_Service).  The module will pass the appropriate header for authentication and save the session cookie for further requests.  This also eliminates the need to store the user's ILLiad credentials in a local database, which could be seen as a security risk.  If this is not a concern for your project, you could use a modified version of this library without enabling the RemoteAuth functionality.  Leave a comment below if you would like some help in getting started with that.  

###Example in video
The screencast below shows an example of this library being integrated into the library's OpenURL resolver.  The user in this example authenticates with the campus Shibboleth system and places a request in ILLiad directly from the resolver interface.  There is no need to visit ILLiad to place the request.  
<div style="width: 700px; margin: 1em; padding:1em;">
<iframe src="http://www.screenr.com/embed/B1a8" width="650" height="396" frameborder="0"></iframe>
</div>

If you are interested in learning more about this project or run into problems when getting started with the library, please leave a comment below and I will get back to you.  