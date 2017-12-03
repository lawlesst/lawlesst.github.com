Title:Now Publishing Complete Lahman Baseball Database with Datasette
Date:12-03-17
Slug:baseball-datasette-full

>Summary: The [Datasette](https://simonwillison.net/2017/Nov/13/datasette/) API available at [https://baseballdb.lawlesst.net](https://baseballdb.lawlesst.net) now contains the full [Lahman Baseball Database](http://www.seanlahman.com/baseball-archive/statistics/).

In a [previous post](http://lawlesst.github.io/notebook/baseball-datasette.html), I described how I'm using [Datasette](https://simonwillison.net/2017/Nov/13/datasette/) to publish a subset of the Lahman Baseball Database. At that time, I only published three of the 27 tables available in the database. I've since expanded that Datasette API to include the complete Baseball Database.

The process for this was quite straightforward. I ran the MySQL dump Lahman [provides](http://www.seanlahman.com/baseball-archive/statistics/) through this [mysql2sqlite](https://github.com/dumblob/mysql2sqlite/blob/master/mysql2sqlite) tool to provide an import file for sqlite. Importing into sqlite for publishing with Datasette was as simple as:

```
$ ./mysql2sqlite lahman2016.sql | sqlite3 baseball.db
```

The complete sqlite version of the Lahman dabase is 31 megabytes.

### Querying

With the full database now loaded, there are many more interesting queries that can be run. Including:

* Who played the most games at 2B in MLB history? [Answer](https://baseballdb.lawlesst.net/baseball-5b7556e?sql=select+F.playerID%2C+M.nameFirst+%7C%7C+%27+%27+%7C%7C++M.nameLast+as+name+%2C+sum%28F.G%29+as+games%0D%0Afrom+Fielding+F%0D%0Ajoin+Master+M+using+%28playerID%29%0D%0Awhere+F.POS%3D%222B%22%0D%0Agroup+by+F.playerID%0D%0AORDER+BY+games+desc+%0D%0ALIMIT+100%3B+)
* In what park has the most MLB games been played? [Answer](https://baseballdb.lawlesst.net/baseball-5b7556e?sql=select+H.%22park.key%22%2C+%22park.name%22%2C+city%2C+state%2C+sum%28games%29+as+games%0D%0Afrom+HomeGames+H%0D%0Ajoin+Parks+P+using+%28%22park.key%22%29%0D%0Agroup+by+H.%22park.key%22+%0D%0Aorder+by+games+desc%0D%0Alimit+100%3B)
* Which players who made their debut in the 1950 season or later committed they most errors? [Answer](https://baseballdb.lawlesst.net/baseball-5b7556e?sql=select+playerID%2C+nameFirst%2C+nameLast%2C+sum%28E%29+as+errors%2C+debut%2C+finalgame%0D%0Afrom+Fielding+F%0D%0Ajoin+Master+M+using+%28playerID%29%0D%0Awhere+debut+%3E+date%28%271950-01-01%27%29%0D%0Agroup+by+playerID%0D%0Aorder+by+errors+desc%0D%0Alimit+100+%3B)

Happy querying. If you are using this in a project or interested in learning more, leave a comment below or contact me via email.

