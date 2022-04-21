from ast import keyword
import json


class SyntaxLoader:
    def __init__(self):
        with open('src/config/languages/cpp.json') as fp:
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
        self.rgx_keywords = "|".join([f"\\y{i}\\y" for i in self.keywords])
        self.rgx_numbers = "|".join(self.numbers)
        self.rgx_strings = "|".join(self.strings)
        self.rgx_comments = "|".join(self.comments)
    
    def get_autocomplete_list(self):
        return [(i, "keyword") for i in self.keywords]
