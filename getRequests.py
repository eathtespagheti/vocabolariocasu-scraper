from Definition import *
import requests


def get_center(url: str):
    """
    return the div with the "center" class
    """
    # Make request
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Explore all the items to find the letters links
    html = list(soup.children)[2]
    body = list(html.children)[3]
    container = list(body.children)[1]
    content = list(container.children)[1]
    return list(content.children)[3]


def get_letters_links(webpage_base: str):
    """
    Find all the letters links in the page
    """
    center = get_center(webpage_base)
    ricerca = list(center.children)[1]
    links = {}
    for letter in ricerca.findAll('a'):
        links[letter.text] = letter.get('href')
    return links


def get_words(webpage_base: str, letter_link: str):
    """
    Find all the definitions which starts with a certain letter
    """
    center = get_center(webpage_base + letter_link)
    lemmi = list(center.children)[3]
    links = {}
    for word in lemmi.findAll('a'):
        links[word.text] = word.get('href')
    return links


def get_definition(webpage_base: str, word_link: str):
    """
    Find all the definitions which starts with a certain letter
    """
    center = get_center(webpage_base + word_link)
    definizioni = list(center.children)[5]
    testo = list(definizioni.children)[2]
    word = Definition(testo)
    word.parse_definition()
    return word
