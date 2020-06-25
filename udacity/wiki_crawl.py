### wikipedia Web Crawl Case Study

import time
import requests
import re
import urllib
from bs4 import BeautifulSoup


"""
program does:
1. open an article
2. Find the first link in the article ( download html, find first link, add lint to chain)
3. Record the link in the article_chain data structure
4. Follow the link
5. repeat this process untill we reach the Philosophy article ( or get stuck )
6. The loop should stop when
    - the link is already visited
    - we reach Philosophy
    - we go on for too long ( eg. 25 steps)
    - we found a page that doesn't have a link in it
"""
# pseudocode
# page = a random starting page
# article_chain = []
# while title of page isn't 'Philosophy' and we have not discovered a cycle:
#     append page to article_chain
#     download the page content
#     find the first link in the content
#     page = that link
#     pause for a second

class WikiCrawl():
    #target_url = 'https://en.wikipedia.org/wiki/Philosophy'
    # changed target ot science because Philosophy doesn't work
    target_url  = 'https://en.wikipedia.org/wiki/Science'
    
    def __init__(self, page):
        self.starting_page = page
        self.article_chain = [page]

    def _check_element(self, element):
        """ function check html element with different conditions and returns first link as a string or None.
         """
        if len(element.find_all("a", recursive=False)) > 0:
            for link in element.find_all("a", recursive=False):
                # print(f" all links in element are {element.find_all('a', recursive=False)}")
                if link.get('href'):
                    if "wiki/Help:" in link.get('href') or "wiki/File:" in link.get('href'):
                        continue
                    else:
                        article_link = link.get('href')
                        return article_link

    def find_first_link(self):
        """ Takes page url as string, download HTML and return first link as a string
            or returns None if there is no link
        """
        url = self.article_chain[-1]
        # get HTML from url , use the requests library
        res = requests.get(url)
        html = res.text
        # get the HTML into Beautiful Soup
        soup = BeautifulSoup(html, "html.parser")
        content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
        
        article_link = None
        for element in content_div.find_all("p", recursive=False):
            article_link = self._check_element(element)
            if article_link:
                break
            
        if not article_link:
            return
        first_link = urllib.parse.urljoin("https://en.wikipedia.org/", article_link)
        # find the first link in the article
        # return the first link as a string or return None
        return first_link
    
    def update_article_chain(self, link):
        """ add founded first link to the article_chain to track visited pages """
        return self.article_chain.append(link)

    def continue_crawl(self):
        """ if function return False the crawling should stop """
        if self.article_chain[-1] == self.target_url:
            print("We've found the target article!")
            print(f"We get target in {len(self.article_chain)} steps!")
            return False
        elif len(self.article_chain) > 25:
            print("The search has gone on suspiciously long, aborting search!")
            return False
        elif len(self.article_chain) != len(set(self.article_chain)):
            print("We've arrived at an article we've already seen; aborting search!")
            return False
        else:
            return True
    
    def run_crawl(self):
        """  """
        while self.continue_crawl():
            # print(f" Last element of list {self.article_chain[-1]}")
            # download HTML and find link
            first_link = self.find_first_link()
            # add link to article_chain
            # print(f"Update chain with link  === {first_link}")
            self.update_article_chain(first_link)
            # delay for 2 second
            time.sleep(2)
        [print(item) for item in self.article_chain]


#url = 'https://en.wikipedia.org/wiki/William_Wurster'
url = "https://en.wikipedia.org/wiki/Special:Random"
#url = 'https://en.wikipedia.org/wiki/Meaning_(linguistics)'
#url = 'https://en.wikipedia.org/wiki/William_Wurster'

#url = 'https://en.wikipedia.org/wiki/A.J.W._McNeilly'

find_new = WikiCrawl(url)
find_new.run_crawl()
         

