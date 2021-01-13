def cprint(string, c='', bgc='', style=0):
    colors = {
    'white':  0,
    'red':    1,
    'yellow': 3,
    'blue':   4,
    'purple': 5,
    'cyan':   6,
    'gray':   7
    }
    styles = {
        'bold':      1,
        'underline': 4,
        'negative':  7
    }
    if c != '':
        c= ('3{}'.format(colors[c]))
    if bgc!= '':
        bgc= ('4{}'.format(colors[bgc]))
    if style != 0:
        style = styles[style]
    if bgc=='':
        print ('\033[{};{}m{}'.format(style, c, string), end='\033[m')
    else:
        print ('\033[{};{};{}m{}'.format(style, c, bgc, string), end='\033[m')