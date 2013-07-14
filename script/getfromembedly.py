from embedly import Embedly # pip install embedly
import pandas as pd

posts = pd.read_csv('posts.csv', na_filter=False, index_col='id')

client = Embedly('c1df1020e9cc4e1b8abf93c088eacc3d')


start_index = 1 #start from index number (1 to n)
writeabout_text = False

newposts = posts[start_index-1:]
postsforupdate = newposts[(newposts['thumb_url'] == '') | (newposts['title'] == '')]

for index, row in postsforupdate.iterrows():
  
  # Run against embedly if empty thumb_url or title
  if index >= start_index:
    obj = client.oembed(row['link_url']) #make API call - http://embed.ly/docs/embed/api/endpoints/1/oembed

    if obj.type == 'photo':
      posts.ix[index, 'thumb_url'] = obj.url
    else:
      if row['thumb_url'] == '': # only write in field if empty
        posts.ix[index, 'thumb_url'] = obj.thumbnail_url
      if writeabout_text == True and row['about_text'] == '':
        posts.ix[index, 'about_text'] = obj.description
      if row['title'] == '':
        posts.ix[index, 'title'] = obj.description 
    

    print index
    print posts.ix[index, 'thumb_url']
    print posts.ix[index, 'about_text']
    print '\n'

posts.to_csv('posts_forreview.csv', index=True, encoding='utf-8')