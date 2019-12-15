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
        with open( path, 'r' ) as file:
            for line in file.readlines():
                if re.findall( pattern, line, re.I ):
                    print(line)
        return line

