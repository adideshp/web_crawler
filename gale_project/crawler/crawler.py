from urllib.request import urlopen
import re
from bs4 import BeautifulSoup


class Crawler:
    def __init__(self, start_url, depth):
        self.start_url = start_url
        self.depth = depth

    def crawl(self):
        seed_url = self.start_url
        depth = self.depth
        target_urls = [seed_url]
        valid_urls = [(seed_url, 0)]
        images_dict = {}
        level = 1
        while level <= self.depth:
            temp_target = []
            urls_list = []
            for url in target_urls:
                html = urlopen(url).read()
                soup = BeautifulSoup(html,features="html.parser")
                anchor_tags = soup.find_all('a', href=True)
                for tag in anchor_tags:
                    if tag.get('href'):
                        urls_list.append(tag.get('href'))
                for link in urls_list:
                    if link.find(self.start_url) !=-1:
                        valid_urls.append((link, level))
                        temp_target.append(link)
                    elif link[0] == "/":
                        valid_urls.append((self.start_url + link, level))
                        temp_target.append(self.start_url + link)
                
                if level+1 > self.depth:
                    if not(url in images_dict):
                        images_dict[url] = []
                    
                    images = soup.find_all('img')
                    for img in images:
                        images_dict[url].append(img['src'])            
            level+=1
            target_urls = []
            target_urls = temp_target
        
        return valid_urls



cr = Crawler("https://gale.agency", 1)
res = cr.crawl()
print(res)