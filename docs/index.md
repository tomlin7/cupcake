# Cupcake Editor 🧁

Cupcake is a code editor that can be embedded in tkinter applications, with syntax highlighting support for over 500+ programming languages, autocompletions, minimap, and many more editing features. The codebase was extracted from the [**Biscuit project**](https://github.com/tomlin7/biscuit) and published as an embeddable widget library. Scroll down to see cupcake in action.

- **Syntax Highlighting** - Over 500+ languages supported
- **Auto completions** - Words and keywords
- **Customizable** - Custom themes and fonts
- **Diff Viewer** - Side-by-side comparison of files, integrate with Git
- **Minimap** - Overview of the code, for quick navigation
- **Breadcrumbs** - Pathview tree
- **Image Viewer** - View images in the editor

![cupcakepreview-modified](https://github.com/user-attachments/assets/cf0855db-f651-40bf-bffe-f1d70a13bb30)

```py
import tkinter as tk
from cupcake import Editor, Languages

root = tk.Tk()

e = Editor(root, language=Languages.TYPESCRIPT)
e.pack(expand=1, fill=tk.BOTH)
e.content.insert(
    "end",
    """// check this out
import "./global.css";
import App from './App.svelte';

const app = new App({
	target: document.body
});

export default app;
""",
)

root.mainloop()
```

For more examples like **Diff viewer**, **Image viewer**, **Custom Theming**, see [/examples](./examples).

## Installation

```
pip install cupcake-editor
```

## The Editor Component

Picks the right editor based on the path, path2, diff values passed. Supports showing diff, images, text files. If no arguments are passed, empty text editor is opened.

### Attributes

| option                | type                                                                                            | description                                                                                                                                                            | field type |
| --------------------- | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| master                | `tk.Widget`                                                                                     | The parent tkinter widget                                                                                                                                              | mandatory  |
| path                  | `str`                                                                                           | Absolute path to the file to be opened                                                                                                                                 | optional   |
| path2                 | `str`                                                                                           | Absolute path to be opened in right hand side (if diff)                                                                                                                | optional   |
| diff                  | `bool`                                                                                          | Whether to be opened in diffviewer                                                                                                                                     | optional   |
| language              | [`cupcake.Language`](https://github.com/billyeatcookies/cupcake/blob/main/cupcake/languages.py) | This is given priority while picking suitable highlighter. If not passed, guesses from file extension.                                                                 | optional   |
| dark_mode             | `bool`                                                                                          | Sets the editor theme to cupcake dark if True, or cupcake light by default. This is ignored if custom config_file path is passed                                       | optional   |
| config_file           | `str`                                                                                           | Absolute path to the custom config (TOML) file, uses theme defaults if not passed. [see examples](https://github.com/billyeatcookies/cupcake/blob/main/cupcake/config) | optional   |
| showpath              | `bool`                                                                                          | Whether to show the breadcrumbs for editor or not                                                                                                                      | optional   |
| font                  | `str`/`tk.font.Font`                                                                            | Font used in line numbers, text editor, autocomplete. defaults to Consolas(11)                                                                                         | optional   |
| uifont                | `str`/`tk.font.Font`                                                                            | Font used for other UI components (breadcrumbs, trees)                                                                                                                 | optional   |
| preview_file_callback | `function`/`lambda`                                                                             | Called when files in breadcrumbs-pathview are single-clicked. MUST take an argument (path)                                                                             | optional   |
| open_file_callback    | `function`/`lambda`                                                                             | Called when files in breadcrumbs-pathview are double clicked. MUST take an argument (path)                                                                             | optional   |

### Methods

| function       | description                                              |
| -------------- | -------------------------------------------------------- |
| `Editor.save`  | If the content is editable writes to the specified path. |
| `Editor.focus` | Gives focus to the content.                              |

**Additionally**, All the **tk.Text** widget methods are available under **Editor.content** (eg. `Editor.content.insert`, `Editor.content.get`)

## Features

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
