Title:Datasette hosting costs
Date:1-16-21
Slug:datasette-hosting

I've been hosting a [Datasette](https://datasette.io/) ([https://baseballdb.lawlesst.net](https://baseballdb.lawlesst.net), aka baseballdb) of historical baseball data for a few years and the last year or so it has been hosted on Google Cloud Run. I thought I would share my hosting costs for 2020 as a point of reference for others who might be interested in running a Datasette but aren't sure how much it may cost.

The total hosting cost on Google Cloud Run for 2020 for the baseballdb was $51.31, or a monthly average of about $4.28 USD. The monthly bill did vary a fair amount from as high as $13 in May to as low as $2 in March. Since I did no deployments during this time or updates to the site, I assume the variation in costs is related to the amount queries the Datasette was serving. I don't have a good sense of how many total queries per month this instance is serving since I'm not using Google Analytics or similar.

Google does report that it is subtracting $49.28 in credits for the year but I don't expect those credits/promotions to expire anytime soon since my projected costs for 2021 is $59.

This cost information is somewhat incomplete without knowing the number of queries served per month but it is a benchmark. The site is freely available and there's no attempt to limit its usage. In short, it costs about as much as a nice latte to run each month. For me, that's a low enough cost to keep it around for the few times a year I care to use it and for any utility others may be getting from it.

Thanks again to [Simon Willison](https://simonwillison.net/)  for building and maintaining Datasette and to the [Chadwick Bureau](http://chadwick-bureau.com/) for maintaining, and making freely available, the Baseball Databank.
