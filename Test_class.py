import re


class Word:
    def __init__(self, file_path):
        self.file_path = file_path

    def find_regex_match(self, pattern, path=None):
        """""
        input data from the file
        """

        if path is None:
            path = self.file_path
        with open(path, 'r') as file:
            for line in file:
                try:
                    word = re.search(pattern, line)
                    if word is not None:
                        word.group(0)
                    else:
                        print('No word found or typo')
                except Exception:
                    print('Cannot open file or find word')
        return word.group(0)