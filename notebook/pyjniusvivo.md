title:Using Python and Pyjinus to connect to Jena models
date:09-30-12
----

At [work](http://library.brown.edu/), I’m loading data into [Vivo](http://vivoweb.org/), an appplicaiton built with the [Jena Framework](http://jena.apache.org/) for building Semantic Web applications.  The Vivo web application comes with a nice set of bulk loading tools through an administrative interface.  However in the current Vivo release (1.5) there aren’t web services or other tools for performing operations programatically on the underlying Jena models, without of course working directly with the Vivo codebase.  There is a separate [harvester](https://github.com/vivo-project/VIVO-Harvester) project that has more utilities for getting data into the system.    

Here's a quick list of operations that we would like to be able perform via ingestion scripts:
 * generate a new, unique identifier to assign to new resources.  
 * find an existing resource in the model and return it's URI.  
 * load RDF created with processing scripts directly from those scripts. 
 * delete RDF created with processing scripts.  

A [recent post](http://news.ycombinator.com/item?id=4407624) on Hacker News pointed me to a project called [Pyjinius](http://pyjnius.readthedocs.org/en/latest/index.html), which is "a Python library for accessing Java classes".  

 * install Pyjinius and its dependencies.   
 * set your classpath to include the jars for the Jena.  

```
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
```

This approach is working well so far.  It allows us to continue to write our data manipulation scripts in a familiar language, Python, and but have the flexibility to call the Java classes when needed.  

Here is a [Gist](https://gist.github.com/3784363) with some real code that we are using in Vivo data loading scripts.  If you are interested in Pyjinius + Jena or Vivo, leave a note and we can discuss other uses for this approach.  