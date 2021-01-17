Title:Connecting Python's RDFLib and Stardog
Date:11-06-14
Slug:rdflib-stardog

For a couple of years I have been working with the Python [RDFLib](https://github.com/RDFLib/rdflib) library for converting data from various formats to RDF.  This library serves this work well but it's sometimes difficult to track down a straightforward, working example of performing a particular operation or task in RDFLib.  I have also become interested in learning more about the commercial triple store offerings, which promise better performance and more features than the open source solutions.  A colleague has had good experiences with [Stardog](http://stardog.com/), a commercial semantic graph database (with a freely licensed community edition) from [Clark & Parsia](http://clarkparsia.com/), so I thought I would investigate how to use RDFLib to load data in to Stardog and share my notes.

A "SPARQLStore" and "SPARQLUpdateStore" have been included with Python's [RDFLib](https://github.com/RDFLib/rdflib) since version 4.0.  These are designed to allow developers to use the RDFLib code as a client to any SPARQL endpoint.  Since Stardog [supports SPARQL 1.1](http://docs.stardog.com/using/#sd-Querying), developers should be able to connect to Stardog from RDFLib in the similar way they would to other triple stores like [Sesame](http://rdf4j.org/) or [Fuseki](http://jena.apache.org/documentation/serving_data/).

### Setup Stardog
You will need a working instance of Stardog.  Stardog is available under a community license for evaluation after going through a simple registration process.  If you haven't setup Stardog before, you might want to checkout Geir Grønmo's [triplestores](https://github.com/grove/triplestores) repository where he has [Vagrant](https://www.vagrantup.com/) provisioning scripts for various triple stores.  This is how I got up and running with Stardog.

Once Stardog is installed, start the Stardog server with security disabled.  This will allow the RDFLib code to connect without a username and password.  Obviously you will not want to run Stardog in this way in production but it is convenient for testing.

```$./bin/stardog-admin server start --disable-security```

Next create a database called "demo" to store our data.

```$./bin/stardog-admin db create -n demo```

At this point a SPARQL endpoint is available at ready for queries at `http://localhost:5820/demo/query`.

### RDF

For this example, we'll add three skos:Concepts to a [named graph](http://en.wikipedia.org/wiki/Named_graph) in the Stardog store.

```turtle
	@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
	@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
	@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
	@prefix xml: <http://www.w3.org/XML/1998/namespace> .
	@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

	<http://example.org/n1234> a skos:Concept ;
	    skos:broader <http://example.org/b5678> ;
	    skos:preferredLabel "Baseball" .

	<http://example.org/b5678> a skos:Concept ;
	    skos:preferredLabel "Sports" .

    <http://example.org/n1000> a skos:Concept ;
    	skos:preferredLabel "Soccer" .
```

### Code
The complete example code here is available as a [Gist](https://gist.github.com/lawlesst/9996cf3050c019a8d5ee).


##### Setting up the 'store'

We need to initialize a [`SPARQLUpdateStore`](https://github.com/RDFLib/rdflib/blob/master/rdflib/plugins/stores/sparqlstore.py#L447) as well as a named graph where we will store our assertions.

```python
	from rdflib import Graph, Literal, URIRef
	from rdflib.namespace import RDF, SKOS
	from rdflib.plugins.stores import sparqlstore

	#Define the Stardog store
	endpoint = 'http://localhost:5820/demo/query'
	store = sparqlstore.SPARQLUpdateStore()
	store.open((endpoint, endpoint))

	#Identify a named graph where we will be adding our instances.
	default_graph = URIRef('http://example.org/default-graph')
	ng = Graph(store, identifier=default_graph)
```

#####Loading assertions from a file

We can load our sample turtle file to an in-memory RDFLib graph.

```python
	g = Graph()
	g.parse('./sample-concepts.ttl', format='turtle')

	#Serialize our named graph to make sure we got what we expect.
	print g.serialize(format='turtle')
```
Since our data is now loaded as an in memory Graph we can add it to Stardog with a SPARQL INSERT DATA operation.

```python
	ng.update(
	u'INSERT DATA { %s }' % g.serialize(format='nt')
	)
```

##### Use the RDFLib API to inspect the data

Using the RDFLib API, we can list all the Concepts in the Stardog that were just added.

```python
	for subj in ng.subjects(predicate=RDF.type, object=SKOS.Concept):
	    print 'Concept: ', subj
```

And, we can find concepts that are broader than others.

```python
	for ob in ng.objects(predicate=SKOS.broader):
	    print 'Broader: ', ob
```

##### Use RDFLib to issue SPARQL read queries.

RDFLib allows for binding a prefix to a namespace.  This makes our queries easier to read and write.

```python
	store.bind('skos', SKOS)
```

A SELECT query to get all the `skos:preferredLabel` for `skos:Concepts`.

```python
	rq = """
	SELECT ?s ?label
	WHERE {
	    ?s a skos:Concept ;
	       skos:preferredLabel ?label .
	}
	"""
	for s, l in ng.query(rq):
	    print s.n3(), l.n3()
```

##### Use RDFLib to add assertions.
The RDFLib API can also be used to add new assertions to Stardog.

```python
	soccer = URIRef('http://example.org/n1000')
	ng.add((soccer, SKOS.altLabel, Literal('Football')))
```

We can now Read statements about soccer using the RDFLib API, which issues the proper SPARQL query to Stardog in the background.

```python
	for s, p, o in ng.triples((soccer, None, None)):
	    print s.n3(), p.n3(), o.n3()
```

### Summary
With a little setup, we can begin working with Stardog in RDFLib in a similar way that we work with RDFLib and other backends.  The sample code here is included in this [Gist](https://gist.github.com/lawlesst/9996cf3050c019a8d5ee).