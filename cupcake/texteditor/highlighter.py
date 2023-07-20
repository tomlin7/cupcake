import os, tkinter as tk

from pygments import lex
from pygments.token import Token
from pygments.lexers import get_lexer_for_filename, guess_lexer
from pygments.util import ClassNotFound


class Highlighter:
    def __init__(self, master, *args, **kwargs):
        self.text = master
        
        Keyword = "#0000ff"
        Name = "#267f99"
        Function = "#795e26"
        String = "#b11515"
        Number = "#098658"
        Comment = "#098658"
        Punctuation = "#3b3b3b"

        try:
            self.lexer = get_lexer_for_filename(os.path.basename(master.path), inencoding=master.encoding, encoding=master.encoding)
        except:
            self.lexer = None

        self.tag_colors = {
            Token.Keyword: Keyword,
            Token.Keyword.Constant: Keyword,
            Token.Keyword.Declaration: Keyword,
            Token.Keyword.Namespace: Keyword,
            Token.Keyword.Pseudo: Keyword,
            Token.Keyword.Reserved: Keyword,
            Token.Keyword.Type: Keyword,

            Token.Name: Name,
            Token.Name.Attribute: Name,
            Token.Name.Builtin: Name,
            Token.Name.Builtin.Pseudo: Name,
            Token.Name.Class: Name,
            Token.Name.Constant: Name,
            Token.Name.Decorator: Name,
            Token.Name.Entity: Name,
            Token.Name.Exception: Name,
            Token.Name.Function:  Function,
            Token.Name.Function.Magic: Function,
            Token.Name.Property: Name,
            Token.Name.Label: Name,
            Token.Name.Namespace: Name,
            Token.Name.Other: Name,
            Token.Name.Tag: Name,
            Token.Name.Variable: Name,
            Token.Name.Variable.Class: Name,
            Token.Name.Variable.Global: Name,
            Token.Name.Variable.Instance: Name,
            Token.Name.Variable.Magic: Name,

            Token.String: String,
            Token.String.Affix: String,
            Token.String.Backtick: String,
            Token.String.Char: String,
            Token.String.Delimiter: String,
            Token.String.Doc: String,
            Token.String.Double: String,
            Token.String.Escape: String,
            Token.String.Heredoc: String,
            Token.String.Interpol: String,
            Token.String.Other: String,
            Token.String.Regex: String,
            Token.String.Single: String,
            Token.String.Symbol: String,

            Token.Number: Number,
            Token.Number.Bin: Number,
            Token.Number.Float: Number,
            Token.Number.Hex: Number,
            Token.Number.Integer: Number,
            Token.Number.Integer.Long: Number,
            Token.Number.Oct: Number,

            Token.Comment: Comment,
            Token.Comment.Hashbang: Comment,
            Token.Comment.Multiline: Comment,
            Token.Comment.Preproc: Comment,
            Token.Comment.PreprocFile: Comment,
            Token.Comment.Single: Comment,
            Token.Comment.Special: Comment,

            # Operator: "#"
            # Operator.Word: "#"

            Token.Punctuation: Punctuation,
            Token.Punctuation.Marker: Punctuation,
        }
        self.setup_highlight_tags()

    def setup_highlight_tags(self):
        for token, color in self.tag_colors.items():
            self.text.tag_configure(str(token), foreground=color)

    def highlight(self):
        if not self.lexer:
            return
        
        for token, _ in self.tag_colors.items():
            self.text.tag_remove(str(token), '1.0', tk.END)
            
        text = self.text.get_all_text()

        # NOTE:  Highlighting only visible area
        # total_lines = int(self.text.index('end-1c').split('.')[0])
        # start_line = int(self.text.yview()[0] * total_lines)
        # first_visible_index = f"{start_line}.0"
        # last_visible_index =f"{self.text.winfo_height()}.end"
        # for token, _ in self.tag_colors.items():
        #     self.text.tag_remove(str(token), first_visible_index, last_visible_index)
        # text = self.text.get(first_visible_index, last_visible_index)

        self.text.mark_set("range_start", '1.0')
        for token, content in lex(text, self.lexer):
            self.text.mark_set("range_end", f"range_start + {len(content)}c")
            self.text.tag_add(str(token), "range_start", "range_end")
            self.text.mark_set("range_start", "range_end")
            
            # DEBUG
            # print(f"{content} is recognized as a <{str(token)}>")
        # print("==================================")
