Title:Python and JSON-LD
Date:08-03-14
Slug:python-jsonld
----

I've published some [code](https://github.com/lawlesst/vivo-sample-data) for mapping CSV data to RDF using Python and JSON-LD on [Github](https://github.com/lawlesst/vivo-sample-data).  The motivation for this work was:

 1. to provide sample data to help people get started with [VIVO](http://www.vivoweb.org/), the research profile system built on Semantic Web standards
 2. to learn more about [JSON-LD](http://www.w3.org/TR/json-ld/) and explore it as a tool for assisting with the [Extract Transform Load (ETL)](http://en.wikipedia.org/wiki/Extract,_transform,_load) type work that's required for projects like VIVO.

Most people wanting to convert data to RDF will have access to relational data sources or tabular data exported as CSV or TSV files.  Using Python to read in a CSV source, convert it to a list of dictionaries using the standard library's [CSV module](https://docs.python.org/2/library/csv.html) and then map it RDF using a [JSON-LD context](http://www.w3.org/TR/json-ld/#the-context) can be really straightforward.  See the [context and code](https://github.com/lawlesst/vivo-sample-data/blob/master/positions.py#L20) for creating academic appointments in VIVO as example.

In a more real-world example, I've used a different [JSON-LD context](https://github.com/Brown-University-Library/vivo-data-management/blob/master/vdm/context.py#L18) to convert JSON data from Pubmed and CrossRef APIs to a local publication ontology.  Here, too, JSON-LD provides a nice way to map from multiple, slightly different sources, to a common RDF model.

There seems to be potential for a community working with RDF in a common ontology, like VIVO, to collaborate on developing common contexts for various data types and sharing and reusing them.  Members could use these contexts in a variety of tools and not be tied to a particular implementation (like Python) since the JSON can be read by nearly all programming languages.

The [RDFLib](https://github.com/RDFLib/) [plugin]((https://github.com/RDFLib/rdflib-jsonld)) for JSON-LD parsing and serializing is still undergoing development and the spec only became final in January of this year, so these are early days.  But I look forward to learning more about the spec and implementing it in other tools.