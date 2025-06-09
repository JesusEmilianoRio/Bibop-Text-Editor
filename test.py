import curses

KEY_EDITION = {
    "KEY_BACKSPACE" : "BACKSPACE",
    "\n" : "SPACEBAR",
}

KEY_NAVEGATION = {
    "KEY_UP" : "FLECHA ARRIBA",
    "KEY_DOWN" : "FLECHA ABAJO",
    "KEY_LEFT" : "FLECHA IZQUIERDA",
    "KEY_RIGHT" : "FLECHA DERECHA"
}



def main(stdscr):
    stdscr.clear()
    stdscr.refresh()

    while True:
        key = stdscr.getkey()
        
        stdscr.addstr(0, 0, " " * 50)

        if key in KEY_EDITION:
            stdscr.addstr(0,0, KEY_EDITION[key])
        elif key in KEY_NAVEGATION:
            stdscr.addstr(0,0, KEY_NAVEGATION[key])
        # "Mostrar" el linezo (actualizar pantalla real)
        stdscr.refresh()

if __name__=="__main__":
    curses.wrapper(main)
