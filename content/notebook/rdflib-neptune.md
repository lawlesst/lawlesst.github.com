Title:Connecting Python's RDFLib to AWS Neptune
Date:03-15-19
Slug:rdflib-neptune

I've [written previously](http://lawlesst.github.io/notebook/rdflib-stardog.html) about using [Python's RDFLib](https://github.com/RDFLib/rdflib) to connect to various triple stores. For a current project, I'm using [Amazon Neptune](https://aws.amazon.com/neptune/) as a triple store and the RDFLib [SPARQLStore](https://rdflib.readthedocs.io/en/latest/apidocs/rdflib.plugins.stores.html#rdflib.plugins.stores.sparqlstore.SPARQLUpdateStore) implemenation did not work out of the box. I thought I would share my solution.

### The problem

Neptune returns ntriples by default and RDFLib, by default in version 4.2.2, is expecting CONSTRUCT queries to return RDF/XML. The solution is to override RDFLib's SPARQLStore to explictly request RDF/XML from Neptune via HTTP content negotiation.

Once this is in place, you can query and update Neptune via SPARQL with RDFLib the same way that you would other triple stores.

### Code

If you are interested in working with Neptune using RDFLib, here's a "NeptuneStore" and "NeptuneUpdateStore" implementation that you can use.

<script src="https://gist.github.com/lawlesst/091e0f4b0103320cfffa55dbe1757fb6.js"></script>





