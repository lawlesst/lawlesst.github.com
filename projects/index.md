title:Projects
date:01-01-12
----
[TOC]

# Brown University
## easyArticle

Developed a [new link-resolver front end](http://library.brown.edu/easyarticle/get/eaT) to provide quick and easy access to library collections.  Uses various web APIs, including 360Link from Serials Solutions, Mendeley, JSTOR, and Microsoft Academic Search, to pull citation and access information as well as article abstracts and citing articles.  Wrote code to place requests in ILLiad, the library interlibrary loan system, on behalf of the user so that articles not in the library’s collection can be requested with one-click.  Developed export routine and indexing process to allow library print holdings to be available via OpenURL.  

## Vufind and Summon

Customized and implemented the open-source [library search](http://library.brown.edu/) front-end Vufind.  Developed code to index multiple sets of local content - digital collections, research guides, student dissertations - and integrated that content with standard library catalog data.  Developed record drivers to allow for custom display of various content types.  Developed export scripts for ILS and local repository systems to keep index up-to-date.  Customized the [Apache Solr](http://lucene.apache.org/solr/) schema to meet the library’s needs.  The project won a university-wide staff innovation award.  

## The Minassian Collection of Qur’anic Manuscripts

Ingested metadata and raw images for ancient Qur’anic manuscripts into the Brown Digital Repository.  Wrote scripts to create derivative images for access copies.  Worked with curator and metadata specialists to index MODS metadata in Apache Solr for [public search and browsing](http://library.brown.edu/cds/projects/quran) via a Django web application.  Implemented a sitemap to maximize the collection’s presence in search engines. 

##Library accessions and cataloging statistical reporting database
Worked with library departmental managers to develop a staff database to track accessions and cataloging activity in the library collections.  Coded custom logic for parsing MARC records and tabulating various statistical counts.  Developed ILS export routines to update the statistical database daily.  Implemented charts and CSV downloads of data to assist staff with analysis.  

##Book locator

Rewrote an existing application that provides users with a [specific floor and aisle location](http://library.brown.edu/find/Record/b5863423) for a given item in the library collections.  Included a web service that supports client-side integration so that the service can be easily integrated into other sites.  This system includes an administrative interface that allows library collections staff to maintain the database of call number locations.  Presented the project at the Innovative Interfaces Users Group meeting and shared the [code](https://bitbucket.org/bul/book-locator/overview) publicly.  

##New Titles at the library

Developed a Django-based, [Apache Solr](http://lucene.apache.org/solr/) powered facet [search application](http://library.brown.edu/titles) that highlights recent acquisitions in the library collections.  Modified and extended an open-source code base, Kochief.  Developed, in conjunction with technical services librarians, a customized MARC record parsing routine.  Implemented a Library of Congress call number normalization process that allows subject librarians to assign titles to university disciplines based off of the assigned call number.  

## Repository ingestion and indexing processeses
Adapted a Modified and maintained a complex set of Perl scripts that modify metadata and manipulate images for ingestion in to the library’s digital repository.   

##Time-off Recording System
Developed a Django application to allow staff and supervisors to manage vacation and sick time.  Built Javascript based timesheet that keeps a running total of staff.  Integrated external databases with organizational chart into local system to track and manage staff and supervisory relationships.  In coordination with Human Resources, developed business logic to handle university policies.  

# Columbia Law School
## Research Guides
Evaluated and implemented new content management system for [library research guides](http://library.law.columbia.edu/guides An_Introduction_to_African_Legal_Resources).  Developed customized theme to match institutional web presence.  Developed workflow for converting existing documents to new system and trained student to convert the guides.  Installed development and live versions of CMS (Mediawiki). 

## Hathi Trust and Open Library
Using APIs provided by the Hathi Trust and the Open Library, inserts 
links to full text public domain titles in [bibliographic records](http://pegasus.law.columbia.edu/record=b428691).  Relies completely on the APIs.  Requires no changes to the existing [bibliographic record](http://pegasus.law.columbia.edu/record=b309402).  Holdings are identified using the OCLC number.  A real time query is sent to the APIs as the page loads.  If the item isn't in the public domain, no link is displayed.  

## Offsite request form
Implemented a simplified and less error-prone [request process](http://pegasus.law.columbia.edu/record=b609702) for titles located in the library's offsite storage facility.  A request link is inserted next to the item barcode and patrons simply provide contact information.  Javascript transfers the necessary metadata from the record screen to the record request form.  Uses the [jQuery](http://jquery.com/) Javascript library.

## Text a call number
A Python-based web utility that allows patrons to [text a call number and location](http://pegasus.law.columbia.edu/record=b480398) to mobile phones.  Retrieves bibliographic information for the title using the [Majax](http://code.google.com/p/majax2/) library from Virginia Tech.  

## E-resources web page
Developed new layout and presentation for [electronic resources and database web page](http://library.law.columbia.edu/eresources/).  Users are allowed to filter results by area of law.  Online listing is updated by a nightly Python script that pulls data directly from the library's ERM system.  Uses the [Exhibit](http://simile-widgets.org/exhibit/) data presentation tools originally developed at MIT.

## New books list
Developed a more automated routine to display monthly lists of [new acquisitions](http://library.law.columbia.edu/newbooks/april2010.html).
Allows users to focuses on titles in particular subject areas or jurisdictions. 
Uses information exported from the ILS to determine which titles should appear on the list and assigns a jurisdiction based on call number.  Also uses [Exhibit](http://simile-widgets.org/exhibit/) for the presentation.

## Electronic bookplates
An [electronic form](http://pegasus.law.columbia.edu/record=b730730) of a traditional bookplate recognizing donated materials.  The tool inserts the plate as the page loads using a local note in the bibliographic record.  Also uses [jQuery](http://jquery.com/).
	
## Staff Wiki
Installed and manage a staff wiki for storing documentation, library procedures and guidelines.  Serves as the library's intranet.  Uses open-source Mediawiki platform.  Integrated with institutional LDAP service for ease of use.  Implemented automated backup routines and developed custom skin/theme.
	
## Batch record retrieval
Developed an ordering and processing routine that allows the library to automatically download bibliographic records, or 'copy cataloging'.  Uses a customized Z39.50 client written in Python.  Records are selected based
on library defined rules for record retrieval.

## Custom programming for technical services
Code various scripts to assist technical service staff with day-to-day functions.

- Examples: 
	- Custom claiming report for Chinese orders in native language.
	- Convert vendor provided spreadsheets into MARC bibliographic and order records that can be loaded into the ILS. 
	- Find duplicate and malformed barcodes in item records.
	- Match current journal holdings with titles available in a database.
	- Modify MARC records to insert URLs with proxy server.
	- Flag bibliographic records included in OCLC error reports for efficient processing.
