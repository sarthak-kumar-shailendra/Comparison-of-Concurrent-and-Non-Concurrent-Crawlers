#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests 
import time
from bs4 import BeautifulSoup


# In[2]:


class GILBlocking(object):
 
    def __init__(self, url_list):
 
        self.urls = url_list
        self.results = {}
 
    def __make_request(self, url):
        try:
            r = requests.get(url=url, timeout=20)
            r.raise_for_status()
        except requests.exceptions.Timeout:
            r = requests.get(url=url, timeout=60)
        except requests.exceptions.ConnectionError:
            r = requests.get(url=url, timeout=60)
        except requests.exceptions.RequestException as e:
            raise e
        return r.url, r.text
 
    def __parse_results(self, url, html):
 
        try:
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.find('title').get_text()
        except Exception as e:
            raise e
 
        if title:
            self.results[url] = title
 
    def wrapper(self, url):
        url, html = self.__make_request(url)
        self.__parse_results(url, html)
 
    def get_results(self):
        for url in self.urls:
            try:
                self.wrapper(url)
            except:
                pass


# In[3]:


if __name__ == '__main__':
    q=time.time()
    scraper = GILBlocking(['https://msn.com',
               'https://www.coursera.com',
               'https://github.com/',
               'https://youtube.com',
               'https://www.facebook.com/'])
    scraper.get_results()
    q1=time.time()
    #print(scraper.results)
    for key,val in scraper.results.items():
        print(key+": "+val)
    print("The time taken to crawl the given web pages is: "+str(q1-q))    


# In[ ]:




