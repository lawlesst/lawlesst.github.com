Title:Datasette hosting costs
Date:1-16-21
Slug:datasette-hosting

I've been hosting a [Datasette](https://datasette.io/) ([https://baseballdb.lawlesst.net](https://baseballdb.lawlesst.net)) of historical baseball data for a few years and the last year or so it has been hosted on Google Cloud Run. I thought I would share my hosting costs for 2020 as a point of reference for others who might be interested in running a Datasette but aren't sure how much it may cost.

The total hosting cost on Google Cloud Run for 2020 was $51.31 for a monthly average of about $4.28 USD. The monthly bill did vary a fair amount from as high as $13 in May to as low as $2 in March. Since, I did no deployments during this time or updates to the site, I assume all of the variation in costs is related to traffic. I don't have a good sense of how many queries this instance is serving since I'm not using Google Analytics or similar.

Google does report that it is subtracting $49.28 in credits for the year but I don't expect those credits/promotions to expire anytime soon since my projected costs for 2021 is $59.

Since I don't know how much this site is used, this cost might not be as helpful as it could be but it is an Datasette instance that's freely available for use and it costs about as much as a nice latte to run each month.

For me, that's a low enough cost to keep it around for the few times a year I care to use it and for any utility others may be getting from it.

Thanks again to [Simon Willison](https://simonwillison.net/)  for building and maintaining Datasette and to the [Chadwick Bureau](http://chadwick-bureau.com/) for maintaining, and making freely available, the Baseball Databank.
