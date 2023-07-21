# Cupcake: Embeddable Code Editor
![image](https://github.com/billyeatcookies/cupcake/assets/70792552/11dbd746-f5c0-41cd-8ee3-e2b9328faf17)
![image](https://github.com/billyeatcookies/cupcake/assets/70792552/a489a4a1-da96-4ab5-a498-47e6dd6cb36c)

Cupcake is an **Embeddable** modern-looking code editor for **python tkinter** applications. It has rich **Autocompletions**, **Minimap** and **Semantic Syntax highlighting**. Cupcake is written in pure python with the tkinter library. It is the code editor which powers [Biscuit](https://github.com/billyeatcookies/Biscuit).
```py
import tkinter as tk
from cupcake import Editor, Languages

root = tk.Tk()
root.minsize(800, 600)

e = Editor(root, language=Languages.TYPESCRIPT)
e.pack(expand=1, fill=tk.BOTH)

e.content.insert("end", """
// check this out
import "./theme.scss";
import "./global.css";
import App from './App.svelte';

const app = new App({
	target: document.body
});

export default app;
""")

root.mainloop()

```
see [**examples**](./examples/) for instructions on **Diff viewer**, **Image viewer** and **Theming**

## Syntax Highlighting & Minimap

<img src=https://user-images.githubusercontent.com/70792552/162617464-65169951-fc20-44f3-9f24-a7d80cb6eb10.gif />

## Auto completions 
<img src=https://user-images.githubusercontent.com/70792552/162617435-a9145e3e-e380-4afd-8e78-cbeedeb1bd24.gif />


<!-- ![something](.github/res/screenshot.png) -->

## Installation
Cupcake can be installed by running:
```
pip install cupcake-editor
```
Cupcake requires Python 3.10+ to run.

## Quick start
Here is a quick example of embedding cupcake in your project:
```py
import tkinter as tk
from cupcake import Editor 

root = tk.Tk()
root.minsize(800, 600)

editor = Editor(root)
editor.pack(expand=1, fill=tk.BOTH)

root.mainloop()
```

## Examples!
Examples demonstrating how to use cupcake are in the [examples](./examples) directory. You can learn how to integrate the editor to your app with these. You can run the examples like `python -m examples.hello`

## Features

- [x] Syntax Highlighting (over 500+ languages supported)
- [x] Auto=Completions (words + keywords)
- [x] Auto-Indentation
- [x] Diff Viewer
- [x] Minimap
- [x] Breadcrumbs and Pathview tree
- [x] Image Viewer
- [x] Fully Customizable and Themable 
- [x] Language Detection from File Extensions
- [ ] Code Folding

### Contributing
Your contributions and support are greatly appreciated! 🧡 See [contributing](./CONTRIBUTING.md) for further details such as coding guidelines and tools used.
