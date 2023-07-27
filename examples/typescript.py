"""
Cupcake with TypeScript lexer
"""

import sys, timeit
from os.path import abspath, dirname, join
sys.path.append(abspath(join(dirname(__file__), '..')))

import tkinter as tk
from cupcake import Editor, Languages

root = tk.Tk()
root.minsize(800, 600)

e = Editor(root, language=Languages.TYPESCRIPT, darkmode=False)
e.pack(expand=1, fill=tk.BOTH)

e.content.write("""import "./theme.scss";
import "./global.css";
import App from './App.svelte';

const app = new App({
	target: document.body
});

export default app;
""")

root.mainloop()
