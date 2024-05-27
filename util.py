import array
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

def print_color(msg, color: str):
    print(Colors[color] + msg + "\u001b[0m")

def print_shelf():
    print("--------------------------------")

def input_color(msg, color: str):
    return input(Colors[color] + msg + "\u001b[0m")


def startmenu_details_editor(header: str, ctx: array):
    """
    keep detail names unique
    """

    cache = []
    final_user_answer = None
    
    for i in range(len(ctx)):
        cache.append([str(ctx[i]), ""])

    while (not final_user_answer):
        print_shelf()
        print(header)
        for i in range(len(cache)):
            pair = cache[i]
            print(f"{i+1} - {pair[0]}: " + pair[1])
        print("quit - stop editing and cancel.")
        print("done - proceed with the given details.")
        print_shelf()

        inp = input()

        if inp == "done":
            final_user_answer = "done"
            break
        elif inp == "quit":
            final_user_answer = "quit"
            break
        
        for i in range(len(cache)):
            if str(i+1) == inp:
                cache[i][1] = input("value:")
                break
    
    print("Exiting details editor.")

    if final_user_answer == "quit":
        return None
    elif final_user_answer == "done":
        dc = {}
        # return dict
        for i in cache:
            dc[i[0]] = i[1]
        return dc
        
        




