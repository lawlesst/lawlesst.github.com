Title:SPARQL to Pandas Dataframes
Date:10-26-17
Slug:sparql-dataframe

## Using Pandas to explore data SPARQL

[Pandas](http://pandas.pydata.org/) is a Python based power tool for munging and analyzing data. While working with data from SPARQL endpoints, you may prefer to explore and analyze it with pandas given its full feature set, strong documentation and large community of users.

The code below is an example of issuing a query to the [Wikidata SPARQL endpoint](http://query.wikidata.org) and loading the data into a pandas dataframe and running basic operations on the returned data.

This is a modified version of [code from Su Labs](https://github.com/SuLab/sparql_to_pandas). Here we remove the types returned by the SPARQL endpoint since they add noise and we will prefer to handle datatypes with Pandas.

{% notebook sparql_dataframe.ipynb %}

'''
with r as (
  select reader_wikidata as wid, count(*) as n
  from episodes 
  group by reader_wikidata
), w as (
  select writer_wikidata as wid, count(*) as n
  from episodes
  group by writer_wikidata
), wids as (
select distinct wid
from
(
select wid from r
union
select wid from w
)
)
select distinct wids.wid, people.personLabel, strftime('%Y-%m-%d', birth) as yr, coalesce(r.n, 0) as reader, coalesce(w.n, 0) as writer, (coalesce(r.n, 0) + coalesce(w.n, 0)) as total_apperances
from wids
left join r using (wid)
left join w using (wid)
join people using (wid)
where reader=1
order by yr 
'''
