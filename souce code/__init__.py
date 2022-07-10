#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Marius Wörfel aka Raboro"
__email__ = "raborogit@gmail.com"
__status__ = "Production 07/10/2022"

from gui import GuiMastermind


def main() -> None:
    gui = GuiMastermind()
    gui.create_layout()
    gui.create_window()
    gui.event_loop()


if __name__ == "__main__":
    main()