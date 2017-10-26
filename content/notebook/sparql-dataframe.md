Title:SPARQL to Pandas Dataframes
Date:10-26-17
Slug:sparql-dataframe

## Using Pandas to explore data SPARQL

[Pandas](http://pandas.pydata.org/) is a Python based power tool for munging and analyzing data. While working with data from SPARQL endpoints, you may prefer to explore and analyze it with pandas given its full feature set, strong documentation and large community of users.

The code below is an example of issuing a query to the [Wikidata SPARQL endpoint](http://query.wikidata.org) and loading the data into a pandas dataframe and running basic operations on the returned data.

This is a modified version of [code from Su Labs](https://github.com/SuLab/sparql_to_pandas). Here we remove the types returned by the SPARQL endpoint since they add noise and we will prefer to handle datatypes with Pandas.

{% notebook sparql_dataframe.ipynb %}

With a few lines of code, we can connect data stored in SPARQL endpoints with pandas, the powerful Python data munging and analysis library.

See the [Su Labs tutorial](https://github.com/SuLab/sparql_to_pandas/blob/master/SPARQL_pandas.ipynb) for more examples.
