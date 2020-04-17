from bs4 import BeautifulSoup, element


class Definition:
    """
    Single dictionary word with definition and examples
    """
    word: str
    meaning: str
    raw: element.Tag

    def __init__(self, raw: element.Tag):
        """
        Initialize the Definition with the raw data
        """
        self.raw = raw
        self.meaning = ""

    def __parse_word__(self):
        """
        Parse word field from the raw data
        """
        self.word = self.raw.find('strong').text

    def __parse_definition__(self):
        """
        Parse definition field from the raw data
        """
        for item in list(self.raw.children):
            if type(item) == element.NavigableString:
                self.meaning += str(item)
            if type(item) == element.Tag and item.name != 'strong':
                self.meaning += str(item)

    def parse_definition(self):
        """
        Parse the definition fields from the raw data
        """
        self.__parse_word__()
        self.__parse_definition__()

    def print(self):
        """
        Print the definition
        """
        print(self.word)

    def to_dict(self):
        """
        Convert the class istance data to a JSONable dict
        """
        data = {
            "word": self.word,
            "definition": self.meaning,
            "raw": str(self.raw)
        }
        return data
