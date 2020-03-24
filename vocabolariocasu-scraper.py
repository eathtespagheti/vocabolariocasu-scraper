# from selenium import webdriver
from bs4 import BeautifulSoup
import requests


def getLettersLinks(WEBPAGE_BASE: str):
    """
    Find all the letters links in the page
    """
    # Make request
    page = requests.get(WEBPAGE_BASE)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Explore all the items to find the letters links
    html = list(soup.children)[2]
    body = list(html.children)[3]
    container = list(body.children)[1]
    content = list(container.children)[1]
    center = list(content.children)[3]
    ricerca = list(center.children)[1]
    links = []
    for letter in ricerca.findAll('a'):
        links.append(WEBPAGE_BASE + letter.get('href'))
    return links


# Website base URL
WEBPAGE_BASE = "http://vocabolariocasu.isresardegna.it"

lettersLinks = getLettersLinks(WEBPAGE_BASE)

