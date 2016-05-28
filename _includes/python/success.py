import curses, sys

def success(s):
    colors = curses.tigetstr('setaf')

    def color(n):
        return curses.tparm(colors, n) if colors else ''

    sys.stdout.write(color(2) + s + color(0))

curses.setupterm()
success('Hello, World!\n')
