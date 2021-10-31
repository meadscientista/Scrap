#!/usr/bin/env python
# coding: utf-8

# In[5]:


import time
import praw
import pandas as pd
import urllib.request
import random

from datetime import datetime
from instauto.api.client import ApiClient
import os
from instauto.api import structs as st
from instauto.api.actions import post as ps
import os

from instauto.api.client import ApiClient
from instauto.api import structs as st
from instauto.api.actions import post as ps
from instauto.api.client import ApiClient
#from instauto.helpers.post import 
import os

from instauto.api.client import ApiClient
from instauto.api import structs as st
from instauto.api.actions import post as ps


# In[6]:


reddit_read_only = praw.Reddit(client_id="hHHfLs9QE2IBr5yAjs1nyQ",client_secret="Tmqr2pbbFIHwbKncHxtevH_TuL_Eqw",user_agent="jjjjjjjjjjgmailcom")


# In[7]:


import pandas as pd
subreddit = reddit_read_only.subreddit("dankmemes")

posts = subreddit.top("hour")
# Scraping the top posts of the current month

posts_dict = {"Title": [], "Post Text": [],
			"ID": [], "Score": [],
			"Total Comments": [],"Username": [], "Post URL": [] ,"Type":[]
			}

for post in posts:
	# Title of each post
	posts_dict["Title"].append(post.title)
	
	# Text inside a post
	posts_dict["Post Text"].append(post.selftext)
	
	# Unique ID of each post
	posts_dict["ID"].append(post.id)
	
	# The score of a post
	posts_dict["Score"].append(post.score)
	
	# Total number of comments inside the post
	posts_dict["Total Comments"].append(post.num_comments)
	posts_dict["Username"].append('u/'+post.author.name)
	# URL of each post
	posts_dict["Post URL"].append(post.url)
	posts_dict["Type"].append(post.url.split('.')[-1])
        

# Saving the data in a pandas dataframe
top_posts = pd.DataFrame(posts_dict)
top_posts = pd.DataFrame(posts_dict)
top_posts=top_posts[(top_posts["Type"] == 'jpg')  | (top_posts["Type"] == 'jpeg')]
print(top_posts)


# In[8]:


countl=len(posts.__dict__)
print(countl)

# In[9]:


usepost=top_posts.iloc[random.randint(0,countl)]


# In[10]:



print(usepost['Post URL'])

# In[11]:
typep=usepost['Post URL'].split('.')[-1]

#usename=f"{usepost['ID']}.jpeg"
usename=f"{usepost['ID']}.{typep}"

# In[13]:


urllib.request.urlretrieve(usepost['Post URL'], usename)


# In[ ]:

print(usename)



# In[14]:




# In[15]:


#client = ApiClient(username='stinky_may_mays', password='Neeri@2021')
client = ApiClient(username='majorflyer', password='Neeri@2021')

client.log_in()

print('Connected')

# In[16]:


'''
#client = ApiClient(username=os.environ.get("INSTAUTO_USER") or 'majorflyer', password=os.environ.get("INSTAUTO_PASS") or 'Neeri@2020')
#client = ApiClient(username='stinky_may_mays', password='Neeri@2021')
client = ApiClient(username=os.environ.get("INSTAUTO_USER") or 'stinky_may_mays', password=os.environ.get("INSTAUTO_PASS") or 'Neeri@2021')

client.log_in()
#client.save_to_disk('./.instauto.save')
'''


# In[17]:

try:
    client.save_to_disk('./.instauto.save')
except:
    try:
        client.save_to_disk('./.instauto.save')
    except:
        print("Couldn't save")
    
#client.save_to_disk('./.instauto.save')


# In[89]:


#client = ApiClient(username=os.environ.get("INSTAUTO_USER") , password=os.environ.get("INSTAUTO_PASS") )


# In[18]:


print(usepost['Title']+'\n'+'Credits: '+usepost['Username'])


# In[91]:


#captionx=str(usepost['Title']+'\n'+'Credits: '+usepost['Username'])


# In[19]:


captionx=usepost['Title']
print(captionx)


# In[93]:


# In[ ]:





# In[21]:


pathx="./"+usename
#pathx=fname


print(pathx)


# In[23]:
time.sleep(5)

post = ps.PostFeed(
    path=pathx,
    caption=captionx
)

print("Post Created")

resp = client.post_post(post, 80)
print("Success: ", resp.ok)
