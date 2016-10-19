Title:Querying Wikidata to Identify Globally Famous Baseball Players
Date:10-18-16
Slug:wikidata-baseball-fame

Earlier this year I had the pleasure of attending a lecture by [Cesar Hidalgo](https://www.media.mit.edu/people/hidalgo) of MIT's Media Lab. One of the projects Hidalgo discussed was [Pantheon](http://pantheon.media.mit.edu/t). Pantheon is a website and dataset that ranks "globally famous individuals" based on a metric the team created called the Historical Popularity Index (HPI). A key component of HPI is the number of Wikipedia pages an individual has in in various languages. For a complete description of the project, see:

>Yu, A. Z., et al. (2016). Pantheon 1.0, a manually verified dataset of globally famous biographies. Scientific Data 2:150075. [http://doi.org/10.1038/sdata.2015.75](http://doi.org/10.1038/sdata.2015.75)

Since the Pantheon project relies mostly on open data, I wondered if I could apply some of their techniques to look at the historical significance of Major League Baseball players. 


## Identifying famous baseball players using Wikidata

When the Pantheon team was assembling their data in 2012 - 2013 they considered using Wikidata rather than Wikipedia and Freebase data dumps but they found, at that time, it wasn't quite ready in terms of the amount of data. A lot has changed since then, data has accumulated in Wikidata and there are various web services for querying it, including a SPARQL endpoint. 

### Querying for total Wikipedia pages

With Wikidata's SPARQL support, we don't have to parse data dumps from Wikipedia and Freebase to do some initial, Pantheon inspired exploration. We can write a single SPARQL query to find entities (players) and the number of Wikipedia language pages each have. 

Here is the query, I used for this exercise.

~~~
SELECT ?player ?playerLabel ?brId (COUNT(DISTINCT(?sitelink)) as ?sites)
WHERE
{
    ?player wdt:P31 wd:Q5 .
    ?player wdt:P1825 ?brId .
    ?sitelink schema:about ?player .
    SERVICE wikibase:label {
        bd:serviceParam wikibase:language "en" .
    }
}
GROUP BY ?player ?playerLabel ?brId
~~~

I'm restricting to instances with a Baseball Reference ID (Wikidata property [P1825](https://www.wikidata.org/wiki/Property:P1825) rather than those with the because when I initially ran this query I found many non-professional baseball players with the occupation ([P106](https://www.wikidata.org/wiki/Property:P106) of baseball player ([Q10871364](https://www.wikidata.org/wiki/Q10871364) in Wikidata. This included former U.S. President [George H.W. Bush](https://en.wikipedia.org/wiki/George_H._W._Bush) and the actor and comedian [Billy Crystal](https://en.wikipedia.org/wiki/Billy_Crystal). These people played baseball at one time, which is interesting in a different way, but not in the MLB.

Retrieving the Baseball Reference ID in another way. I can use it to join the knowledge stored in Wikidata with other sources, like Baseball Reference or the [Lahman Baseball Database](http://www.seanlahman.com/baseball-archive/statistics/). This is one of the aspects that I find most promising with Wikidata, it can serve as an identifier hub that allows users to join data from many sources, each of which have unique aspects. 

### Results
Using the results from this SPARQL query we are able to rank players by the number of Wikipedia language pages written about them. The top 10 is as follows. 

<script src="https://gist.github.com/lawlesst/bdbd2142c2ab667eae1be3b7a789f5da.js?file=top10_by_language_pages.csv"></script>

This top 10 list is filled with some of baseball's all time greats, including Babe Ruth at number one, which seems right. But there is at least one surprise, [Jim Thorpe](https://en.wikipedia.org/wiki/Jim_Thorpe) coming in at sixth. Thorpe had a remarkable athletic career in multiple sports but only played briefly in the MLB, so he's not often in discussions of baseball's great players.

I've also uploaded a [csv file](https://gist.github.com/lawlesst/bdbd2142c2ab667eae1be3b7a789f5da#file-top_250_by_pages-csv) containing players that have 9 or more Wikipedia language pages, which means they are in the top 250 players (or) when ranked by number of language pages.

### Digging deeper 

Now that we have a list of globally famous baseball players determined by the number of Wikipedia pages in various languages, we can dig a little deeper and try to understand if fame has anything to do with actual performance on the baseball field. 

## Wins Above Replacement - WAR
Baseball Reference, calculates a metric called [Wins Above Replacement (WAR)](http://www.baseball-reference.com/about/war_explained.shtml). Describing WAR in detail is beyond the scope of this post but, briefly, WAR is a metric that attempts to capture how much a player is better than the average, or a replacement, player. If a player has a WAR of 2 for a season, that means his team won 2 more games than they would have if they would have used a replacement player instead. WAR attempts to cover all facets of the game, hitting, fielding, and base running. In recent years, WAR has begun to receive more attention from baseball media since it tries to capture the complete value of a player rather than a single aspect, like batting average.

WAR can also be a valuable way to rank players over the course of a career. Baseball Reference [publishes a list](http://www.baseball-reference.com/leaders/WAR_bat_career.shtml) of the top 1,000 players of all time based on career WAR. Here again, Babe Ruth tops the list here too. But, does WAR, or performance on the field, relate at all to global fame? 

To investigate this question, I grabbed the [top 50 players](http://www.baseball-reference.com/leaders/WAR_bat_career.shtml) by career WAR from Baseball Reference. Since WAR is calculated differently for position players and pitchers, I've focused this exercise just on position players. 

I merged the career WAR information with the Wikidata information using the Baseball Reference IDs. I then generated a rank for each player based on the number of Wikipedia language pages and career WAR ranking. The full data is available as [CSV](https://gist.github.com/lawlesst/bdbd2142c2ab667eae1be3b7a789f5da#file-war_top_50-csv) and inline below.

<script src="https://gist.github.com/lawlesst/bdbd2142c2ab667eae1be3b7a789f5da.js?file=war_top_50.csv"></script>

At least a few things stand out in this list.

* some players, like the legendary Yankees centerfielder Joe DiMaggio have significant higher fame scores than WAR scores (5th vs 42nd). This can because of non-baseball reasons (served in WWII and was married to Marilyn Monroe) or because of a relatively short impactful, career. 

* other players performed well on the field but aren't as famous. Lou Whitaker and George Davis are both ranked in the top 50 for career WAR but not in in the top 2000 players when ranked by Wikipedia language pages. 

* there are still relatively few players that could be considered "globally famous" when thinking of history as a whole. The Pantheon team set a threshold of 25 language pages when they ran their analysis. At this time, only 12 players would meet that mark.

* the list seems weighted towards players who have played during the last 10-15 years. We could use the Baseball Reference data to verify that.


To pursue these basic comparisons further, and produce more meaningful results, I would want to take a look at the other data used by the Pantheon team, like Wikipedia page views, and the time period of the careers to develop a HPI-like metric for baseball players. We could also try to isolate by team, era, etc or investigate which languages are writing about baseball players and see if we can gleam any cultural insight from that.

## Conclusion

The main takeaway for me is that using Wikidata and SPARQL, and the methods from the Pantheon project, we can relatively quickly explore global fame for groups people we are interested in. Using identifiers stored in Wikidata, we can join information from the Wikidata knowledge base with external, domain specific, sets of data that can allow us to dig deeper.