import tkinter as tk
from itertools import chain

from ...utils import Toplevel
from .item import AutoCompleteItem
from .kinds import Kinds


class AutoComplete(Toplevel):
    """AutoComplete class.

    Args:
        master: Parent widget.
        items: List of items to autocomplete.
        active: Whether the autocomplete is active.
    """

    def __init__(self, master, items=None, active=False, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.autocomplete_kinds = Kinds(self)
        self.config(padx=1, pady=1, bg=self.base.theme.border)

        self.active = active
        if not self.active:
            self.withdraw()

        self.overrideredirect(True)
        self.wm_attributes("-topmost", True)
        self.grid_columnconfigure(0, weight=1)

        self.menu_items = []
        self.active_items = []
        self.row = 0
        self.selected = 0
        if items:
            # TODO this should be a dict
            self.items = items  # [(completion, type), ...]
            self.add_all_items()
            self.refresh_selected()

    def update_completions(self):
        """Updates and rerenders the completions."""

        self.refresh_geometry()
        self.update_idletasks()
        self.update_all_words()

        term = self.master.get_current_word()

        exact, starts, includes = [], [], []
        for i in self.menu_items:
            if i.get_text() == term:
                exact.append(i)
            elif i.get_text().startswith(term):
                starts.append(i)
            elif term in i.get_text():
                includes.append(i)
        new = list(chain(exact, starts, includes))

        self.hide_all_items()
        if any(new):
            self.show_items(new[:10] if len(new) > 10 else new, term)
        else:
            self.hide()

    def move_up(self, *_):
        """Moves the selection up."""
        if self.active:
            self.select(-1)
            return "break"

    def move_down(self, *_):
        """Moves the selection down."""
        if self.active:
            self.select(1)
            return "break"

    def add_all_items(self):
        """Adds all items to the menu."""
        for i in self.items:
            self.add_item(i[0], i[1] if len(i) > 1 else None)

        self.active_items = self.menu_items
        self.refresh_selected()

    def update_all_words(self):
        """Updates the words in the menu."""
        for word in self.master.words:
            if word not in self.get_items_text():
                self.add_item(word, "word")

        for word in self.menu_items:
            if word.get_text() not in self.master.words and word.get_kind() == "word":
                self.remove_item(word)

    def add_item(self, text: str, kind=""):
        """Adds an item to the menu.

        Args:
            text: Text to add.
            kind: Kind of the item.
        """

        new_item = AutoCompleteItem(self, text, kind=kind)
        new_item.grid(row=self.row, sticky=tk.EW)

        self.menu_items.append(new_item)

        self.row += 1

    def remove_item(self, item: AutoCompleteItem):
        """Removes an item from the menu.

        Args:
            item: Item to remove.
        """

        a = self.menu_items
        item.grid_forget()
        self.menu_items.remove(item)
        self.row -= 1

    def select(self, delta: int):
        """Selects an item.

        Args:
            delta: The change in selection.
        """

        self.selected += delta
        if self.selected > len(self.active_items) - 1:
            self.selected = 0
        elif self.selected < 0:
            self.selected = len(self.active_items) - 1
        self.refresh_selected()

    def reset_selection(self):
        """Resets the selection."""

        self.selected = 0
        self.refresh_selected()

    def refresh_selected(self):
        """Refreshes the selected item."""

        for i in self.active_items:
            i.deselect()
        if self.selected < len(self.active_items):
            self.active_items[self.selected].select()

    def get_items_text(self):
        """Gets the text of all items.

        Returns:
            List of text of all items.
        """

        return [i.get_text() for i in self.menu_items]

    def hide_all_items(self):
        """Hides all items."""

        for i in self.menu_items:
            i.grid_forget()

        self.active_items = []
        self.row = 1

    def show_items(self, items: list[AutoCompleteItem], term: str):
        """Shows the items.

        Args:
            items: Items to show.
            term: The term to match.
        """

        self.active_items = items
        for i in items:
            i.grid(row=self.row, sticky=tk.EW)
            self.row += 1

            i.mark_term(term)

        self.reset_selection()

    def refresh_geometry(self, *_):
        """Refreshes the geometry of the menu."""

        self.update_idletasks()
        self.geometry("+{}+{}".format(*self.master.cursor_screen_location()))

    def show(self, pos: tuple[int, int]):
        """Shows the menu.

        Args:
            pos: Position to show the menu.
        """

        self.active = True
        self.update_idletasks()
        self.geometry("+{}+{}".format(*pos))
        self.deiconify()

    def hide(self, *_):
        """Hides the menu."""

        self.active = False
        self.withdraw()
        self.reset()

    def reset(self):
        """Resets the menu."""

        self.reset_selection()

    def choose(self, this=None, *_):
        """Chooses an item.

        Args:
            this: The item to choose. Used when user clicks on an item.
        """

        if not self.active_items:
            return

        if not this:
            this = self.active_items[self.selected]

        self.master.confirm_autocomplete(this.get_text())
        self.hide()
        return "break"
