from enum import Enum

Colors = {
    "BLACK": "\u001b[30m",
    "RED": "\u001b[31m",
    "GREEN": "\u001b[32m",
    "YELLOW": "\u001b[33m",
    "BLUE": "\u001b[34m",
    "MAGENTA": "\u001b[35m",
    "CYAN": "\u001b[36m",
    "WHITE": "\u001b[37m"
}

def print_color(msg: str, color: str):
    print(Colors[color] + msg + "\u001b[0m")

def print_shelf():
    print("--------------------------------")

def input_color(msg: str, color: str):
    return input(Colors[color] + msg + "\u001b[0m")
