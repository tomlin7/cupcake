# Cupcake 🧁

[Docs](https://billyeatcookies.github.io/cupcake/pages/docs.html) |
[Gallery](https://billyeatcookies.github.io/cupcake/index.html) |
[Releases](https://github.com/billyeatcookies/cupcake/releases)

<!--
<table>
    <td>
        <a href=https://billyeatcookies.github.io/cupcake/pages/docs.html>Docs</a>
    </td>
    <td>
        <a href=https://billyeatcookies.github.io/cupcake/index.html>Documentation</a>
    </td>
    <td>
        <a href=https://github.com/billyeatcookies/cupcake/releases>Releases</a>
    </td>
</table> -->

Cupcake is the code editor that powers [Biscuit](https://github.com/billyeatcookies/Biscuit), written in pure python with the tkinter library. See a good list of the code editor's features [here](#features). It is licensed under the [MIT License](./LICENSE).

<table>
    <td>
        <img src=https://user-images.githubusercontent.com/70792552/162617435-a9145e3e-e380-4afd-8e78-cbeedeb1bd24.gif />
    </td>
    <td>
        <img src=https://user-images.githubusercontent.com/70792552/162617464-65169951-fc20-44f3-9f24-a7d80cb6eb10.gif />
    </td>
</table>

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

- [x] Syntax Highlighting
- [x] Auto completions
- [x] Auto Indentation
- [x] Minimap
- [x] Find Replace
- [ ] Extendable language support
- [ ] Code Debugging
- [ ] Language Detection
- [ ] Code Folding


### Contributing
Thank you if you are considering to contribute to Cupcake. See [contributing](./CONTRIBUTING.md) for further details such as coding guides and editing tools used.
