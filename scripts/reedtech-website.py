#!/usr/bin/env python
# coding: utf-8

# In[1]:


from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import urllib


# In[2]:


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)


def main():
    url_base = "https://patents.reedtech.com"
    raw_html = simple_get(f"{url_base}/pgyb.php#15874")
    html = BeautifulSoup(raw_html, 'html.parser')
    tarballs = [td.a['href'] for td in html.select('td') if td.a and td.a['href'].endswith('.tar')]
    for t in tarballs:
        parts = t.split('/')
        filename = parts[-1]
        if filename.startswith('18'):
            print(f"{url_base}/{t}")


if __name__ == "__main__":
    main()



