#spotify search API
import requests
import json

base_url = 'https://itunes.apply.com/search'

#make a request
url = base_url + '?term=the+beatles&country=us'
#instead of the above we can also do:
r = requests.get(base_url, params = {'term': 'the beatles', 'country':'us'})
print(r.url)

#we can also add a limit request by adding 'limit':200 under params
print(requests.get(url, verify = False))


#store the response

#insepct the structure of the response


#locate the release of the song


#print all song names

#print release data of all songs

#we can strucutre and export the data by using the dataframe for an API request and we cna also conver it to a file format as well
# import pandas as pd
# songs_df = pd.DataFrame(info["results"])
# print(songs_df)


#pagination:separation through page format
#we will look into github jobs API
base_site = 'https://jobs.github.com/positions.json'
r = requests.get(base_site, params = {'decription':'data science', 'location': 'los angeles'})

r.json() #returns all the returned data
r.keys() #shows us the keys int he data
#the return showed a small list so we will look at a broader perspective
r = requests.get(base_url)
r.json()
#and we can go through the pages by doing
r = requests.get(base_site, params = {'page':2})
r.json #we will be shown the second page and so on

#to extract data from multiple pages we can do

results = []
for i in range(5):
    r = requests.get(base_site, params={'page':i+1})
    if len(r.json()) ==0: #if we hit the end of the page then stop it
        break
    else:
        results.extend(r.json()) # to add multiple thigns to an object we do .extend() if we were to do append it will add the new list as an array inside an array

