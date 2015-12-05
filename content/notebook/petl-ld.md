Title:Python ETL and JSON-LD
Date:12-05-15
Slug:petl-ld

I've written an [extension](https://github.com/lawlesst/petl-ld) to [petl](https://petl.readthedocs.org/en/latest/), a Python ETL library, that applies JSON-LD contexts to data tables for transformation into RDF.

### The problem

Converting existing data to RDF, such as for [VIVO](http://vivoweb.org), often involves taking tabular data exported from a system of record, transforming or augmenting it in some way, and then mapping it to RDF for ingest into the platform. The W3C maintains an [extensive list](http://www.w3.org/wiki/ConverterToRdfSome) of tools designed to map tabular data to RDF.

General purpose CSV to RDF tools, however, almost always require some advanced preparation or cleaning of the data. This means that developers and data wranglers often have to write custom code. This code can quickly become verbose and difficult to maintain. Using an [ETL](https://en.wikipedia.org/wiki/Extract,_transform,_load) toolkit can help with this.

### ETL with Python

One such ETL tool that I'm having good results with is [petl](https://petl.readthedocs.org/en/latest/), Python ETL. [petl](https://petl.readthedocs.org/en/latest/) started at an informatics group at the University of Oxford and is maintained by [Alistair Mles](http://www.well.ox.ac.uk/alistair-miles). It has clear [documentation](https://petl.readthedocs.org/en/latest/) and is available under an open license.

petl provides adapters for reading data from a variety of sources - csv, Excel, databases, XML - and many utilities for cleaning, transforming, and validating. For example adding a column of static values to a petl table is as simple as:

```python
etl.addfield(table1, 'type', 'person')
```

### petl and JSON-LD for RDF

petl, however, doesn't have utilities for outputting tables to RDF. To add this functionality, I've written a small extension, called [petl-ld](https://github.com/lawlesst/petl-ld), to use [JSON-LD](http://www.w3.org/TR/json-ld/#the-context) contexts to map petl's table data structure to RDF. This allows the developer to clean, enhance, and validate the incoming data with petl functionality and patterns - and then, as a final step, apply a JSON-LD context to create an RDF serialization.

The JSON-LD transformation utilizes the [rdflib-jsonld](https://github.com/RDFLib/rdflib-jsonld) extenstion to RDFLib maintained by [Niklas Lindström](https://github.com/niklasl).

Here is an example:

~~~
import petl as etl
import petlld

# set up a petl table  to demonstrate
table1 = [['uri', 'name'],
          ['n1', "Smith, Bob"],
          ['n2', "Jones, Sally"],
          ['n3', "Adams, Bill"]]

# use petl utilities to add a column with our data type - foaf:Person
table2 = etl.addfield(table1, 'a', 'foaf:Person')

# a JSON-LD context for our data
ctx = {
    "@base": "http://example.org/people/",
    "a": "@type",
    "uri": "@id",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "name": "rdfs:label"
}

# serialize the data as
table2.tojsonld(ctx, indent=2)
~~~

The JSON-LD output:

```json
{
   "@context":{
      "a":"@type",
      "foaf":"http://xmlns.com/foaf/0.1/",
      "name":"rdfs:label",
      "rdfs":"http://www.w3.org/2000/01/rdf-schema#",
      "uri":"@id",
      "@base":"http://example.org/people/"
   },
   "@graph":[
      {
         "a":"foaf:Person",
         "uri":"n1",
         "name":"Smith, Bob"
      },
      {
         "a":"foaf:Person",
         "uri":"n2",
         "name":"Jones, Sally"
      },
      {
         "a":"foaf:Person",
         "uri":"n3",
         "name":"Adams, Bill"
      }
   ]
}
```

If you would rather output an [RDFLib](https://github.com/RDFLib/rdflib) [Graph](https://rdflib.readthedocs.org/en/stable/intro_to_graphs.html) for serialization in another format, that is possible too.

~~~python
graph = table2.tograph(ctx)

print graph.serialize(format='turtle')
~~~

The [turtle](http://www.w3.org/TR/turtle/) output:

```turtle
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://example.org/people/n1> a foaf:Person ;
    rdfs:label "Smith, Bob" .

<http://example.org/people/n2> a foaf:Person ;
    rdfs:label "Jones, Sally" .

<http://example.org/people/n3> a foaf:Person ;
    rdfs:label "Adams, Bill" .
```

### Summary

If you are working with Python and converting tabular data to RDF, take a look at [petl-ld](https://github.com/lawlesst/petl-ld)) and see if it helps you write less, more readable code. Feedback is welcome.


