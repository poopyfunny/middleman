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

def collect_details_menu(header: str, ctx: array):
    cache = []
    final_user_answer = None
    
    for i in range(len(ctx)):
        cache.append([str(ctx[i]), ""])

    while (not final_user_answer):
        print_shelf()
        print(header)
        for i in range(len(cache)):
            pair = cache[i]
            print(f"{i} - {pair[0]}: " + pair[1])
        print("c - cancel")
        print("f - finish")
        print_shelf()

        inp = input("select:")
        if inp == "f":
            final_user_answer = "f"
            break
        elif inp == "c":
            final_user_answer = "c"
            break
        
        for i in range(len(cache)):
            if str(i) == inp:
                cache[i][1] = input("value:")
                break
    
    print("Exiting details editor.")

    if final_user_answer == "c":
        return None
    elif final_user_answer == "f":
        dc = {}
        # return dict
        for i in cache:
            dc[i[0]] = i[1]
        
        




