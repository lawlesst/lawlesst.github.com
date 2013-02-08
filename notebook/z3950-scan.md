title:Using Z39.50 to produce a Stack View.  
date:02-08-13
----

The [Harvard Library Innovation Lab](http://librarylab.law.harvard.edu/) has developed a library brosing tool called [Stack View](http://librarylab.law.harvard.edu/blog/stack-view/).  It provides a way to virtual browse through a collection of items from a library.   

The examples on the Stack View website show how to pull data in from a variety of sources and example scripts are provided.  But many libraries might want to pull data in from their own catalog.  Additionally libraries might want to display the items in call number order so that the virtual Stack View approximates what a user would see if they were actually browsing the shelves in your library.

One way to get the data necessary for Stack View is via [Z39.50](http://en.wikipedia.org/wiki/Z39.50).  Below is an example of a Stack View for "On the Road" by Jack Kerouac from the Brown University library catalog.  

<!-- stackview.css to style the stack -->
<link rel="stylesheet" href="http://librarylab.law.harvard.edu/projects/stackview/demo/lib/jquery.stackview.css" type="text/css">
 
<!-- stackview.js and all js dependencies -->
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.min.js"></script>
<script type="text/javascript" src="http://librarylab.law.harvard.edu/projects/stackview/demo/lib/jquery.stackview.min.js"></script>
 
<div id="stackview" title="Sample Stack View" style="margin: 2em; "></div>
    
<script type="text/javascript">
    var data = {
  "start": "-1", 
  "num_found": 40, 
  "limit": 50, 
  "docs": [
    {
      "callnumber": "PS3521.E716 D6 1987", 
      "link": "http://library.brown.edu/find/Record/b3168718", 
      "measurement_page_numeric": 245, 
      "creator": [
        "Kerouac, Jack, 1922-1969."
      ], 
      "measurement_height_numeric": 21, 
      "items": 1, 
      "title": "Doctor Sax :Faust part three /", 
      "pub_date": "1987", 
      "id": "b3168718", 
      "shelfrank": 10
    }, 
    {
      "callnumber": "PS3521.E716 E9", 
      "link": "http://library.brown.edu/find/Record/b1438756", 
      "measurement_page_numeric": 128, 
      "creator": [
        "Kerouac, Jack, 1922-1969."
      ], 
      "measurement_height_numeric": 22, 
      "items": 1, 
      "title": "Excerpts from Visions of Cody.", 
      "pub_date": "1959", 
      "id": "b1438756", 
      "shelfrank": 10
    }, 
    {
      "measurement_page_numeric": 605, 
      "creator": [
        "Kerouac, Jack, 1922-1969."
      ], 
      "items": 2, 
      "title": "On the road /", 
      "callnumber": "PS3521.E716 O5 1979", 
      "link": "http://library.brown.edu/find/Record/b1102953", 
      "shelfrank": 50, 
      "measurement_height_numeric": 20, 
      "pub_date": "1979", 
      "id": "b1102953"
    }, 
    {
      "callnumber": "PS3521.E716 O77x 2002", 
      "link": "http://library.brown.edu/find/Record/b3238455", 
      "measurement_page_numeric": 176, 
      "creator": [
        "Kerouac, Jack, 1922-1969."
      ], 
      "measurement_height_numeric": 21, 
      "items": 1, 
      "title": "Orpheus emerged /", 
      "pub_date": "2002", 
      "id": "b3238455", 
      "shelfrank": 10
    }, 
    {
      "callnumber": "PS3521.E716 T6", 
      "link": "http://library.brown.edu/find/Record/b1438761", 
      "measurement_page_numeric": 499, 
      "creator": [
        "Kerouac, Jack, 1922-1969."
      ], 
      "measurement_height_numeric": 22, 
      "items": 1, 
      "title": "The town & the city.", 
      "pub_date": "1950", 
      "id": "b1438761", 
      "shelfrank": 10
    }, 
    {
      "measurement_page_numeric": 280, 
      "creator": [
        "Kerouac, Jack, 1922-1969."
      ], 
      "items": 1, 
      "title": "Vanity of Duluoz :an adventurous education, 1935-46 /", 
      "callnumber": "PS3521.E716 V3 1969", 
      "link": "http://library.brown.edu/find/Record/b1438770", 
      "shelfrank": 10, 
      "measurement_height_numeric": 21, 
      "pub_date": "1969", 
      "id": "b1438770"
    }, 
    {
      "callnumber": "PS3521.E716 V3 1969", 
      "link": "http://library.brown.edu/find/Record/b1438770", 
      "measurement_page_numeric": 280, 
      "creator": [
        "Kerouac, Jack, 1922-1969."
      ], 
      "measurement_height_numeric": 21, 
      "items": 1, 
      "title": "Vanity of Duluoz :an adventurous education, 1935-46 /", 
      "pub_date": "1969", 
      "id": "b1438770", 
      "shelfrank": 10
    }, 
    {
      "callnumber": "PS3521.E716 V48", 
      "link": "http://library.brown.edu/find/Record/b1438775", 
      "measurement_page_numeric": 398, 
      "creator": [
        "Kerouac, Jack, 1922-1969."
      ], 
      "measurement_height_numeric": 24, 
      "items": 1, 
      "title": "Visions of Cody", 
      "pub_date": "1972", 
      "id": "b1438775", 
      "shelfrank": 10
    }, 
    {
      "callnumber": "PS3521.E716 V5", 
      "link": "http://library.brown.edu/find/Record/b1438779", 
      "measurement_page_numeric": 151, 
      "creator": [
        "Kerouac, Jack, 1922-1969."
      ], 
      "measurement_height_numeric": 21, 
      "items": 2, 
      "title": "Visions of Gerard.", 
      "pub_date": "1963", 
      "id": "b1438779", 
      "shelfrank": 50
    }, 
    {
      "callnumber": "PS3521.E716 Z72", 
      "link": "http://library.brown.edu/find/Record/b1438783", 
      "measurement_page_numeric": 419, 
      "creator": [
        "Charters, Ann."
      ], 
      "measurement_height_numeric": 24, 
      "items": 1, 
      "title": "Kerouac;a biography.", 
      "pub_date": "1973", 
      "id": "b1438783", 
      "shelfrank": 10
    }, 
    {
      "measurement_page_numeric": 60, 
      "creator": [
        "Gifford, Barry, 1946-"
      ], 
      "items": 1, 
      "title": "Kerouac's town /", 
      "callnumber": "PS3521.E716 Z756 1977", 
      "link": "http://library.brown.edu/find/Record/b1083350", 
      "shelfrank": 10, 
      "measurement_height_numeric": 18, 
      "pub_date": "1977", 
      "id": "b1083350"
    }, 
    {
      "callnumber": "PS3521.E716 Z755", 
      "link": "http://library.brown.edu/find/Record/b1095175", 
      "measurement_page_numeric": 339, 
      "creator": [
        "Gifford, Barry, 1946-"
      ], 
      "measurement_height_numeric": 24, 
      "items": 4, 
      "title": "Jack's book :an oral biography of Jack Kerouac /", 
      "pub_date": "1978", 
      "id": "b1095175", 
      "shelfrank": 100
    }, 
    {
      "callnumber": "PS3521.E716 Z756 1977", 
      "link": "http://library.brown.edu/find/Record/b1083350", 
      "measurement_page_numeric": 60, 
      "creator": [
        "Gifford, Barry, 1946-"
      ], 
      "measurement_height_numeric": 18, 
      "items": 1, 
      "title": "Kerouac's town /", 
      "pub_date": "1977", 
      "id": "b1083350", 
      "shelfrank": 10
    }, 
    {
      "callnumber": "PS3521.E716 Z76", 
      "link": "http://library.brown.edu/find/Record/b1050253", 
      "measurement_page_numeric": 150, 
      "creator": [
        "Hipkiss, Robert A., 1935-"
      ], 
      "measurement_height_numeric": 23, 
      "items": 1, 
      "title": "Jack Kerouac, prophet of the new romanticism :a critical study of the published works of Kerouac and a comparison of them to those of J. D. Salinger, James Purdy, John Knowles, and Ken Kesey /", 
      "pub_date": "1976", 
      "id": "b1050253", 
      "shelfrank": 10
    }, 
    {
      "callnumber": "PS3521.E716 Z775", 
      "link": "http://library.brown.edu/find/Record/b1126318", 
      "measurement_page_numeric": 400, 
      "creator": [
        "McNally, Dennis."
      ], 
      "measurement_height_numeric": 24, 
      "items": 2, 
      "title": "Desolate angel :Jack Kerouace, the Beat generation, and America /", 
      "pub_date": "1979", 
      "id": "b1126318", 
      "shelfrank": 50
    }, 
    {
      "callnumber": "1-SIZE PS3521.E716 Z776x", 
      "link": "http://library.brown.edu/find/Record/b1296288", 
      "measurement_page_numeric": 250, 
      "creator": [], 
      "measurement_height_numeric": 28, 
      "items": 2, 
      "title": "Moody Street irregulars.", 
      "pub_date": "1978", 
      "id": "b1296288", 
      "shelfrank": 50
    }, 
    {
      "callnumber": "PS3521.E718 H6", 
      "link": "http://library.brown.edu/find/Record/b1094786", 
      "measurement_page_numeric": 264, 
      "creator": [
        "Kerr, Jean."
      ], 
      "measurement_height_numeric": 22, 
      "items": 1, 
      "title": "How I got to be perfect /", 
      "pub_date": "1978", 
      "id": "b1094786", 
      "shelfrank": 10
    }, 
    {
      "callnumber": "PS3521.E718 M3", 
      "link": "http://library.brown.edu/find/Record/b1438789", 
      "measurement_page_numeric": 181, 
      "creator": [
        "Kerr, Jean."
      ], 
      "measurement_height_numeric": 22, 
      "items": 2, 
      "title": "Mary, Mary.", 
      "pub_date": "1963", 
      "id": "b1438789", 
      "shelfrank": 50
    }, 
    {
      "callnumber": "PS3521.E718 P6", 
      "link": "http://library.brown.edu/find/Record/b1002686", 
      "measurement_page_numeric": 202, 
      "creator": [
        "Kerr, Jean."
      ], 
      "measurement_height_numeric": 22, 
      "items": 2, 
      "title": "Poor Richard;[a play]", 
      "pub_date": "1965", 
      "id": "b1002686", 
      "shelfrank": 50
    }, 
    {
      "measurement_page_numeric": 168, 
      "creator": [
        "Kerr, Jean."
      ], 
      "items": 2, 
      "title": "The snake has all the lines.", 
      "callnumber": "PS3521.E718 S5", 
      "link": "http://library.brown.edu/find/Record/b1438792", 
      "shelfrank": 50, 
      "measurement_height_numeric": 22, 
      "pub_date": "1960", 
      "id": "b1438792"
    }, 
    {
      "callnumber": "PS3521.E72 I3", 
      "link": "http://library.brown.edu/find/Record/b1438797", 
      "measurement_page_numeric": 292, 
      "creator": [
        "Kerr, Sophie, 1880-1965."
      ], 
      "measurement_height_numeric": 20, 
      "items": 1, 
      "title": "In for a penny", 
      "pub_date": "1931", 
      "id": "b1438797", 
      "shelfrank": 10
    }, 
    {
      "callnumber": "PS3521.E72 S4", 
      "link": "http://library.brown.edu/find/Record/b1438800", 
      "measurement_page_numeric": 3, 
      "creator": [
        "Kerr, Sophie, 1880-1965."
      ], 
      "measurement_height_numeric": 20, 
      "items": 1, 
      "title": "The see-saw;a story of to-day,", 
      "pub_date": "1919", 
      "id": "b1438800", 
      "shelfrank": 10
    }, 
    {
      "callnumber": "PS3521.E735 A6 1995", 
      "link": "http://library.brown.edu/find/Record/b2305716", 
      "measurement_page_numeric": 625, 
      "creator": [
        "Kerouac, Jack, 1922-1969."
      ], 
      "measurement_height_numeric": 21, 
      "items": 2, 
      "title": "The portable Jack Kerouac /", 
      "pub_date": "1995", 
      "id": "b2305716", 
      "shelfrank": 50
    }, 
    {
      "callnumber": "PS3521.E735 A6x 1990", 
      "link": "http://library.brown.edu/find/Record/b2096271", 
      "measurement_page_numeric": 3, 
      "creator": [
        "Kerouac, Jack, 1922-1969."
      ], 
      "measurement_height_numeric": 4, 
      "items": 4, 
      "title": "The Jack Kerouac collection", 
      "pub_date": "1990", 
      "id": "b2096271", 
      "shelfrank": 100
    }, 
    {
      "callnumber": "PS3521.E735 A92 1999", 
      "link": "http://library.brown.edu/find/Record/b2988454", 
      "measurement_page_numeric": 249, 
      "creator": [
        "Kerouac, Jack, 1922-1969."
      ], 
      "measurement_height_numeric": 23, 
      "items": 2, 
      "title": "Atop an Underwood :early stories and other writings /", 
      "pub_date": "1999", 
      "id": "b2988454", 
      "shelfrank": 50
    }, 
    {
      "callnumber": "PS3521.E735 B55 1995", 
      "link": "http://library.brown.edu/find/Record/b2362786", 
      "measurement_page_numeric": 1, 
      "creator": [
        "Kerouac, Jack, 1922-1969."
      ], 
      "measurement_height_numeric": 19, 
      "items": 2, 
      "title": "Book of blues /", 
      "pub_date": "1995", 
      "id": "b2362786", 
      "shelfrank": 50
    }, 
    {
      "callnumber": "PS3521.E735 B667 2006", 
      "link": "http://library.brown.edu/find/Record/b4037830", 
      "measurement_page_numeric": 413, 
      "creator": [
        "Kerouac, Jack, 1922-1969."
      ], 
      "measurement_height_numeric": 16, 
      "items": 1, 
      "title": "Book of sketches, 1952-57 /", 
      "pub_date": "2006", 
      "id": "b4037830", 
      "shelfrank": 10
    }, 
    {
      "callnumber": "PS3521.E735 D48 1959", 
      "link": "http://library.brown.edu/find/Record/b2586148", 
      "measurement_page_numeric": 192, 
      "creator": [
        "Kerouac, Jack, 1922-1969."
      ], 
      "measurement_height_numeric": 18, 
      "items": 3, 
      "title": "The Dharma bums /", 
      "pub_date": "1959", 
      "id": "b2586148", 
      "shelfrank": 70
    }, 
    {
      "callnumber": "PS3521.E735 M34 1993", 
      "link": "http://library.brown.edu/find/Record/b3984953", 
      "measurement_page_numeric": 194, 
      "creator": [
        "Kerouac, Jack, 1922-1969."
      ], 
      "measurement_height_numeric": 20, 
      "items": 1, 
      "title": "Maggie Cassidy /", 
      "pub_date": "1993", 
      "id": "b3984953", 
      "shelfrank": 10
    }, 
    {
      "callnumber": "PS3521.E735 M435 1992", 
      "link": "http://library.brown.edu/find/Record/b2069765", 
      "measurement_page_numeric": 202, 
      "creator": [
        "Jones, James T., 1948-"
      ], 
      "measurement_height_numeric": 23, 
      "items": 1, 
      "title": "A map of Mexico City blues :Jack Kerouac as poet /", 
      "pub_date": "1992", 
      "id": "b2069765", 
      "shelfrank": 10
    }, 
    {
      "callnumber": "PS3521.E735 O5 2007", 
      "link": "http://library.brown.edu/find/Record/b4357673", 
      "measurement_page_numeric": 408, 
      "creator": [
        "Kerouac, Jack, 1922-1969."
      ], 
      "measurement_height_numeric": 24, 
      "items": 1, 
      "title": "On the road :the original scroll /", 
      "pub_date": "2007", 
      "id": "b4357673", 
      "shelfrank": 10
    }, 
    {
      "callnumber": "PS3521.E735 O5 2009", 
      "link": "http://library.brown.edu/find/Record/b6149606", 
      "measurement_page_numeric": 1, 
      "creator": [
        "Kerouac, Jack, 1922-1969."
      ], 
      "measurement_height_numeric": 20, 
      "items": 1, 
      "title": "Getting inside Jack Kerouac's head /", 
      "pub_date": "2009", 
      "id": "b6149606", 
      "shelfrank": 10
    }, 
    {
      "callnumber": "PS3521.E735 O5x 1957", 
      "link": "http://library.brown.edu/find/Record/b4040534", 
      "measurement_page_numeric": 254, 
      "creator": [
        "Kerouac, Jack, 1922-1969."
      ], 
      "measurement_height_numeric": 18, 
      "items": 1, 
      "title": "On the road /", 
      "pub_date": "1957", 
      "id": "b4040534", 
      "shelfrank": 10
    }, 
    {
      "callnumber": "PS3521.E735 O5x 1958", 
      "link": "http://library.brown.edu/find/Record/b2598586", 
      "measurement_page_numeric": 254, 
      "creator": [
        "Kerouac, Jack, 1922-1969."
      ], 
      "measurement_height_numeric": 18, 
      "items": 1, 
      "title": "On the road /", 
      "pub_date": "1958", 
      "id": "b2598586", 
      "shelfrank": 10
    }, 
    {
      "callnumber": "1-SIZE PS3521.E735 O5325 2007", 
      "link": "http://library.brown.edu/find/Record/b4758951", 
      "measurement_page_numeric": 207, 
      "creator": [
        "Gewirtz, Isaac."
      ], 
      "measurement_height_numeric": 29, 
      "items": 1, 
      "title": "Beatific souls :Jack Kerouac on the road /", 
      "pub_date": "2007", 
      "id": "b4758951", 
      "shelfrank": 10
    }, 
    {
      "callnumber": "PS3521.E735 O533 1999", 
      "link": "http://library.brown.edu/find/Record/b2982105", 
      "measurement_page_numeric": 137, 
      "creator": [
        "Holton, Robert, 1950-"
      ], 
      "measurement_height_numeric": 23, 
      "items": 1, 
      "title": "On the road :Kerouac's ragged American journey /", 
      "pub_date": "1999", 
      "id": "b2982105", 
      "shelfrank": 10
    }, 
    {
      "measurement_page_numeric": 205, 
      "creator": [
        "Leland, John, 1959-"
      ], 
      "items": 1, 
      "title": "Why Kerouac matters :the lessons of On the road (they're not what you think) /", 
      "callnumber": "PS3521.E735 O5347 2007", 
      "link": "http://library.brown.edu/find/Record/b4181991", 
      "shelfrank": 10, 
      "measurement_height_numeric": 22, 
      "pub_date": "2007", 
      "id": "b4181991"
    }, 
    {
      "callnumber": "PS3521.E735 O5347 2007", 
      "link": "http://library.brown.edu/find/Record/b4181991", 
      "measurement_page_numeric": 205, 
      "creator": [
        "Leland, John, 1959-"
      ], 
      "measurement_height_numeric": 22, 
      "items": 1, 
      "title": "Why Kerouac matters :the lessons of On the road (they're not what you think) /", 
      "pub_date": "2007", 
      "id": "b4181991", 
      "shelfrank": 10
    }, 
    {
      "callnumber": "PS3521.E735 O537 1999", 
      "link": "http://library.brown.edu/find/Record/b2857341", 
      "measurement_page_numeric": 130, 
      "creator": [
        "Swartz, Omar."
      ], 
      "measurement_height_numeric": 24, 
      "items": 1, 
      "title": "The view from On the road :the rhetorical vision of Jack Kerouac /", 
      "pub_date": "1999", 
      "id": "b2857341", 
      "shelfrank": 10
    }, 
    {
      "callnumber": "PS3521.E735 O55 2009", 
      "link": "http://library.brown.edu/find/Record/b4671317", 
      "measurement_page_numeric": 214, 
      "creator": [], 
      "measurement_height_numeric": 23, 
      "items": 1, 
      "title": "What's your road, man? :critical essays on Jack Kerouac's On the road /", 
      "pub_date": "2009", 
      "id": "b4671317", 
      "shelfrank": 10
    }, 
    {
      "callnumber": "1951 K3966 J69s 1994", 
      "link": "http://library.brown.edu/find/Record/b2247678", 
      "measurement_page_numeric": 4, 
      "creator": [
        "Kerouac, Jack, 1922-1969."
      ], 
      "measurement_height_numeric": 16, 
      "items": 3, 
      "title": "Scripture of the golden eternity /", 
      "pub_date": "1994", 
      "id": "b2247678", 
      "shelfrank": 70
    }
  ]
};
    $(function () { 
            $('#stackview').stackView(
                {
                "data" : data,
                'books_per_page': "1",
                'start': "30",
                'ribbon': "Stackview -- On the road -- PS3521.E716 O5",
                }
            );
    });
</script>

### Z39.50 

[Z39.50](http://en.wikipedia.org/wiki/Z39.50) is a pre-Web protocol for search and retrieval.  The major advantage to using Z39.50 for data sources in examples like these is that it has been implemented widely (if varyingly) and most ILS systems provide servers both for querying internal data and allowing others to query the data in the system.  In the current library systems environment, it may be the only API to the underlying data.      

For more information about the protocol and working with it I recommend the [Z39.50 for Dummies](http://www.indexdata.com/blog/2009/08/z3950-dummies) series that [IndexData](http://www.indexdata.com) put together in 2009.  You can also read some of the arguments for and against still using Z39.50 in the comment thread of this blog post on [Disruptive Library Technology Jester](http://dltj.org/article/z3950-for-dummies/).  

### Z39.50 scan results
Some Z39.50 implementations provide a facility for 'scanning' a collection by various indexes.  Scan results are like the [title](http://josiah.brown.edu/search~S7/t?SEARCH=on+the+road), [call number](http://josiah.brown.edu/search/c?searchtype=c&searcharg=PS3521.E716), and [subject](http://josiah.brown.edu/search~S7/d?search=blizzards) browses seen in most 'classic' library catalogs.  

The Library of Congress Z39.50 implementor agreement says that [scan](http://www.loc.gov/z3950/agency/contributions/2.html), "returns results that consist of terms with complementary data, representing rows from an ordered list. The results can be presented to an end user, enabling him or her to browse forward and optionally backwards.."

The examples below use the Python [PyZ3950](https://github.com/asl2/PyZ3950) library.  You can install it with 'pip install Pyz3950'.  It's also helpful to use [pymarc](https://github.com/edsu/pymarc/) to handle the returned MARC records.

The code below has been tested only with an Innovative Interfaces Z39.50 server but it should work with minimal modification on any Z39.50 implementations that supports scan.  

### Call number scan.  

Below is code for a basic scan by call number.  As you can see, we specify the number of results to be returned (11) and the position (6) we want the requested call number to be in that list.    

~~~~{.python}
from PyZ3950 import zoom

conn = zoom.Connection('library.school.edu', 210)
conn.databaseName = 'INNOPAC'

call_number = "PS3521.E716 O5 1979"

params = '@attr 1=16 "%s"' % call_number
query = zoom.Query('PQF', params)

#Number of items returned.  
conn.numberOfEntries = 11
#Position in the list of the item we are requesting.
response_position = 6
conn.responsePosition = response_position

results = conn.scan(query)

for index, rec in enumerate(results):
    display = rec.get('display')
    if index + 1 == response_position:
        print '---->  ', display
    else:
        print '\t', display

conn.close()
~~~~

Running this search against the [Brown University Library](http://library.brown.edu/) library catalog, you would get results like below.  The arrow indicates the position in the list of the call number we requested.  

~~~
        Ps 3521 E716 D4^   1 entry
        Ps 3521 E716 D6^   1 entry
        Ps 3521 E716 D6 1959^   1 entry
        Ps 3521 E716 D6 1987^   1 entry
        Ps 3521 E716 E9^   1 entry
---->   Ps 3521 E716 O5 1979^   2 entries
        Ps 3521 E716 O77 X 2002^   1 entry
        Ps 3521 E716 T6^   1 entry
        Ps 3521 E716 V3^   2 entries
        Ps 3521 E716 V3 1969^   1 entry
        Ps 3521 E716 V48^   1 entry

~~~

### Call number scan and fetching metadata

Taking this a step further, now that you have a sorted list of call numbers you might want to fetch the bibliographic details for each title.  In the example below, each item in the scan result is passed to a Z39.50 search that returns the MARC record for each title.  The MARC record is read with [pymarc](https://github.com/edsu/pymarc/) and a Record object is created that allows us to convert the data into more friendly formats.  

~~~~{.python}
from PyZ3950 import zoom
import pymarc

conn = zoom.Connection('library.school.edu', 210)
conn.databaseName = 'INNOPAC'

def get_record_by_call(call):
    """
    Function to fetch a bib record by 
    call number.
    """
    params = '@attr 1=16 "%s"' % call
    query = zoom.Query('PQF', params)
    results = conn.search(query)
    for bib in results:
        return pymarc.Record(data=bib.data)

call_number = "PS3521.E716 O5"

params = '@attr 1=16 "%s"' % call_number
query = zoom.Query('PQF', params)

#Number of items returned.  
conn.numberOfEntries = 20
#Position in the list of the item we are requesting.
conn.responsePosition = 11

results = conn.scan(query)

for rec in results:
    #print rec
    display = rec.get('display')
    #Get the call number
    call = rec.get('term')[1]
    #Get the bibliographic record for this call number.
    bib = get_record_by_call(call)
    print bib.title()

conn.close()
~~~~

### Web service to implement Stack View on your library website

To fully integrate this into a website, you will need to run a basic web service that can lookup the call number for a given title, scan for nearby items, and then return the metadata for those items in a [Stack View compliant JSON format](http://librarylab.law.harvard.edu/projects/stackview/demo/documentation.html).  I have posted [code](https://gist.github.com/lawlesst/4722068) for a simple Python and [Flask](http://flask.pocoo.org/) app on [Github]((https://gist.github.com/lawlesst/4722068)) that implements Stack View.  This code is in use on an internal website and seems to be working fine but hasn't been fully implemented yet.  So please use it as a reference rather than something that can be installed and used right away. 


