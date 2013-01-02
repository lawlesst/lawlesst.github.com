title: Reading and writing RDF for VIVO with RDFAlchemy
date:1-2-13
----

For the last few months I have been working on converting a diverse set of data about the university and its faculty into RDF for import into [VIVO](http://www.vivoweb.org/), the semantic web application.  The workflow generally consists of mapping the incoming data to the VIVO ontology(s) and then writing a Python script to create the RDF necessary for loading into VIVO.  One of the tools I have begun using is [RDFAlchemy](https://rdfalchemy.readthedocs.org/en/latest/).  RDFAlchemy takes its lead from the Python SQL toolkit [SQLAlchemy](http://www.sqlalchemy.org/). It allows for "a object type API access to an RDF Triplestore."  What this means in practice is that you can create a set of classes for reading and writing RDF for VIVO.  Once your classes are created they can be reused down the line for future RDF reading, writing, and SPARQL queries.  

To demonstrate, I have created a basic FacultyMember class definition that models RDF for loading information about faculty into VIVO.  For sample data I am using the [people.csv](http://iweb.dl.sourceforge.net/project/vivo/Data%20Ingest/people.csv) file provided in the [VIVO Data Ingest Guide](http://iweb.dl.sourceforge.net/project/vivo/Data%20Ingest/Data_Ingest_Guide.pdf).[^outdated]  Each RDFAlchemy class definition has an RDF type assignment to identify the [RDF Class](http://en.wikipedia.org/wiki/RDF_Schema#Classes) that they object is linked to.  The remaining attributes, known as descriptors, are the specific [data or object properties](http://www.vivoweb.org/glossary/term/47) of the object.  The right hand side of the descriptor assignment includes whether the property is a single or repeating value (all single here) and the specific RDF property and namespace.  This will become the predicate in the outputted triples.  If you have worked with [Django models](https://docs.djangoproject.com/en/dev/topics/db/models/) or SQLAlchemy previously, this should seem quite familiar.  

[^outdated]:  The Data Ingest Guide is written for the VIVO 1.1 release.  The ontology may have changed a bit so please verify before reusing this snippet.  I have retained the data properties from the guide for clarity.  

~~~~{.python}

class FacultyMember(rdfSubject):
    rdf_type = core.FacultyMember
    label = rdfSingle(RDFS.label)
    firstname = rdfSingle(foaf.firstName)
    middlename = rdfSingle(core.middleName)
    lastname = rdfSingle(foaf.lastName)
    work_email = rdfSingle(core.workEmail)
    phone = rdfSingle(core.workPhone)
    fax = rdfSingle(core.workFax)
    research_overview = rdfSingle(core.researchOverview)
    preferred_title = rdfSingle(core.preferredTitle)
    moniker = rdfSingle(vitro.moniker)
    people_id = rdfSingle(local.peopleID)

~~~~

###Writing RDF

Now that the FacultyMember class is defined we can write RDF that we can load into VIVO.  The incoming data is in a CSV file and looks like this.   

~~~~{.csv}
person_ID,name,first,last,middle,email,phone,fax,title
3130,"Burks, Rosella ",Rosella,Burks,,BurksR@univ.edu,963.555.1253,963.777.4065,Professor 
3297,"Avila, Damien ",Damien,Avila,,AvilaD@univ.edu,963.555.1352,963.777.7914,Professor 
~~~~

Next we open and loop through the CSV file pulling out the values from cells and assigning them to our FaculyMember objects.   

~~~~{.python}

#Create a graph
g = rdfSubject.db

#Open the sample VIVO people file.
csv_url = 'http://iweb.dl.sourceforge.net/project/vivo/Data%20Ingest/people.csv'
people_file = urllib.urlopen(csv_url)
for count, row in enumerate(csv.DictReader(people_file)):
    #Create a URI for the person.
    person_uri = URIRef("%sfaculty%s" % (app, count + 1))
    #Instantiate a FacultyMember object using the URI created above. 
    fac = FacultyMember(person_uri)
    fac.label = row.get('name').strip()
    fac.people_id = row.get('person_ID')
    fac.moniker = row.get('title')
    fac.firstname = row.get('first')
    middle_name = row.get('middle')
    if middle_name is not None and middle_name != "":
        fac.middlename = row.get('middle')
    fac.lastname = row.get('last')
    fac.work_email = row.get('email')
    fac.phone = row.get('phone')
    fac.fax = row.get('fax')

print g.serialize(format='n3')
g.close()

~~~~

The output of the script should look like the following.  This file could be loaded directly into VIVO using the "Add/remove RDF" tool from the administrative page.  

~~~~{.python}
<http://localhost/vivo/faculty8> a core:FacultyMember;
    rdfs:label "Derek, Antoine Mccoy";
    local:peopleID "2561";
    vitro:moniker "Curator";
    core:middleName "Mccoy";
    core:workEmail "DerekA@univ.edu";
    core:workFax "963.777.5454";
    core:workPhone "963.555.2992";
    foaf:firstName "Antoine";
    foaf:lastName "Derek" .

<http://localhost/vivo/faculty9> a core:FacultyMember;
    rdfs:label "Hawkins, Callie";
    local:peopleID "1625";
    vitro:moniker "Professor";
    core:workEmail "HawkinsC@univ.edu";
    core:workFax "963.777.4949";
    core:workPhone "963.555.3350x6480";
    foaf:firstName "Callie";
    foaf:lastName "Hawkins" .

~~~~


###Reading RDF

The classes created for writing RDF with RDFAlchemy can also be helpful for extracting data from RDF.  For example, if you have exported a set of data from VIVO or retrieved it via a SPARQL query and now want to perform operations on it, the class definitions above will provide access to specific properties.  In the example below we load the [people.n3](http://iweb.dl.sourceforge.net/project/vivo/Data%20Ingest/people.n3) file from the [Data Ingest Guide](http://iweb.dl.sourceforge.net/project/vivo/Data%20Ingest/Data_Ingest_Guide.pdf) and filter it to show only those people who have the moniker "Assistant Professor".  The FacultyMember class, and all RDF Alchemy rdfSubject classes, has a method 'filter_by' which takes a descriptor and a value for querying.  

~~~~{.python}

#Load the n3 file as a rdfSubject db.
people_n3 = 'http://iweb.dl.sourceforge.net/project/vivo/Data%20Ingest/people.n3'
rdfSubject.db.load(people_n3, format='n3')
#Filter by all of the assistant professors in the graph.
asst_professors = FacultyMember.filter_by(moniker="Assistant Professor")
print '\n' + '=' * 20
print "Assistant Professors"
print '=' * 20 + '\n'
for fac in asst_professors:
    #Print full name, email, and url to vivo profile.
    print "%s\t%s\t%s" % (fac.label, fac.work_email, fac.resUri.toPython())
~~~~

The output of this script should look like below.  

~~~~{.python}
====================
Assistant Professors
====================

Quentin, Sam Hyde       QuentinS@univ.edu       http://localhost/vivo/faculty35
Mullins, Kimberly       MullinsK@univ.edu       http://localhost/vivo/faculty14
Chuck, Lloyd Haney      ChuckL@univ.edu http://localhost/vivo/faculty15

~~~~

Another class method 'get_by' is also available for retrieving single class instances.    

~~~~{.python}
#Use get_by to retrieve a single faculty member
faculty = FacultyMember.get_by(hr_id='3958')
print faculty.label
~~~~

###Wrap Up

The code below includes the snippets above and can be downloaded an run for testing.  RDFAlchemy is [available on PyPi](http://pypi.python.org/pypi/RDFAlchemy/) and also on [Github](https://github.com/gjhiggins/RDFAlchemy).  There are [other examples](https://github.com/gjhiggins/RDFAlchemy/tree/master/rdfalchemy/samples) in the Github repository that could be helpful for getting started.  

For the VIVO implementation work I am doing, I creating RDFAlchemy class definitions for other VIVO classes, like InformationResources, Events, Roles, Positions, etc.  If you are interested in those, please leave a note below. 

<div style="width: 800px; margin: 1em; padding:1em; font-size:1em;">
<script src="https://gist.github.com/4429683.js"></script>
</div>