#!/bin/python3
"""
A game about space craft and interplanertary and interstellar flight.
Inspiration from the game `Spaceflight Simulator`.
"""

if __name__ == '__main__':
    import turtle


WINDOW = turtle.Screen()
WINDOW.setup(0.75)
WINDOW.title("Space Simulator")


from json import load, dump
from typing import NoReturn
from tkinter import Canvas, Tk, Toplevel


CANVAS: Canvas = turtle.getcanvas()
ROOT_CANVAS: Toplevel | Tk = CANVAS.winfo_toplevel()



def save_data(data: dict [str, dict | list],
              path: str,
              ) -> None:

    """
    Saves data to the database.

    :param dict data: Edited database to save as the new data.
    :param str path: Path to a database to save the new data to.

    :return None:
    """

    with open(path, 'w') as file:
        dump(data, file, indent = 2)

    return


def load_data(path: str,
              ) -> dict:

    """
    Return the contents of the file at path

    :param str path: Filepath to the database

    :return dictionary:
    """

    with open(path, 'r') as file:
        data: dict = load(file)

    return data
