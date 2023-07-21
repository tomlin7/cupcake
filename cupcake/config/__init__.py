import toml, os
from tkinter import font
from types import SimpleNamespace

from .styles import Style

class Config:
    def __init__(self, master, config_file=None, darkmode=True):
        self.base = master

        if not config_file:
            config_file = 'dark.toml' if darkmode else 'light.toml'

        self.dir = os.path.dirname(__file__)
        self.font = font.Font(family="Consolas", size=11)
        self.load_from(config_file)
    
    def load_from(self, config_file: str):
        self.theme = SimpleNamespace(**toml.load(os.path.join(self.dir, config_file)))
        self.theme.editor = SimpleNamespace(**self.theme.editor)
        self.theme.diffeditor = SimpleNamespace(**self.theme.diffeditor)
        self.syntax = self.theme.syntax

        self.style = Style(self.base, self.theme)
