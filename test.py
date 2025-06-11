import curses

#stdscr.clrtoeol() se utiliza para renderizar solo la linea que esta siendo editada
#stdscr.clrtobot() se utiliza para renderizar multiples lineas
#stdscr.clear() se utiliza para renderizar toda la pantalla. Me puede ser util para buscar archivos o querer salir del sistema.

#Configuracion inicial. Queda en duda de por que deberia implementar el primer punto
#curses.curs_set(1) Cursos normal
#stdscr.keypad(True) Habilita teclas especiales

class Window():
    def __init__(self, n_row, n_col):
        self.n_row = n_row
        self.n_col = n_col

class Cursor():
    def __init__(self, pos_y = 0, pos_x = 0):
        self.pos_y = pos_y
        self.pos_x = pos_x

    def up(self):
        if self.pos_y > 0:
            self.pos_y -= 1

    def down(self, window_y):
        if self.pos_y < window_y:
            self.pos_y += 1

    def left(self):
        if self.pos_x > 0:
            self.pos_x -= 1

    def right(self, window_x):
        if self.pos_x < len(window_x):
            self.pos_x += 1

def main(stdscr):    
    #Variables del editor
    text = ""
    cursor = Cursor()
    window = Window(curses.LINES - 1, curses.COLS - 1)


    while True:
        key = stdscr.getch()

        if key == 27:
            break
        elif 32 <= key <= 126:
            text += chr(key)
        elif key == curses.KEY_BACKSPACE:
            if text:
                text = text[:-1]

        elif key == 13 or key == 10:
            cursor.down(window.n_row)
            text = ""
        
        stdscr.move(cursor.pos_y,cursor.pos_x)
        stdscr.clrtoeol()
        stdscr.addstr(text)
        stdscr.refresh()














if __name__=="__main__":
    curses.wrapper(main)
