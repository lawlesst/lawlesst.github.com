Title: OrgRef data as RDF
Date: 01-10-2015
Slug: orgref-rdf
Summary: Notes on mapping [OrgRef](http://www.orgref.org/web/download.htm) to DBPedia and publishing with [Linked Data Fragments](http://linkeddatafragments.org/) .

This past fall, [Data Salon](http://www.datasalon.com/web/index.htm), a UK-based data services company, released an open dataset about academic and research organizations called [OrgRef](http://www.orgref.org/).  The data is [available as a CSV](http://www.orgref.org/web/download.htm) and contains basic information about over 30,000 organizations.

>OrgRef was created with publishers in mind, and so its main focus is on institutions involved with academic content: universities, colleges, schools, hospitals, government agencies and companies involved in research.

This announcement caught our attention at my place of work because we are compiling information about educational organizations in multiple systems, including a [VIVO](http://vivoweb.org) instance, and are looking for manageable ways to consume Linked Data that will enrich or augment our local systems.  Since the OrgRef data has been curated and focuses on a useful subset of data that we are interested in, it seemed to be a good candidate for investigation, even it isn't published as RDF.  Due to it's size, it is also easier to work with than attempting to consume and process something like [VIAF](http://viaf.org/) or [DBPedia](http://dbpedia.org) itself.

#Process
We downloaded the OrgRef CSV dataset and used the ever helpful [csvkit](https://github.com/onyxfish/csvkit) tool to get handle on what data elements exist.

```

$ csvstat --unique orgref.csv
  1. Name: 31149
  2. Country: 210
  3. State: 51
  4. Level: 3
  5. Wikipedia: 31149
  6. VIAF: 10764
  7. ISNI: 5765
  8. Website: 25910
  9. ID: 31149

```

The [attributes](http://www.orgref.org/web/help.htm) are will documented by OrgRef.  To highlight though, identifiers to other systems are included - Wikipedia Page ID (pageid), [ISNI](http://www.isni.org/), and [VIAF](http://viaf.org/).  These identifiers will be important for matching data from other systems or finding more LOD resources later.  There is also a link to official organizational home pages.  We've found that organizational home pages are surprisingly inconsistently available or not to an official page in other sources, so this is something from OrgRef that we would be interested in using right away.

##OrgRef to DBPedia
Since we are working on a project that uses RDF as the data model, we wanted to convert this OrgRef data from CSV to RDF.  All the organizations in the dataset (as of the December 2014 download) have Wikipedia page IDs (pageid).  DBPedia also includes the pageid so we can lookup the DBPedia URI for each and use that in our RDF representation of the data.  Rather that sending 30,000 SPARQL queries to DBPedia, we [downloaded](http://wiki.dbpedia.org/Downloads2014#page-ids) the DBPedia to pageid ntriples file from [DBPedia](http://wiki.dbpedia.org/Downloads2014#page-ids) and wrote a [script](https://github.com/lawlesst/vivo-sample-data/blob/master/orgref/orgref_to_dbpedia.py) to output another CSV with OrgRef ID and DBPedia URI pairs, like below.

```
orgref-id,uri
1859,http://dbpedia.org/resource/Arizona_State_University
2025,http://dbpedia.org/resource/Crandall_University
2236,http://dbpedia.org/resource/Acadia_University
3712,http://dbpedia.org/resource/Bell_Labs
3768,http://dbpedia.org/resource/Bundestag
```

##OrgRef as RDF

With a mapping of OrgRef IDs to DBPedia URIs we were able to create an RDF representation of each organization.  For an initial pass, we decided to only use name, pageid, ISNI, VIAF, and websites from OrgRef.  A script merged the original OrgRef CSV with our DBPedia URI to OrgRefID CSV and produced triples like the following for a single organization.

```
<http://dbpedia.org/resource/Michigan_Technological_University> a foaf:Organization ;
    rdfs:label "Michigan Technological University" ;
    dbpedia-owl:isniId "0000000106635937" ;
    dbpedia-owl:viafId "150627130" ;
    dbpedia-owl:wikiPageID "45893" ;
    schema:url "http://www.mtu.edu" .
```

The VIAF information is stored as both a string literal (to aid querying by the identifier later) and as an owl:sameAs relationship, since VIAF is published as Linked Data.  For ISNI, we are only storing the literal because, as of January 2015, isn't [available as Linked Data](http://lists.w3.org/Archives/Public/public-lod/2014Jun/0049.html).

##Publishing for querying with Linked Data Fragments.

With the OrgRef data model as RDF we, decided to use a [Linked Data Fragments](http://linkeddatafragments.org/) server to publish and query it.  LDF is a specification and software for publishing Linked Data datasets in way that minimizes server side requirements.  LDF data can be queried via SPARQL using a [client](https://github.com/LinkedDataFragments/Client.js) developed by the team or via HTTP requests.  [Ruben Verborgh](http://ruben.verborgh.org/), one of the researchers behind the LDF, has a posted a one minute [video](https://www.youtube.com/watch?v=fVvtuy6P248) with a clear summary of the motivations behind the effort.

Following the documentation for the [LDF server](https://github.com/LinkedDataFragments/Server.js), we setup an instance on [Heroku](https://www.heroku.com/) and loaded it with the OrgRef RDF file.  You can query this data at `http://ldf-vivo.herokuapp.com/orgref` with a [LDF client](https://github.com/LinkedDataFragments/Client.js) or browse it via the [web interface](http://ldf-vivo.herokuapp.com/orgref?subject=http://dbpedia.org/resource/Michigan_Technological_University).  Due to the design of the LDF server, we are able to publish and query this using a free Heroku instance.  See this [paper](http://ceur-ws.org/Vol-1268/paper3.pdf) for related, lightweight approaches.

##Summary
To wrap up, we found a quality, curated, and targeted dataset available as CSV that we would like to integrate into our local projects that use RDF.  Using the identifiers in the CSV file, we were able to match it to Linked Data URIs from DBPedia and create an RDF representation of it.  We also published the RDF via [Linked Data Fragments](http://linkeddatafragments.org/) for others to browse and query.

Our interest in the OrgRef data doesn't stop here though.  We want to make use of it on our local applications, particularly a [VIVO](http://vivoweb.org) instance.  I'll write more about that later.