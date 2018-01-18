""" The Girl from the Other Side comic downloader"""
import os
import urllib.request
import requests
from bs4 import BeautifulSoup

for chapter_number in range(1, 22):
    chapter_number = 20.6
    page = requests.get('http://mangakakalot.com/chapter/totsukuni_no_shoujo/chapter_' + str(chapter_number))
    soup = BeautifulSoup(page.content, 'html.parser')
    images = soup.select("#vungdoc img")

    for image in images:
        urllib.request.urlretrieve(image['src'], image['src'].split('/')[-1])
    os.system('zip -vm cp0' + str(chapter_number) +'.cbz *.jpg')
