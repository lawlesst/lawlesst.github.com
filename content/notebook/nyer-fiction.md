Title:Exploring 10 years of the New Yorker Fiction Podcast with Wikidata
Date:02-06-18
Slug:nyer-fiction

>Note: The dta behind this datasette was updated on 7/24/18 to capture new episodes. The examples below might result in slightly different numbers.

The [New Yorker Fiction Podcast](https://www.newyorker.com/podcast/fiction) recently celebrated its ten year anniversary. For those of you not familiar, this is a monthly podcast hosted by New Yorker fiction editor Deborah Treisman where a writer who has published a short story in the New Yorker selects a favorite story from the magazine's archive and reads and discusses it on the podcast with Treissman.[^1] 

I've been a regular listener to the podcast since it started in 2007 and thought it would be fun to look a little deeper at who has been invited to read and what authors they selected to read and discuss.

[^1]: For those of you who are listeners to the podcast, I apologize for the hasty paraphrase of the show's intro.

The New Yorker posts all episodes of the Fiction podcast on their website in nice clean, browseable HTML pages. I wrote a [Python script](https://github.com/lawlesst/new-yorker-fiction-podcast-data/blob/master/scripts/harvest.py) to step through the pages and pull out the basic details about each episode:

* title
* url
* summary
* date published
* writer
* reader

The reader and the writer for each story is embedded in the title so a bit of text processing was required to cleanly identify each reader and writer. I also had to manually reconcile a few episodes that didn't follow the same pattern as the others.

All code used here and harvested data is available on [Github](https://github.com/lawlesst/new-yorker-fiction-podcast-data).

## Matching to Wikidata

I then took each of the writers and readers and [matched](https://github.com/lawlesst/new-yorker-fiction-podcast-data/blob/master/scripts/wd_details.py) them to Wikidata using the [searchentities API](https://www.wikidata.org/w/api.php?action=help&modules=wbsearchentities).

With the Wikidata ID, I'm able to retrieve many attributes each reader and writer by querying the Wikidata [SPARQL endpoint](https://query.wikidata.org/), such as gender, date of birth, awards received, Library of Congress identifier, etc.

## Publishing with Datasette

I saved this harvested data to two CSV files - `episodes.csv` and `people.csv` - and then built a sqlite database to publish with [Datasette](https://github.com/simonw/datasette) using the built-in integration with [Zeit Now](https://zeit.co/now). This data is available at [nyerfp-demo-datasette.now.sh](https://nyerfp-demo-datasette.now.sh/)

## Results

Now we can use Datasette and SQL to take a deeper look at who has participated in the podcast over the years.

* [167 distinct people](https://nyerfp-demo-datasette.now.sh/nyer-fiction-podcast-27cb333?sql=select+distinct+wid%2C+personLabel%2C+siteLink+%0D%0Afrom+people%0D%0Aorder+by+personLabel%3B+) have been either readers or writers on the podcast over [129 episodes](https://nyerfp-demo-datasette.now.sh/nyer-fiction-podcast-27cb333?sql=select+*+from+episodes%0D%0Aorder+by+date_published%3B).

* [62 women and 105 men](https://nyerfp-demo-datasette.now.sh/nyer-fiction-podcast-27cb333?sql=select+genderLabel%2C+count%28distinct+wid%29+%0D%0Afrom+people%0D%0Agroup+by+genderLabel+%3B) have either read or written a featured story.

* The late [Donald Barthelme](https://en.wikipedia.org/wiki/Donald_Barthelme) has had the [most appearances](https://nyerfp-demo-datasette.now.sh/nyer-fiction-podcast-27cb333?sql=select+wid%2C+personLabel%2C+count%28distinct+e1.id%29+as+reader%2C+count%28distinct+e2.id%29+as+writer%2C+%28count%28distinct+e1.id%29+%2B+count%28distinct+e2.id%29%29+as+total%0D%0Afrom+people+p%0D%0Aleft+join+episodes+e1+on+p.wid%3De1.reader_wikidata+%0D%0Aleft+join+episodes+e2+on+p.wid%3De2.writer_wikidata+%0D%0Agroup+by+wid%0D%0Aorder+by+total+desc%3B) on the podcast with five of his stories being read. This also makes him the most featured writer.

* [Junot Diaz](https://en.wikipedia.org/wiki/Junot_D%C3%ADaz) has read three stories, which tops the readers.

* [20 writers](https://nyerfp-demo-datasette.now.sh/nyer-fiction-podcast-27cb333?sql=with+p+as+%28%0D%0A++select+wid%2C+personLabel%2C+count%28distinct+e1.id%29+as+reader%2C+count%28distinct+e2.id%29+as+writer%2C+%28count%28distinct+e1.id%29+%2B+count%28distinct+e2.id%29%29+as+total%2C+siteLink%0D%0Afrom+people+p%0D%0Aleft+join+episodes+e1+on+p.wid%3De1.reader_wikidata+%0D%0Aleft+join+episodes+e2+on+p.wid%3De2.writer_wikidata+%0D%0Agroup+by+wid%0D%0A%29%0D%0Aselect+*%0D%0Afrom+p%0D%0Awhere+reader+%3E+0+and+writer+%3E+0+%0D%0Aorder+by+total+desc%3B) have both read a story and were the author of a featured story.

* [13 writers](https://nyerfp-demo-datasette.now.sh/nyer-fiction-podcast-432e4ea?sql=select+distinct+wid%2C+personLabel%2C+siteLink%0D%0Afrom+people%0D%0Awhere+macGeniusGrant%3D1%0D%0Aorder+by+personLabel%3B) that have appeared or been featured on the podcast have also received a [MacArthur Genius Grant](https://en.wikipedia.org/wiki/MacArthur_Fellows_Program).

* [Téa Obreht](https://en.wikipedia.org/wiki/T%C3%A9a_Obreht) is the [youngest writer](https://nyerfp-demo-datasette.now.sh/nyer-fiction-podcast-27cb333?sql=select+wid%2C+personLabel%2C+strftime%28%27%25Y-%25m-%25d%27%2C+birth%29+as+birthYear%2C+siteLink%0D%0Afrom+people+%0D%0Aorder+by+birthYear+desc+%3B) to appear on the podcast - born in 1985 - when she read Stephanie Vaughn's story on the [12/16/11 episode](https://www.newyorker.com/podcast/fiction/tea-obreht-reads-stephanie-vaughn).

* [Bruno Schulz](https://en.wikipedia.org/wiki/Bruno_Schulz) is the oldest writer to have been featured on the podcast, born 1892. [Nicole Krauss](https://en.wikipedia.org/wiki/Nicole_Krauss) read his story on the [2/17/12 episode](https://www.newyorker.com/podcast/fiction/nicole-krauss-reads-bruno-schulz).

Use the Datasette instance at [nyerfp-demo-datasette.now.sh](https://nyerfp-demo-datasette.now.sh/) to ask your own questions.

## Summary/notes

Some notes on the data harvesting and processing:

The New Yorker data was straightforward to harvest from their website since the pages are well structured and all episodes are published. However, the information about each episode is rather sparse. For instance, the reader and writer of the story aren't fielded but described in a sentence, albeit one structured similarly across episodes. I also didn't attempt to pull out the name of the story read, which does seem to be in the description for most stories, so that could be an improvement.

On the Wikidata side, the full name of the author and looking for "writer/author/novelist" in the description string was enough to resolve the reader and writer strings to a Wikidata ID. In three cases, the writer didn't have a Wikidata profile so I simply created pages for these people. As for querying Wikidata via the SPARQL endpoint, I find the provided [examples](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples) to be excellent and used those to fetch the relevant properties.

There may be errors in how the readers and writers were matched to Wikidata or some problems with how the data was pulled. If you find something or have a question, leave a comment below.
