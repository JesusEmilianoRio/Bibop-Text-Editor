import curses
import argparse
#stdscr.clrtoeol() se utiliza para renderizar solo la linea que esta siendo editada
#stdscr.clrtobot() se utiliza para renderizar multiples lineas
#stdscr.clear() se utiliza para renderizar toda la pantalla. Me puede ser util para buscar archivos o querer salir del sistema.

#Configuracion inicial. Queda en duda de por que deberia implementar el primer punto
#curses.curs_set(1) Cursos normal
#stdscr.keypad(True) Habilita teclas especiales

#key == 13 or key == 10 ENTER
#key == 27 ESC
#KEY >= 32 AND KEY <= 126
class Window():
    def __init__(self, n_row, n_col):
        self.n_row = n_row
        self.n_col = n_col


#Prueba del Cursor. Todavia faltan modificaciones.
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

def read_mode(filename, key_movement): #Esta funcion realizara el comportamiento del editor en modo ES
    try:
        with open(filename, "r") as f:
            buffer = f.readlines()


def insert_mode(): #Esta funcion realizara el comportamiento del editor en modo "i"
    pass

def main(stdscr):    
    #Variables del editor
    text = ""
    mode = True
    
    #Tama;o de la ventana
    window = Window(curses.LINES - 1, curses.COLS - 1)

    #Movimiento del cursor
    cursor = Cursor()





    #Parsear un archivo.
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    while True:
        key = stdscr.getch()
        
        if key == 27: #esc
            mode = True
        if key == 105: #i

        if mode:
            read_mode()
        else:
            insert_mode()
            
        #elif 32 <= key <= 126:
        #    text += chr(key)
        #elif key == curses.KEY_BACKSPACE:
        #    if text:
        #        text = text[:-1]

        #elif key == 13 or key == 10:
        #    cursor.down(window.n_row)
        #    text = ""
        
        #stdscr.move(cursor.pos_y,cursor.pos_x)
        #stdscr.clrtoeol()
        #stdscr.addstr(text)
        #stdscr.refresh()














if __name__=="__main__":
    curses.wrapper(main)
