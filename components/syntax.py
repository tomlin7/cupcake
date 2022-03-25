from ast import keyword
import json


class SyntaxLoader:
    def __init__(self):
        with open('config/languages/cpp.json') as fp:
            self.syntax = json.load(fp)
        
        self.setup_token_colors()
    
    def get_pattern(self, tokenkind):
        try:
            return self.syntax[tokenkind]
        except KeyError:
            return "#000000"

    def setup_token_colors(self):
        self.keywords = self.get_pattern("keywords")
        self.numbers = self.get_pattern("numbers")
        self.strings = self.get_pattern("strings")
        self.comments = self.get_pattern("comments")

        self.regexize_tokens()

    def regexize_tokens(self):
        self.keywords = [f"\\y{i}\\y" for i in self.keywords] 
        # (?<![A-Za-z]+){i}(?![A-Za-z]+) -- unfortunately, no lookbehind support for tcl regex

        self.keywords = "|".join(self.keywords)
        print(self.keywords)
        self.numbers = "|".join(self.numbers)
        self.strings = "|".join(self.strings)
        self.comments = "|".join(self.comments)
    
    def get_autocomplete_list(self):
        return ["test", "keyword"] # [(i, "keyword") for i in self.keywords]
