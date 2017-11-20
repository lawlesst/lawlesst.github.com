Title:Publishing the Lahman Baseball Database with Datasette
Date:11-20-17
Slug:baseball-datasette

>Summary: publishing the [Lahman Baseball Database](http://www.seanlahman.com/baseball-archive/statistics/) with [Datasette](https://simonwillison.net/2017/Nov/13/datasette/). API available at [https://baseballdb.lawlesst.net](https://baseballdb.lawlesst.net).

For those of us interested in open data, an exciting new tool was released this month. It's by [Simon Willison](https://simonwillison.net/) and called [Datasette](https://simonwillison.net/2017/Nov/13/datasette/). Datasette allows you to very quickly convert CSV files to a sqlite database and publish on the web with an API. Head over to Simon's [site](https://simonwillison.net/2017/Nov/13/datasette/) for more details. [Paul Ford](https://twitter.com/ftrain) also has also published a nice summary of the tool on Medium, "[Big Data, Small Effort](https://trackchanges.postlight.com/big-data-small-effort-b62607a43a8c)".

Since I'm interested in both open data and baseball history, I decided to try Datasette with the [Lahman Baseball Database](http://www.seanlahman.com/baseball-archive/statistics/). For those not familiar, the Lahman Baseball Database is a dataset of players, teams, managers, parks - really anything baseball - that spans from 1871 to 2016. It's available under a Creative Commons License and freely available for download from [Lahman's site](http://www.seanlahman.com/baseball-archive/statistics/). If you ever had a copy of the Baseball Encyclopedia, this is basically what it is but in database form. It's a great resource.

### Setup

For an initial proof-of-concept with Datasette, I decided to focus just on players (the Master.csv file), appearances, and teams. This is a large enough subset of the total database to be interesting but small enough to quickly get up and running. Following the documentation in the Datasette README, I was able to have the tool up and running in minutes. Very easy to get started.

### Querying

You can find the Datasette instance loaded with the Lahaman database running at [https://baseballdb.lawlesst.net](https://baseballdb.lawlesst.net). The three tables are easily browseable using Datasette's interface and API. Datasette also supports SQL and bookmarkable queries.

Using the Lahman database we can start asking questions about baseball history. Here are a few basic queries to get started:

* What's the minimum and maximum birth year for players who have appeared in MLB? [Answer](https://baseballdb.lawlesst.net/baseball-60223b5?sql=select+min%28birthYear%29%2C+max%28birthYear%29+from+Master)

* What's the most frequent home state for players across all years? [Answer](https://baseballdb.lawlesst.net/baseball-60223b5?sql=select+birthState%2C+count%28birthState%29+n+from+Master+group+by+birthState+order+by+n+desc%3B)

And few more complex queries that require joining across tables:

* Top 20 players in terms of the number of seasons they appeared in. [Answer](https://baseballdb.lawlesst.net/baseball-60223b5?sql=select+A.playerID%2C+M.nameFirst%2C+M.nameLast%2C+M.debut%2C+count%28distinct+A.yearID%29+as+n+%0D%0Afrom+Appearances+A%0D%0Ajoin+Master+M%0D%0A+on+A.playerID%3DM.playerID%0D%0Awhere+G_all+%3E+0+%0D%0Agroup+by+A.playerID+%0D%0Aorder+by+n+desc+limit+20%3B)

* Players who appeared in games during the 1984 season for the World Series winning 1984 Detroit Tigers. This requires joining all three tables. [Answer](https://baseballdb.lawlesst.net/baseball-60223b5?sql=select+A.playerID%2C+M.nameFirst%2C+M.nameLast%2C+A.G_all+as+gamesPlayed%0D%0Afrom+Teams+T%0D%0Ajoin+Appearances+A+on%0D%0A+T.yearID%3DA.yearID+and+T.teamID%3DA.teamID%0D%0Ajoin+Master+M+on%0D%0A+A.playerID%3DM.playerID%0D%0Awhere+T.yearID%3D1984+and+T.teamID%3D%22DET%22%0D%0Aorder+by+M.nameLast)

If you are interested in baseball history or statistics, I'm sure you can easily come up with more questions to build off of these.

### Deployment
Some details on deploying Datasette for public querying.

To deploy, I settled on using a small Digital Ocean droplet and am using Apache as a reverse proxy. Datasette is setup to be easily published with [Zeit Now](https://zeit.co/now) but the sqlite database of these three baseball files exceeded the size limit for the free tier with Now. I also tried Heroku but again ran into file size issues.

I also ran into connection timeout issues with the [Sanic](https://github.com/channelcat/sanic) web framework Datasette uses, as described in this [pull request](https://github.com/channelcat/sanic/pull/939). This was more of an annoyance than a problem since clicking refresh in Chrome made the error disappear. Installing Sanic directly from Github with pip made this issue go away.

Datasette is deployed wit the [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) option so you should be able to use this endpoint in client side demos.

Thanks for reading this far. Please add a comment with any feedback you have or any ways that you may extend this.

