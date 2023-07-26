# Cupcake Editor 🧁
![pypi](https://img.shields.io/pypi/v/cupcake-editor) ![issues open](https://img.shields.io/github/issues/billyeatcookies/cupcake) ![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/billyeatcookies/cupcake)

The Cupcake Editor is an embeddable text editor with autocompletions and the fully featured code editor from [Biscuit](https://github.com/billyeatcookies/Biscuit). Scroll down to see some of the supported features.

![image](https://github.com/billyeatcookies/cupcake/assets/70792552/a489a4a1-da96-4ab5-a498-47e6dd6cb36c)

Cupcake has syntax highlighting support for over 500+ programming languages, autocompletions, minimap, and many editing features included. Written in Python using the Tkinter library.

## Installing 
```
pip install cupcake-editor
```

> **Note**
> You need **python 3.10** or above. 

To integrate the editor into your app, here's a quick start!
```py
import tkinter as tk
from cupcake import Editor, Languages

root = tk.Tk()
root.minsize(800, 600)

e = Editor(root, language=Languages.TYPESCRIPT)
e.pack(expand=1, fill=tk.BOTH)

e.content.insert("end", """
// check this out
import "./global.css";
import App from './App.svelte';

const app = new App({
	target: document.body
});

export default app;
""")

root.mainloop()

```
See these [**complete samples**](./examples/) for instructions on **Diff viewer**, **Image viewer** and **Theming**. 
> **Note**
> You can run the examples from the project directory like `python examples/basic.py`

## The Editor Component
Picks the right editor based on the path, path2, diff values passed. Supports showing diff, images, text files. If no arguments are passed, empty text editor is opened. 

### Attributes
|option|type|description|field type|
|---|---|---|---|
|master|`tk.Widget`|The parent tkinter widget|mandatory|
|path|`str`|Absolute path to the file to be opened|optional|
|path2|`str`|Absolute path to be opened in right hand side (if diff)|optional|
|diff|`bool`|Whether to be opened in diffviewer|optional|
|language|[`cupcake.Language`](https://github.com/billyeatcookies/cupcake/blob/main/cupcake/languages.py)|This is given priority while picking suitable highlighter. If not passed, guesses from file extension.|optional|
|dark_mode|`bool`| Sets the editor theme to cupcake dark if True, or cupcake light by default. This is ignored if custom config_file path is passed|optional|
|config_file|`str`|Absolute path to the custom config (TOML) file, uses theme defaults if not passed. [see examples](https://github.com/billyeatcookies/cupcake/blob/main/cupcake/config)|optional|
|showpath|`bool`|Whether to show the breadcrumbs for editor or not|optional|
|font|`str`/`tk.font.Font`|Font used in line numbers, text editor, autocomplete. defaults to Consolas(11)|optional|
|uifont|`str`/`tk.font.Font`|Font used for other UI components (breadcrumbs, trees)|optional|
|preview_file_callback|`function`/`lambda`|Called when files in breadcrumbs-pathview are single-clicked. MUST take an argument (path)|optional|
|open_file_callback |`function`/`lambda`|Called when files in breadcrumbs-pathview are double clicked. MUST take an argument (path)|optional|

### Methods
|function|description|
|---|---|
|`Editor.save`|If the content is editable writes to the specified path.|
|`Editor.focus`|Gives focus to the content.|

**Additionally**, All the **tk.Text** widget methods are available under **Editor.content** (eg. `Editor.content.insert`, `Editor.content.get`)

## Features
### Syntax Highlighting & Minimap (over 500+ languages supported)
<img src=https://user-images.githubusercontent.com/70792552/162617464-65169951-fc20-44f3-9f24-a7d80cb6eb10.gif />

### Auto completions (words + keywords)
<img src=https://user-images.githubusercontent.com/70792552/162617435-a9145e3e-e380-4afd-8e78-cbeedeb1bd24.gif />

## other features
- [x] Auto Indentation
- [x] Diff Viewer
- [x] Minimap
- [x] Breadcrumbs and Pathview tree
- [x] Image Viewer
- [x] Fully Customizable and themable configurations
- [x] Language Detection from File Extensions
- [x] Default dark/light mode themes

### Contributing
Your contributions and support are greatly appreciated! 🧡 See [contributing](./CONTRIBUTING.md) for further details such as coding guidelines and tools used.
