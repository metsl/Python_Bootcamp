import re


class Input:
    def __init__(self, file, pattern):
        self.file = file
        self.pattern = pattern

    def in_data(self):
        """""
        input data from the file
        """
        data = open(self.file, "r")
        result = ""
        for line in data:
            if re.match(f"(.+) {self.pattern} (.+)", line):
                result = result + line
        return result

    # print("{:s}\n{:s}\n".format(result, len(result) * "^"))   #underlines with ^ the whole line.

    def get_output_option(self):
        """""
        underlining matching text (not with ^) on -u
        Highlighting matching text on -c
        outputting machine readable output on -m
        outputting regular text on -x
        """
        choice = input("Enter -u ( -- for underscore )\nEnter -c ( --color highlighting )\nEnter -m ( --machine "
                       "readable output \nEnter -x for standard output")
        if choice == 'u':
            formatted_text = []
            for t in result.lower().split():
                if t == self.pattern:
                    formatted_text.append("\\033[4m" + t + "\033[0m")
                else:
                    formatted_text.append(t)

            return " ".join(formatted_text)

        elif choice == 'c':
            formatted_text = []
            for t in result.lower().split():
                if t == self.pattern:
                    formatted_text.append("\033[92m" + t + "\033[0m")
                else:
                    formatted_text.append(t)

            return " ".join(formatted_text)
        # print( "\033[92m {}\033[00m" .format(line))  #highlights the whole line, not pattern

        elif choice == 'm':
            pass  # machine readable input

        elif choice == 'x':
            return result


def get_data():
    file: str = input("enter filename:")
    pattern: str = input("enter text to be searched:")
    return file, pattern

# ??????
i = input()
if __name__ == '__main__':
    get_data()
