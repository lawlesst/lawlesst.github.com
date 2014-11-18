Title:A utility script for developing VIVO custom list views 
Date:03-18-13
Slug:vivo-listview

As you continue with your [VIVO](http://www.vivoweb.org/) implementation, you might want to adjust the properties that are displayed on profile pages.  VIVO handles what properties display on a profile page through a set of list views, which are SPARQL queries that pull data from your VIVO store and pass it on to [Freemarker](https://wiki.duraspace.org/display/VIVO/FreeMarker) templating system. 

To speed up the development of these SPARQL queries, my colleague and I put together a [Python script](https://gist.github.com/lawlesst/5192700) to simulate what VIVO does when it reads a list view and queries the RDF models for data.  The script, called [generate_listview.py](https://gist.github.com/lawlesst/5192700), parses the VIVO XML based list view config files ([example](https://github.com/vivo-project/VIVO/blob/develop/productMods/config/listViewConfig-awardOrHonor.xml)) and queries VIVO via SPARQL to retrieve the data and display it to the terminal.  This eliminates the need to edit the list view config files on the server and reload pages, and all of the profile data, to see if your query is doing what you expect.  This workflow allows you to build a custom list view separately and then copy the finished the list view config XML file to the server when you are more confident that it is retrieving the data that you want it to.  

A script like this isn't necessary for developing custom list views but we have found it to be useful and makes us a bit more productive.  You can run these queries in the browser using the built-in SPARQL query interface.  However, the list views use a pattern of creating a new graph via SPARQL CONSTRUCT queries and then running a final SELECT query against the constructed graph, which is hard, if not impossible, to simulate in the browser.  This script will simulate that flow and allow you to see all the actions in one step as you run the query.  

Since this script is not exactly the same as what VIVO does when you load a profile in your browser, you will likely encounter aspects of list views that it doesn't handle well.  For example, you won't be able to use ARQ functions in the final SELECT query, since it's executed with RDFLib rather than VIVO.  But overall this could be a convenient tool to have available.  We think it is.  

#### Getting started

 * [Download the scripts](https://gist.github.com/lawlesst/5192700) and place them in a directory. 

 * Install required Python modules.  

~~~~
$ pip install git+git://github.com/RDFLib/rdflib-sparql.git
$ pip install SPARQLWrapper
$ pip install requests
~~~~

  * Run the list view generator by passing it an existing list view config file.
~~~~
$ python generate_listview.py /path/to/listViewConfig-awardOrHonor.xml
~~~~

  * View the output in the terminal.  Adjust the listViewConfig.xml file and rerun until it meets your needs.   

#### Other resources
 * The [list view documentation](https://github.com/vivo-project/VIVO/blob/develop/doc/list_view_configuration_guidelines.txt) included with VIVO covers the list view process in more detail.  

 * A [presentationn](http://www.vivoweb.org/files/presentations/12ws3/Cooks_tour.pdf) from the 2012 VIVO conference details possible approaches to customizing VIVO.


