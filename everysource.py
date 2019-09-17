# imports the newsapi library
from newsapi import NewsApiClient
# not sure if it's better to use the CVS or pandas library to export the API pull results
# still learning how to use both libraries
import csv
import pandas
# assigns my key to the newsapi variable to access api data
api = NewsApiClient(api_key = 'e8307c205d23466e9daed66da20777ed')
# defines a series of parameters and assigns them to the all_articles variable
all_articles = newsapi.get_everything(q='Cory Booker',
#                                      sources='bbc-news,the-verge,',
#                                      domains='bbc.co.uk,techcrunch.com',
#                                      from_param='2019-08-07',
#                                      to='2019-09-01',
#                                      language='en',
#                                      sort_by='relevancy',
#                                      page=2)

print(all_articles)
# prints all q variables results from every news source w/i the last 7 days
results = api.get_everything(q='Cory Booker')
# create pd dataframe - JSON to panda
# panda to CSV
# with open('CB_News.csv', 'w') as f: - figure out where to place this to write my results to a csv named CB_News
#   f.write(results.csv)  - learning how to write the results to a csv using the csv library  
print(results)

