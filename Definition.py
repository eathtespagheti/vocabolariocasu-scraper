from bs4 import BeautifulSoup, element


class Definition:
    """
    Single dictionary word with definition and examples
    """
    word: str
    definition: str
    raw: element.Tag

    def __init__(self, raw: element.Tag):
        """
        Initialize the Definition with the raw data
        """
        self.raw = raw
        self.definition = ""

    def __parseWord__(self):
        """
        Parse word field from the raw data
        """
        self.word = self.raw.find('strong').text

    def __parseDefinition__(self):
        """
        Parse definition field from the raw data
        """
        for item in list(self.raw.children):
            if type(item) == element.NavigableString:
                self.definition += str(item)
            if type(item) == element.Tag:
                if item.name != 'strong':
                    self.definition += str(item)

    def parseDefinition(self):
        """
        Parse the definition fields from the raw data
        """
        self.__parseWord__()
        self.__parseDefinition__()

    def print(self):
        """
        Print the definition
        """
        print(self.word)

    def toDict(self):
        """
        Convert the class istance data to a JSONable dict
        """
        data = {
            "word": self.word,
            "definition": self.definition,
            "raw": str(self.raw)
        }
        return data
