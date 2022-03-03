import json as jn
import tkinter.font as font

class Config:
    def __init__(self, *args, **kwargs):
        self.load_config()
        
        self._cfg = {}

    def load_config(self):
        with open("config/config.json", "r") as fp:
            self._cfg = jn.load(fp)

        self.font = font.Font(
            family=self._cfg["font"],
            size=13, weight="normal")
            
