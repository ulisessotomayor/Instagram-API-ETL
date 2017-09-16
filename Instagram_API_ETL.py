from instagram.client import InstagramAPI
import requests
import json
import pandas as pd
import time
import datetime as datetime

#Enter credentials below
access_token = ''
client_secret = ''

recentMediaResponse = requests.get("https://api.instagram.com/v1/users/self/media/recent/",params = {"access_token": access_token})
recentMediaJson = json.loads(recentMediaResponse.text)

Created_Time, Caption, Type, Filter, Link, Comments, Likes, Tags, Id = [], [], [], [], [], [], [], [], []
for result in recentMediaJson['data']:
    Created_Time.append(result['created_time'])
    Caption.append(result['caption']['text']),
    Type.append(result['type']),
    Filter.append(result['filter']),
    Link.append(result['link']),
    Comments.append(result['comments']['count']),
    Likes.append(result['likes']['count']),
    Tags.append(result['tags']),
    Id.append(result['id'])

df = pd.DataFrame([Created_Time, Caption, Type, Filter, Link, Comments, Likes, Tags, Id]).T

st = time.time()
st = datetime.datetime.fromtimestamp(st).strftime('%Y-%m-%d %H:%M:%S')
df['PullTime'] = st

DF = df.rename(
    columns={0L: 'Created_Time', 1L: 'Caption', 2L: 'Type', 3L: 'Filter', 4L: 'Link', 5L: 'Comments', 6L: 'Likes',
             7L: 'Tags', 8L: 'Id'})

print DF

# db = create_engine('mysql+mysqlconnector://[user]:[pass]@[host]:[port]/[schema]', echo=False)
# cnx = db.connect()
# DF.to_sql(name = 'data_base_table_here', con= cnx, if_exists='append', index=True)
# cnx.close()
# db.dispose()