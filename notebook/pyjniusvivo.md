title:Using Python and Pyjnius to connect to Jena models
date:10-03-12
----

At [work](http://library.brown.edu/), I’m loading data into [Vivo](http://vivoweb.org/), an application built with the [Jena Framework](http://jena.apache.org/).  The Vivo web application comes with a nice set of bulk loading tools through an administrative interface.  However in the current Vivo release (1.5) there aren't web services or other tools for performing operations programatically on the underlying Jena models, without of course working directly with the Vivo codebase.  There is a separate [harvester](https://github.com/vivo-project/VIVO-Harvester) project that has more utilities for getting data into the system.    

Here's a quick list of operations on the Vivo model that we would like to be able perform via ingestion scripts:

 * generate a new, unique identifier to assign to new resources.  
 * find an existing resource in the model and return it's URI.  
 * load RDF created with processing scripts directly from those scripts. 
 * delete RDF created with processing scripts.  

A [recent post](http://news.ycombinator.com/item?id=4407624) on Hacker News pointed me to a project called [Pyjnius](http://pyjnius.readthedocs.org/en/latest/index.html), which is "a Python library for accessing Java classes."  

For the last couple of weeks, we have been using Pyjnius, with pretty good results.  We are able to write our ingestion scripts in Python, using [RDFLib](http://rdflib.readthedocs.org/en/latest/index.html), but still use the Jena and Vivo harvester classes when needed to connect to the existing data.  (See steps below for installing Pyjnius).  

I have included a couple of examples of how you might use Pyjnius to connect to a Jena database (in our case Vivo).  This [Gist](https://gist.github.com/3829194) contains some code that we are using in Vivo data loading scripts.  We are just beginning to explore the [Vivo harvester](https://github.com/vivo-project/VIVO-Harvester) in detail and hope to take fuller advantage of it moving forward.

If you are interested in Pyjnius + Jena or Vivo, leave a note and we can discuss other uses for this approach.  

### Example of connecting to an existing Jena database.  

~~~~{.python}
from jnius import autoclass

#Load java classes
#Database setup
DBConnection = autoclass('com.hp.hpl.jena.db.DBConnection')
LayoutType = autoclass('com.hp.hpl.jena.sdb.store.LayoutType')
DatabaseType = autoclass('com.hp.hpl.jena.sdb.store.DatabaseType')
SDBConnection = autoclass('com.hp.hpl.jena.sdb.sql.SDBConnection')
SDBFactory = autoclass('com.hp.hpl.jena.sdb.SDBFactory')
StoreDesc = autoclass('com.hp.hpl.jena.sdb.StoreDesc')

storeDesc = StoreDesc(LayoutType.LayoutTripleNodesHash, DatabaseType.MySQL)
conn = SDBConnection(DB_URL, DB_USER, DB_PASSWD)
store = SDBFactory.connectStore(conn, storeDesc)
dataset = SDBFactory.connectDataset(store)
model = dataset.getNamedModel('http://vitro.mannlib.cornell.edu/default/vitro-kb-2')

namespaces = model.listNameSpaces()
while namespaces.hasNext():
    print namespaces.next()

model.close()
store.close()
conn.close()
~~~~

The output for a default Vivo install should look something like the following:
~~~~
http://vitro.mannlib.cornell.edu/ns/vitro/public#
http://www.w3.org/1999/02/22-rdf-syntax-ns#
http://purl.org/NET/c4dm/event.owl#
http://purl.org/ontology/bibo/
http://xmlns.com/foaf/0.1/
http://www.w3.org/2002/07/owl#
http://purl.org/dc/terms/
http://vivoweb.org/ontology/core#
http://vitro.mannlib.cornell.edu/ns/vitro/0.7#
http://www.w3.org/2000/01/rdf-schema#
~~~~

#### Performing SPARQL queries
This example is closer to the operation of thing you might want to perform.  It executes a SPARQL select query on the Vivo model.  
~~~~{.python}
from jnius import autoclass

QueryFactory = autoclass('com.hp.hpl.jena.query.QueryFactory')
QueryExecutionFactory = autoclass('com.hp.hpl.jena.query.QueryExecutionFactory')
ResultSetFormatter = autoclass('com.hp.hpl.jena.query.ResultSetFormatter')
String = autoclass('java.lang.String')


storeDesc = StoreDesc(LayoutType.LayoutTripleNodesHash, DatabaseType.MySQL)
conn = SDBConnection(DB_URL, DB_USER, DB_PASSWD)
store = SDBFactory.connectStore(conn, storeDesc)
dataset = SDBFactory.connectDataset(store)
model = dataset.getNamedModel('http://vitro.mannlib.cornell.edu/default/vitro-kb-2')

query = """
PREFIX rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs:  <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:   <http://www.w3.org/2002/07/owl#>
SELECT ?thing ?label
WHERE
{
      ?thing rdf:type owl:Thing
      OPTIONAL { ?thing rdfs:label ?label } 
}
LIMIT 20
"""

query = QueryFactory.create(String(query))
qset = QueryExecutionFactory.create(query, model)
qexec = qset.execSelect()
results = ResultSetFormatter.toList(qexec).listIterator()

while True:
    if results.hasNext():
        next_result = results.next()
        uri = next_result.get('?thing').toString()
        label = next_result.get('?label').toString()
        print uri, label
    else:
        break

qset.close()
model.close()
store.close()
conn.close()
~~~~

#### Pyjnius Installation 
The [installation instructions](http://pyjnius.readthedocs.org/en/latest/installation.html) for Pyjnius are pretty straightforward.  I would recommend installing it with [virtualenv](http://pypi.python.org/pypi/virtualenv).  Below are the installation steps I took on an Ubuntu Server box but should be pretty similar on other platforms.  Make sure that you have a [JDK](http://en.wikipedia.org/wiki/Java_Development_Kit) installed. You will also want to make sure your [classpath](http://en.wikipedia.org/wiki/Classpath_(Java)) is set if you want to use external libraries.  

~~~~
vagrant@lucid32:~$ mkdir pyjnius-project
vagrant@lucid32:~$ cd pyjnius-project/
vagrant@lucid32:~/pyjnius-project$ virtualenv venv
New python executable in venv/bin/python
Installing setuptools............done.
Installing pip...............done.
(venv)vagrant@lucid32:~/pyjnius-project$ source venv/bin/activate
vagrant@lucid32:~/pyjnius-project$ pip install cython
Downloading/unpacking cython...
Successfully installed cython
Cleaning up...
(venv)vagrant@lucid32:~/pyjnius-project$ git clone git://github.com/kivy/pyjnius.git
Initialized empty Git repository in /home/vagrant/pyjnius-project/pyjnius/.git/
...
(venv)vagrant@lucid32:~/pyjnius-project$ cd pyjnius/
(venv)vagrant@lucid32:~/pyjnius-project/pyjnius$ python setup.py install
(venv)vagrant@lucid32:~/pyjnius-project/pyjnius$ cd ..
(venv)vagrant@lucid32:~/pyjnius-project/pyjnius$ python
Python 2.6.5 (r265:79063, Apr 16 2010, 13:09:56)
[GCC 4.4.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from jnius import autoclass
>>> Stack = autoclass('java.util.Stack')
>>> stack = Stack()
>>> stack.push('hello')
'hello'
>>> stack.push('world')
'world'
>>> stack.pop()
'world'
>>> stack.pop()
'hello'
>>> exit()
~~~~
