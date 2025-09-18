from colorama import init, Fore, Style

init(autoreset=True)

def printar():
    banner_lines = [
        "  _    _            _    _  _____  _  __",
        " | |  | |          | |  | ||  __ \\| |/ /",
        " | |__| | __ _  ___| | _| || |__) | ' / ",
        " |  __  |/ _` |/ __| |/ / ||  ___/|  <  ",
        " | |  | | (_| | (__|   <| || |    | . \\ ",
        " |_|  |_|\\__,_|\\___|_|\\_\\_||_|    |_|\\_\\"
    ]
    for p in banner_lines:
        print(Fore.GREEN + p + Style.RESET_ALL)  # verde