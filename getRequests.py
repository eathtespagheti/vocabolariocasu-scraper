from Definition import *
import requests


def getCenter(URL: str):
    """
    return the div with the "center" class
    """
    # Make request
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Explore all the items to find the letters links
    html = list(soup.children)[2]
    body = list(html.children)[3]
    container = list(body.children)[1]
    content = list(container.children)[1]
    return list(content.children)[3]


def getLettersLinks(WEBPAGE_BASE: str):
    """
    Find all the letters links in the page
    """
    center = getCenter(WEBPAGE_BASE)
    ricerca = list(center.children)[1]
    links = {}
    for letter in ricerca.findAll('a'):
        links[letter.text] = letter.get('href')
    return links


def getWords(WEBPAGE_BASE: str, LetterLink: str):
    """
    Find all the definitions which starts with a certain letter
    """
    center = getCenter(WEBPAGE_BASE + LetterLink)
    lemmi = list(center.children)[3]
    links = {}
    for word in lemmi.findAll('a'):
        links[word.text] = word.get('href')
    return links


def getDefinition(WEBPAGE_BASE: str, WordLink: str):
    """
    Find all the definitions which starts with a certain letter
    """
    center = getCenter(WEBPAGE_BASE + WordLink)
    definizioni = list(center.children)[5]
    testo = list(definizioni.children)[2]
    word = Definition(testo)
    word.parseDefinition()
    return word
