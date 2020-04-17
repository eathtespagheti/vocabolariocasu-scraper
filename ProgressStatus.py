from TimeManagement import TimeManager
from fileIO import save_dict_to_json, save_list_to_json, get_item_from_json, check_if_path_exist


class ProgressStatus:
    """
    Class containing all the status variables for the script execution
    """
    # Time
    time: TimeManager
    # Links
    json_words_reference: list
    number_of_definitions: int
    # Progress
    processed_definitions: int
    last_word_source_index: str
    last_word_processed_index: str
    skipped_words: list
    # Save location informations
    filename: str
    save_folder: str
    #
    __links_subname__: str
    __progress_subname__: str
    __skipped_subname__: str

    def __init__(self, save_folder: str = "", filename: str = "status"):
        self.time = TimeManager()
        self.json_words_reference = []
        self.number_of_definitions = 0
        self.processed_definitions = 0
        self.save_folder = save_folder
        self.filename = filename
        self.last_word_processed_index = -1
        self.skipped_words = []
        self.__links_subname__ = "links"
        self.__progress_subname__ = "progress"
        self.__skipped_subname__ = "skipped"

    def __get_filename__(self, data_type: str):
        """
        Return the composed filename for saving
        """
        return self.filename + "_" + data_type + ".json"

    def __to_dict_link__(self):
        """
        Store and return the links class data to a dict
        """
        data = {
            "json_words_reference": self.json_words_reference,
            "number_of_definitions": self.number_of_definitions
        }
        return data

    def __to_dict_progress__(self):
        """
        Store and return the progress class data to a dict
        """
        data = {
            "processed_definitions": self.processed_definitions,
            "last_word_source_index": self.last_word_source_index,
            "last_word_processed_index": self.last_word_processed_index
        }
        return data

    def save_links(self):
        """
        Save the links to the json file
        """
        save_dict_to_json(self.__to_dict_link__(),
                          self.__get_filename__(self.__links_subname__), self.save_folder)

    def save_progress(self):
        """
        Save the links to the json file
        """
        save_list_to_json(self.__to_dict_progress__(),
                          self.__get_filename__(self.__progress_subname__), self.save_folder)

    def save_skipped(self):
        """
        Save the skipped words to the a json file
        """
        save_dict_to_json(self.skipped_words,
                          self.__get_filename__(self.__skipped_subname__), self.save_folder)

    def save(self):
        """
        Save all the reusable data to json
        """
        self.save_links()
        self.save_progress()

    def load_links(self):
        """
        Load the links data from the json file
        """
        data = get_item_from_json(self.__get_filename__(
            self.__links_subname__), self.save_folder)
        self.json_words_reference = data.get("json_words_reference")
        self.number_of_definitions = data.get("number_of_definitions")

    def load_progress(self):
        """
        Load the progress data from the json file
        """
        data = get_item_from_json(self.__get_filename__(
            self.__progress_subname__), self.save_folder)
        self.processed_definitions = data.get("processed_definitions")
        self.last_word_source_index = data.get("last_word_source_index")
        self.last_word_processed_index = data.get("last_word_processed_index")

    def load_skipped(self):
        """
        Load the skipped words from the json file
        """
        data = get_item_from_json(self.__get_filename__(
            self.__skipped_subname__), self.save_folder)
        self.skipped_words = data

    def load(self):
        """
        Load all the data from the json files
        """
        if check_if_path_exist(self.__get_filename__(self.__links_subname__), self.save_folder):
            self.load_links()
        if check_if_path_exist(self.__get_filename__(self.__progress_subname__), self.save_folder):
            self.load_progress()
        if check_if_path_exist(self.__get_filename__(self.__skipped_subname__), self.save_folder):
            self.load_skipped()

    def check_saved(self):
        """
        Check if there's a saved istance of ProgressStatus
        """
        return check_if_path_exist(self.__get_filename__(self.__links_subname__), self.save_folder)

    def remaining_items(self):
        """
        Return the number of remaining items
        """
        return self.number_of_definitions - self.processed_definitions

    def skip(self, word: str):
        """
        Skip a work from the download list
        """
        self.skipped_words.append(word)
        self.save_skipped()
