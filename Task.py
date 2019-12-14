import re

file: str = input("enter filename:")
pattern: str = input("enter text to be searched:")


class InputOutput:

    def in_data():
        """""
        input data from file
        """
        data = open(file, "r")
        result = ""
        for line in data:
            if re.match(f"(.+) {pattern} (.+)", line):
                result = result + line
        return result

    def __init__(self, file, pattern):
        self.file = file
        self.pattern = pattern

    # asking user for inputting any of 3 options: underscoring, highlighting and generate machine readable output
    print("Available output options:\nEnter -u ( --underscore )\nEnter -c ( --color highlighting )\nEnter -m ( "
          "--machine readable output \nEnter -x for standard output")

    # print("{:s}\n{:s}\n".format(result, len(result) * "^"))   #underlines with ^ the whole line.

    def get_output_option(self, pattern, result):

        """""
        underlining matching text (not with ^) on -u
        Highlighting matching text on -c
        outputting machine readable output on -m
        outputting regular text on -x
        """
        choice = input("Enter -u ( -- for underscore )\nEnter -c ( --color highlighting )\nEnter -m ( --machine "
                       "readable output \nEnter -x for standard output")
        if choice == 'u':
            formattedtext = []
            for t in result.lower().split():
                if t == pattern:
                    formattedtext.append("\\033[4m" + t + "\033[0m")
                else:
                    formattedtext.append(t)

            print(" ".join(formattedtext))

        elif choice == 'c':
            formattedtext  = []
            for t in result.lower().split():
                if t == pattern:
                    formattedtext.append("\033[92m" + t + "\033[0m")
                else:
                    formattedtext.append(t)

            print(" ".join(formattedtext))
        # print( "\033[92m {}\033[00m" .format(line))  #highlights the whole line, not pattern

        elif choice == 'm':
            pass  # machine readable input

        elif choice == 'x':
            print(result)
        return 0
