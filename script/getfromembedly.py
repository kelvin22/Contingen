from embedly import Embedly
import pandas as pd

posts = pd.read_csv('posts.csv')

client = Embedly('c1df1020e9cc4e1b8abf93c088eacc3d')


for index, row in posts.iterrows():
  obj = client.oembed(row['link_url'])

  if obj.type == 'photo':
    posts.ix[index, 'thumb_url'] = obj.url
  else:
    posts.ix[index, 'thumb_url'] = obj.thumbnail_url
    posts.ix[index, 'about_text'] = obj.description
  
  print index
  print posts.ix[index, 'thumb_url']
  print posts.ix[index, 'about_text']
  print '\n'

# posts.to_csv('postsnew.csv', index='FALSE')