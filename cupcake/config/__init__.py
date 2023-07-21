import toml, os
from tkinter import font
from types import SimpleNamespace


class Config:
    def __init__(self, master, config_file=None, darkmode=True):
        self.base = master

        if not config_file:
            config_file = 'dark.toml' if darkmode else 'light.toml'

        self.dir = os.path.dirname(__file__)
        self.font = font.Font(family="Consolas", size=11)
        self.theme = SimpleNamespace(**toml.load(os.path.join(self.dir, config_file)))
        self.syntax = self.theme.syntax
    
    def load_from(self, config_file: str):
        self.theme = SimpleNamespace(**toml.load(os.path.join(self.dir, config_file)))
        self.syntax = self.theme.syntax
    
        