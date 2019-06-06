from urllib.request import urlopen
import re, os, sys
from bs4 import BeautifulSoup
from django.db.models.signals import post_save
from django.dispatch import receiver
import urllib.error
import os
import sys
 
from django.utils import timezone 
 

class Crawler:
    def __init__(self, start_url):
        self.start_url = start_url

    def get_urls(self, source_url, start_url):
        try:
            html = urlopen(source_url).read()
        except urllib.error.HTTPError as e:
            return []
        soup = BeautifulSoup(html,features="html.parser")
        urls_list = []
        valid_urls = []
        anchor_tags = soup.find_all('a', href=True)
        for tag in anchor_tags:
            if tag.get('href'):
                urls_list.append(tag.get('href'))
        for link in urls_list:
            if link.find(start_url) !=-1:
                valid_urls.append(link)
            elif link[0] == "/":
                valid_urls.append(start_url + link)
        return valid_urls

                        
    def get_images(self, source_url):
        try:
            html = urlopen(source_url).read()
        except urllib.error.HTTPError as e:
            return []
        soup = BeautifulSoup(html,features="html.parser")
        images = soup.find_all('img')
        result = []
        for img in images:
            result.append(img['src'])
        return result


        #Driver function that starts the spider
    def start(self, depth):
        result = {"result" : []}
        if depth == 1:
            page_list = self.get_urls(self.start_url, self.start_url)
            for page in page_list:
                result["result"].append([page_list])
        elif depth >= 2:
            intermediate_result = self.spider(self.start_url, self.start_url, depth)
            result["result"] = intermediate_result
        return result


    def spider(self, parent_url, seed_url, depth):
        if depth == 0:
            leaf_result = {"images": self.get_images(parent_url)}
            return leaf_result
        else:
            crawl_result = []        
            for url in self.get_urls(parent_url, seed_url):
                result = self.spider(url, seed_url, depth -1)
                crawl_result.append([url ,result])
            return crawl_result

