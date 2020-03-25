from bs4 import BeautifulSoup, element


class Definition():
    """
    Single dictionary word with definition and examples
    """
    word: str
    definition: str
    examples: list
    raw: element.Tag

    def parseWord(self):
        self.word = self.raw.find('strong').text

    def print(self):
        print(self.word)
