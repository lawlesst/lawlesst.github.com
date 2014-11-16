Title:An OpenRefine reconciliation service for academic journal data
Date:08-07-13
Slug:journaltoc-reconcile
----

Recently I've been working to link local data stored in [VIVO](http://vivoweb.org) as RDF with other sources on the Web.  The [RDF Refine extension](http://refine.deri.ie/docs) for [OpenRefine](http://openrefine.org/)[^refine] has been a useful tool in this work.  OpenRefine allows you to query a [reconciliation service](https://github.com/OpenRefine/OpenRefine/wiki/Reconciliation-Service-API) to match local strings to entities from another source and the RDF Extension allows for export as RDF.

Some of the data that I'm trying to interlink involves the work of university researchers and the venues in which their research is published.  The [JournalTOCs](http://www.journaltocs.ac.uk/about.php) project manged at [Heriot-Watt University](http://www.hw.ac.uk/) is a good source of metadata about academic journals and articles.  This resource aggregates table of contents information from over 22,000 journals.  The JournalsTOC service also kindly offers an [API](http://www.journaltocs.ac.uk/develop.php) for querying both article and journal metadata from their dataset.

Using a [demo reconciliation service](https://github.com/mikejs/reconcile-demo) developed by Michael Stephens as a model, I put together a basic reconciliation service for the JournalTOC data that queries the [JournalTOC API](http://www.journaltocs.ac.uk/develop.php) and translates the response to the format that OpenRefine is expecting.  The [code is available on Github](https://github.com/lawlesst/journaltocs-reconcile).  This service can be run locally and OpenRefine will query it just fine.  I have tested this with local data and it looks like a good option if you are working with similar data or interested in this work.

The URIs returned for publications are not quite [cool](http://www.w3.org/TR/cooluris/).  They are modeled after the URIs for journals that CrossRef makes available in its [RDF representation of DOIs](http://crosstech.crossref.org/2011/04/content_negotiation_for_crossr.html) domain, e.g http://id.crossref.org/issn/1059-9495, but can't yet be resolved to RDF representations.  I'm working out a better solution for this and will write about that when I have something to report.

[^refine]: OpenRefine was Google Refine until recently.  The latest released version is [Google Refine 2.5](http://openrefine.org/) and still carries the Google branding, which can be confusing.  A new release of Refine is being developed and that will be called OpenRefine.
