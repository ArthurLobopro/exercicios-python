colors = {
    "black": 30,
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
    "white": 37
}

BG_COLORS = {
    "black": 40,
    "red": 41,
    "green": 42,
    "yellow": 43,
    "blue": 44,
    "magenta": 45,
    "cyan": 46,
    "white": 47
}

STYLES = {
    "bold":      1,
    "underline": 4,
    "negative":  7,
    "default": 0
}


def cprint(string: str, color="", bgcolor="", style="default", end="\n", reset=True):
    print(creturn(string, color, bgcolor, style, reset=reset), end=end)


def creturn(string: str, c="", bgc="", style="default", reset=True):
    if c in colors:
        c = colors[c]

    style_code = STYLES[style]

    if not bgc in BG_COLORS:
        return f"\033[{style_code};{c}m{string}" + "\033[0m" if reset else ""

    bgc = BG_COLORS[bgc]

    return f"\033[{style_code};{c};{bgc}m{string}" + "\033[0m" if reset else ""
